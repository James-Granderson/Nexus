# Nexus Design Principles

These are the rules Nexus is built on. They apply to any sport Nexus simulates — basketball is the first, not the only. If a new feature can't be justified by one of these principles, it doesn't belong in the engine.

The one-sentence version: **the game shouldn't tell you what happened, it should tell you why it thinks it happened.**

---

## 1. Every attribute must be qualitative, falsifiable, and measurable

If you can't point to what an attribute actually changes, it's a magic variable and it doesn't belong in the engine.

Before adding any attribute, ask: does it affect shot selection, risk-taking, reaction time, decision quality — something concrete? If you can't answer that, cut it.

This is the filter for the whole system. Don't ask "what feature do we add?" Ask "what measurable property of a real athlete are we trying to model?"

## 2. Every change needs a cause

Never `Passing +5`. Always the chain that produced it: environment → opportunity → repetition → adaptation → skill change → performance change.

Two players can start with identical ratings and diverge completely five years later because they were exposed to different situations, not because the game rolled different dice for them. Ability and production are separate — a player can get better and score less because his role changed. The system tracks the mechanism, not just the outcome.

## 3. Not all X

An event creates a *possibility*, not a guaranteed outcome. Score 40 points, and the reaction isn't `teammates +10, fans +20, coach +5` on rails — it depends entirely on who's reacting.

Not all criticism creates a fracture. Not all playoff games matter equally. Not all rivalries are real rivalries. The event supplies information; it never supplies its own conclusion. If a system can be described as "X always causes Y," it's flattening the world and needs to be rebuilt around probability instead.

## 4. Meaning is supplied by entities, not by the event

A statement has no inherent meaning. "I think I should get more shots" could be ambition, insecurity, or entitlement — the coach, the veteran teammate, and the media will each interpret it differently, based on who *they* are.

A torn hamstring doesn't say "sit him." It says "this player's physical state changed." The doctor, the coach, the player, and the GM each supply a different meaning from the same fact. Design every event object to carry information only — never a built-in verdict.

## 5. Context is the hidden layer under everything

`Event + context + entity + history = interpretation.` Without context you get a spreadsheet: injury = miss games, bad quote = lose reputation, criticism = chemistry −10. With context, the same action means something different depending on when and to whom it happens.

Context is multidimensional — don't collapse it into one axis:

- **Player importance** — superstar, starter, role player, prospect
- **Situation importance** — preseason vs. elimination game
- **Competitive importance** — standings/seeding implications, rivalry, revenge game
- **Personal importance** — contract year, first game vs. former team, milestone
- **Organizational importance** — rebuild vs. championship window, coach on the hot seat

A 70%-healthy star in a random January game gets rested. The same player, same injury, in Game 7 of the Finals plays 25 minutes. The injury didn't change — the equation did. Build context variables (`season_stage`, `player_importance`, `relationship_level`, `risk_tolerance`, `recent_history`) instead of writing special-case rules per scenario (`if finals: increase injury tolerance`). The special cases should never exist in code — they should emerge from the variables.

## 6. Growth and decay, not potential

Reject both bad extremes: a rigid pre-written "92 potential," and pure player-controlled XP spending. Instead, potential is a relationship between time and action — learning speed, physical ceiling, work ethic, opportunity, and environment, all interacting.

A player is good because he had opportunities, made decisions, practiced, and avoided decay — not because the game decided he deserves to be good. This keeps the system egalitarian (everyone runs on the same rules) without making everyone equal (learning speed and ceiling still differ).

## 7. Programming over time — decouple when information arrives from when consequences land

Real processes have delay built in: fetch and decode happen fast, execute happens later. Free agency isn't when a player decides where he wants to be — it's the public conclusion of a process that started months earlier.

Model this explicitly. Some executions are immediate (coach benches a player). Some are delayed (contract talks). Some are conditional ("if you improve your defense, you start"). Some are only potential ("we'll look into getting you help"). A promise is not a scheduled future event — it's a pending possibility the system has to carry forward:

