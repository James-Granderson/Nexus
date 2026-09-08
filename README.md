# Nexus Basketball

Nexus Basketball is a basketball simulation built around one bet: replayability doesn't come from spectacle, it comes from a world that reasons about itself. See [`NEXUS_DESIGN_PRINCIPLES.md`](./NEXUS_DESIGN_PRINCIPLES.md) for the rules the whole engine follows — this doc is the basketball-specific application of them.

## The core idea

Most sports games are a blank slate every time you press play: two teams, a difficulty slider, a score. Nexus instead treats every game as a system carrying history — a player entering a matchup carries his previous performances, his injuries, his confidence, his relationships, his tendencies. Two teams colliding for the fourth time in a playoff series isn't "Game 4," it's "these two systems have collided three times before — what's changed?"

CPU teams don't have a difficulty slider, they have goals. A bad team wants to develop its young players. A contender wants to protect its championship window. A coach doesn't want to get beat one-on-one by a specific opponent. Strategy emerges from those goals colliding, not from a rating check.

The player returns not for another unlock, but because the world keeps presenting questions: why did this team beat me, how did this rookie become a star, can this strategy work against this opponent.

## Systems

### Cognition & memory
Players aren't a stat block. Each has a cognitive profile — pattern recognition, working memory, prediction, adaptability, discipline, decision speed — modeled as a weighted memory cache rather than a fixed IQ number. A rookie might hold 3–5 tendencies about an opponent at once; a veteran holds 8–10. Cognition can also propagate through a team when a smart player communicates what he sees, giving veterans a passive effect on teammates' recognition speed.

### Development
Skill growth is a byproduct of exposure, not a spent stat point. A point guard who takes 2,500 pick-and-roll reps over two seasons develops passing and decision-making because of the reps, not because a level-up screen said so. Ability and production are tracked separately — a player can get better and score less if his role or team changed around him.

### Injuries & physics
Injuries emerge from physical load — joint stress, collision force, landing mechanics, accumulated fatigue — evaluated against tolerance, not rolled from a table. Diagnosis is uncertain and gets refined over time (an on-court "preliminary diagnosis, low confidence" becomes a post-game MRI result). Recovery is a set of measurable states (inflammation, mobility, structural stability, pain tolerance), and doctors can disagree with each other.

### Relationships
Relationships are built from remembered patterns, not a chemistry meter. A teammate doesn't like or dislike you because of a `+2`/`−2` counter — he remembers who gets him involved, who covers his mistakes, who takes his shots away. Memories carry importance, age, and emotional weight, and fade at different rates depending on the player.

### Scouting, media & fog of war
The player never sees ground truth, only what the organization's people believe. A scout report carries a name, a confidence level, and a sample size. Different departments (an amateur scout, an analytics department, a head coach) can describe the same player in contradictory but individually reasonable ways. Media and fan sentiment operate as a public memory system with their own feedback loops — criticism can tank a young player's confidence, and public support from a veteran can offset it.

### Coaching, front office & ownership
Coaches represent a system and a worldview (switch-everything vs. rim-protection-and-post-ups), not a stat boost. GMs evaluate whether a player increases the probability of winning *given the existing roster system*, not just whether his rating is higher. Ownership has its own axis — a championship owner and a rebuilding owner make structurally different decisions from identical financial reports.

### Information architecture
The world is organized into places, not menus, each answering a different question:

| Hub | Answers |
|---|---|
| League Office | What's happening in the league? |
| Team Headquarters | What's happening in my organization? |
| Player Hub | Who is this person? |
| Scouting Department | What do we know, and how confident are we? |
| Medical Department | What's the physical state of our players? |
| Media Network | What does the world think? |

Every piece of information in every hub has a source and a confidence level attached — nothing is presented as bare fact.

### Game modes
Franchise/GM mode is the default frame, but the design supports alternate formats built on the same engine: an 82-0 playoff replacement bracket, a modern-apron salary-cap fantasy draft, a 90s ruleset, FIBA rules, and an Olympic mode with national-roster construction constraints.

## Design philosophy in one line

The game is not about finding the best pieces. It's about understanding the system those pieces create.

## Status

Design phase. Systems above are specified at the philosophy/mechanics level; implementation has not started. See the design principles doc before building anything — if a feature can't be justified by one of those principles, it shouldn't be built.
