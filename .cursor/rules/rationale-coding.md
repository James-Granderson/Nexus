# Rationale Coding

Rationale coding is the Nexus development method. It defines what things mean before writing code and verifies machine behavior before moving on. The final goal is full control and understanding of each nook and cranny in a codebase.

To understand rationale coding, consider its alternative: vibe coding. Vibe coding relies on prompting and immediate syntax generation from artificial intelligence tools. The developer asks a tool for code, accepts output that looks reasonable, and runs it until the error messages disappear. You hand off the entire design process to the LLM.

With vibe coding you can produce classes that compile. With rationale coding you produce classes that actually mean something when the simulation grows, and develop good practice.

Vibe coding accelerates syntax generation, but it defers architectural truth. When a simulation expands, vibe-coded architecture collapses under unexamined assumptions, and a disconnect between programmer and AI intention.

---

### What Rationale Coding Is

Rationale coding starts with a desire for meaning and ends with understanding. Rationale coding is not about hyper-fixating on syntax, files, or class names. It starts with basic questions about reality:

* What is the thing?
* Where does it live?
* What does it live with?
* What changes it?
* What happens when it is copied, moved, or destroyed?

Ask and answer these questions before writing code. Verify them after writing code.

---

### You Decide.


The mechanism behind why rationale coding works because you make the choice.

Vibe coding and blind copy-pasting delegates decisions to outside entities. When an LLM or an external source dictates an implementation, you hand off control of the architecture. You are no longer in the driver seat. You lose control over what you were actually trying to implement.

Take a fight as an example. You would not take a random weapon and head off into battle. You make the choice of taking a sword or knife yourself depending on your situation. That is rationale coding. You decide. You do it yourself. And eventually, you become wiser and sharper than any knife. You choose. You win.

The bad loop that leads to structural failure is:

Question → AI gives implementation → Copy → Compile → Move on

Because the choice has disappeared, six months later you have:

*Code you did not choose*

*Abstractions you do not understand*

*Dependencies you do not remember*

*Methods you never personally evaluated*

This outcome is code decay. Code decay is not caused by bad syntax; it is caused by unevaluated choices.

The rationale loop replaces passive copying with active engineering by forcing you through a sequence of deliberate decisions before code ever enters the architecture.

It begins with the problem itself, stripped of syntax or framework assumptions. Rather than grabbing the first available answer, you identify the possible moves and see what each move does. This means mapping out your options and testing how each candidate approach interacts with system memory, state ownership, and execution flow.

You then understand the consequences of those options—evaluating trade-offs in complexity, lifetime, and performance—so that when you make a choice, it is an intentional act of design rather than an accident of generation. You justify that choice by explicitly defining why this approach fits the physical model and what breaks if it is omitted.

Only after this rationale is established do you implement the code. Once written, you watch it in motion, relying on direct execution traces, memory inspection, and machine output rather than theoretical assumptions. Seeing the machine run yourself allows you to realize the concept—verifying that the relationship between source code, objects, and runtime behavior is completely understood.

Finally, based on physical evidence from execution rather than whether it simply compiled, you make the definitive call to keep, reject, or revise the code.

Through this sequence, AI and external tools remain utility instruments that illuminate candidate moves, while the architectural authority stays entirely with you.




### Ten-Step Process

Complete each step sequentially before starting the next:

1. **Ask what must be true:** Identify reality in the sim, undefined elements, and existing assumptions.
2. **Separate concerns:** Assign concepts to their specific layer. A court is not an arena; a player is not a team. Each concept has one home.
3. **Identify the object:** State what thing is being created, represented, stored, or manipulated.
4. **Justify representation:** State why a field, type, class, pointer, container, or relationship exists and what breaks if omitted.
5. **Defer explicitly:** Mark unknown attributes as `None` or optional with a note rather than leaving them undefined.
6. **Implement:** Write code that mirrors the agreed model. Never invent a model mid-file.
7. **Inspect the result:** Trace what the code created, where it exists, what variables contain, and what changed.
8. **Instantiate and manipulate:** Create the smallest example. Interact with it, change values, copy, pass, print and destroy it.
9. **Observe consequence:** Rely on machine execution output rather than reading text explanations.
10. **Realize the concept:** Move on only when the relationship between code, object, representation, and behavior is understood.

---

### Rationale Before Syntax

Establish intended meaning before writing code. The core question is: *"What thing am I trying to make happen?"* Write the smallest code that represents that intention. 

---

### Play With It

Play is the core of the method. Test features, variables, and functions by curiously asking:

* What is this feature?
* What does this do?
* What happens when I change or pass this in?
* What happens when I attempt to compile or print this object?

Run the machine, break the code, and observe the results. Don't stop at syntax. A developer who plays with code learns what the code is actually doing; a developer who only reads about code learns what someone else said it is.

---

### Code Must Be Inspectable

Isolate new language features, abstractions, data structures, or memory concepts in minimal examples. Compile, run, print, change, and observe them.

* **Pointers:** Establish what the pointer is, what it contains, what it points to, and what changes when the pointed-to value alters.
* **Shared Pointers (`std::make_shared`):** Establish what object is constructed, what the `shared_ptr` represents, how ownership functions, and what memory is involved.

The goal is establishing the direct relationship between source code, objects, memory, ownership, and behavior.

---

### Realization

A concept is learned when you can answer how the object operates in practice:

* What is the thing, why does it exist, and where is it located?
* What represents, contains, or refers to it?
* What causes it to exist and what changes it?
* What is the hierarchy of components?
* What constrains this object, and what does it output?
* What observable behavior follows from these facts?

---

### Nexus Decision Matrix

| Question | Rationale | Result |
| --- | --- | --- |
| Does a player float? | No floor is defined, so 2D coordinate tracking is incomplete. | Add `z` |
| Where is the floor? | The floor is the playing surface, not the building outer shell. | `Court.floor_z` |
| What about the ceiling? | The ceiling is an arena property and rarely affects play state. | `Arena.ceiling_z` (optional) |
| What is default player height? | The player stands directly on the court floor. | `Player.z` defaults to `Court.floor_z` |

---

### Implementation Inspection

Inspect results against the rationale after writing code:

* Did code create the intended thing in the intended location?
* Does the type represent the intent and match ownership models?
* Does behavior follow from initial assumptions?

If any answer is no, stop and resolve the discrepancy before writing more code.

---

### Experiment Before Abstraction

Never test an unfamiliar concept, feature, or memory mutation directly on the main project object. Modifying live structures risks collateral state corruption and hides side effects.

Create an isolated experiment before putting unfamiliar concepts into production architecture:

1. Create the thing.
2. Observe it.
3. Change it.
4. Observe the change.
5. Destroy or release it when relevant.
6. Explain why the behavior occurred.

Use the isolated experiment as physical evidence for architectural decisions. Transfer code to the main project object only after its behavior is fully understood.

---

### Rules

* Do not add coordinates, fields, or classes until their role in the model is clear.
* Do not add syntax merely because it is conventional.
* Do not introduce an abstraction that cannot be explained.
* Keep one home per concept (floor on court, ceiling on arena).
* Discuss and decide when unsure, then write the smallest correct diff.
* Do not move past a concept merely because the code compiles.
* Isolate and experiment with important or unfamiliar concepts.
* Inspect memory, ownership, references, and lifetime when they affect the concept.
* Prefer small coherent architecture over large ambiguous code.
* Justify code before writing it; realize code before building upon it.
* Lay out plans and assumptions before writing code.
* Play with the code.
  