```
Event:
  occurred_at
  discovered_at
  interpreted_at
  consequences_pending
  consequences_triggered
```

The pipeline is `Fetch → Decode → Execute → Persist → Resolve` — not because every system needs five stages, but because the world needs somewhere to hold unfinished business.

## 8. One processing loop, not special-case systems

Every entity — media, coach, GM, teammate — runs the same `Fetch → Decode → Execute` loop. What differs is what each entity knows and how it decodes, never the architecture.

This eliminates "the media system does X, the coach system does Y" special-casing. Adding a new entity type six months from now means plugging into the existing loop, not inventing a new framework.

## 9. Memory is a weighted cache, not a log

Entities don't remember everything, and they don't forget by deleting — they forget by eviction. Give each entity a cache with limited capacity; when it fills, the lowest-scoring memory gets replaced.

Score memories by recency, reinforcement, and impact — not just age. A rookie might hold 3–5 tendencies at once; a veteran might hold 8–10. This produces basketball IQ (or hockey IQ, or any sport's version of it) as an emergent property of cache size, recognition speed, and eviction policy — never as a bare "IQ: 95" stat.

## 10. Game/situation importance is a first-class variable

Most sports simulations treat every game as an identical container for stats. Nexus doesn't. `season_stage`, `elimination_status`, `standings_impact`, `rivalry_level`, and `historical_significance` all feed into how entities interpret what happens in that game — and into what gets stored as a high-priority memory versus forgotten by next week.

A 40-point night in February is a stat line. A 40-point night in Game 7 becomes part of a player's identity, because the *context* multiplies the weight of the memory, not the box score.

## 11. The world is the interface — never expose the machinery

The backend can be as mathematical as it needs to be. The player should never see it directly.

Wrong: `Player confidence modifier +8.` Right: `After struggling early in the season, Higgins has become more aggressive attacking the rim after several successful games.`

This extends to structure, not just copy. The game shouldn't present itself as tabs and sliders — it should present itself as a league office, a team headquarters, a scouting department, a medical department, a media network. The player should feel like they're running an organization, not operating a spreadsheet. Every "menu" should instead be a place with people in it who send reports and have opinions.

## 12. Uncertainty is a feature — the player sees what the organization knows, not the truth

Fog of war isn't a limitation to work around, it's core to the fantasy of scouting and management. A scout report is never ground truth — it's `Scout Michael Anderson — 82% confidence — based on 14 viewed games`. Two scouts watching the same player can produce two different reports depending on their own evaluation strengths.

Information has provenance. It comes from somewhere, carries a confidence level, and can be wrong.

## 13. Design principles come before code

If a feature can't be traced back to one of these principles, don't build it. Code is the translation of the design; it isn't the design itself. When stuck, the question is never "how do I implement this," it's "what is this actually simulating."

## 14. Every action has a physical consequence

Contact is real. A spin move that clips a defender produces a collision, not a clean animation swap. Momentum from a speed burst has to be paid for later — stamina, weight, and fatigue apply, not a costless "turbo" button. If a player is tired, movement gets slower and less precise, visibly.

This principle exists specifically to keep the physics layer honest against real film, not against other sports games' animation systems.

## 15. The simulation is separate from its renderer

World state → simulation → observable state → visualization. Never the reverse (3D model → physics bolted onto the model → hope the model reveals what happened).

The 2D board is not a lesser version of a future 3D game — it's the first correct view of a world that exists independent of any renderer. Rendering code never mutates simulation state; it only reads it.

**The microscope, not junk.** If a possession can run with zero graphics and be fully reconstructed from printed state — positions, velocities, contact points, contact force — the simulation is real. If it can't, the graphics are hiding the fact that there's no simulation underneath them. Debugging a weird animation by staring at it is the wrong move. The right move is asking "what did the simulation believe happened," and reading the state that answers that.

```
Player A
  position: (...)
  velocity: (...)
  hand_position / hand_velocity / hand_orientation: (...)
  possession: true
Ball
  position: (...) velocity: (...) spin: (...)
Contact
  entity_a: Player A   entity_b: Ball
  contact_point: (...)  contact_force: (...)  contact_duration: (...)
```

This gives Nexus three interchangeable windows onto one state: the state view (raw/terminal), the spatial view (2D), and eventually a 3D view. None of them define the world. All of them observe it.

## 16. Scale is measured, not invented

Don't decide the court is "100 units because that's convenient" — establish a correspondence with reality and hold it. An NBA court is 94 feet; Nexus's geometry has to correspond to that, whether the internal unit is called feet, meters, or a normalized coordinate. Pick one convention, document the conversion, and never touch it again out of convenience.

This matters most once physics enters the picture — velocity, gravity, player and hoop dimensions all only mean something if the coordinate system they're expressed in has a fixed relationship to the real world. Coordinates are measurements, not pixels. This is principle 1 applied to geometry instead of attributes: the physical model has to be falsifiable against real basketball, the same way an attribute has to be falsifiable against real behavior.

## 17. Rationale coding, not vibe coding

Reason → specify → translate → execute → observe → prove → update. No decision gets made in code until there's a reason for it to exist — no unjustified library, no extra object, no unrequested feature.

This is "design principles > code" (13) turned into a workflow. The intellectual work — what should this thing do, specified precisely enough that implementing it is close to mechanical — happens before a line of code is written. The implementation language is incidental; the logic belongs to Nexus, not to Python or C++ specifically. When something needs building, the question is never "what feels right here," it's "what did we already decide this needs to do."

---

## Architecture: four layers

Nexus separates cleanly into four layers. Nothing above the simulation layer is allowed to define what's true — everything above it is a window onto the layer below.

**1. Simulation layer — the world.** Players, ball, court, positions, movement, possession, collisions, physics, strategy, cognition, memory, probability. This is the only layer that decides what happened.

**2. Data layer — the knowledge.** Player records, historical games, attributes, relationships, development, scouting information, results — whatever persists. This is SQL territory: Python asks a database questions and gets structured answers back, rather than trying to turn dictionaries into a database engine.

**3. Presentation layer — what the human sees.** The 2D court, players as circles, the ball, the shot clock, menus, eventually richer interfaces. This layer reads simulation state; it never generates it.

**4. Observation layer — the terminal.** The game doesn't have to communicate everything visually. A possession can be fully legible as text:

```
NEXUS — POSSESSION
12.4s  LAL possession
James: right wing   Davis: low post
Defender: attached  Help defender: strong-side
Ball: James

ACTION            James drives right
DEFENSIVE RESPONSE  Help defender rotates
RESULT            Kick-out pass
SHOT              3PT — OPEN
RESULT            MISS
```

That's already a game, before any GUI exists. The build order this implies: get the terminal proving the simulation is correct first (`FETCH → DECODE → EXECUTE → TEST → PRINT`), then build the 2D display around the same state, and only then worry about a polished interface. The first GUI only has to answer "can I see the world the simulation says exists" — court, players, ball, shot clock, movement. Nothing more, and don't rush it.

The GUI doesn't create the simulation. It visualizes the simulation.

---

## How the principles stack

They aren't fifteen unrelated ideas — they're layers of the same philosophy:

- **Growth & Decay** — how things change over time
- **Not All X** — why outcomes aren't predictable
- **Entities Supply Meaning** — who determines the outcome
- **Context** — what conditions change the interpretation
- **Fetch → Decode → Execute (→ Persist → Resolve)** — the architecture that processes all of it
- **Memory with priority/eviction** — how the world remembers at scale
- **Programming Over Time** — when consequences are allowed to land
- **The World Is the Interface** — how all of the above gets shown to the player without ever looking like a spreadsheet

If a new system doesn't plug into this stack, that's a signal the system is wrong, not that the stack needs an exception.

The four-layer architecture (15–17, plus the layer breakdown above) is where this stack becomes buildable: the simulation layer is where all of the above principles actually live, the data layer is where memory and history persist, and presentation/observation are just different windows that read state without ever being allowed to write it.
