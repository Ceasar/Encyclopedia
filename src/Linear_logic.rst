
================================================================================
Linear logic
================================================================================

Introduced in a paper in 1987 by a Frenchman, Girard. In the last few pages,
talks about some of the work that went in to development.

Motivated because he was studying semantics of programming languages. In
particular, look at resources. Then he wanted semantics for it.

Tremendously influential. Cited more than 4000 times.

Assumed familiar with propositional logic.


Properties
================================================================================

Resource conscious
--------------------------------------------------------------------------------

Logic that is somehow resource conscious. Not independent of time and space.
When forming a proof, linear hypotheses must be used exactly once. Resources can
be consumed, and here, must be consumed. Eliminating contraction and weakening.

"Communication" behaviors
--------------------------------------------------------------------------------

Can describe communication behavior.

Duality
--------------------------------------------------------------------------------

Central to the idea. Duality between sender and receiver. In logic, correspond
to various kind of DeMorgan's law. Gives some nice symmetries which can be
exploited.

Types as proposition. Linear types as describing state of program or process.

Applications
================================================================================

- Memory management

- Various kinds of states and effects

- Control aliasing

- Capabilities

- Session types (ways of describing protocols over communication channels)

- Concurrency and parallelism

Logical view
================================================================================

- Constructive. Proofs have computational content. Via curry-howard, we can run
  them as program.

- Can embed via encoding both intuitionistic propositional logic and classical
  propositional logic. In some sense, linear logic is lower level than either.

- Proof search. Translating into linear logic can shed light on structure of
  proof. Has led to focusing and polarization in automated proof search.

- Consistent.

- Cut elimination. (notion of duality appears a bit in the proof for this)

- Proof nets.

- Security.

Semantics
================================================================================

Coherent spaces
--------------------------------------------------------------------------------

From the original paper.

Game semantics
--------------------------------------------------------------------------------

Duality of player and opponent.

Categorical semantics
--------------------------------------------------------------------------------

Many languages come equipped with denotational semantics in terms of categorical
semantics.

Models, often degenerate:

- Rel

- Finite vector spaces (FinVec)

- Boolean algebras

- Strict continuous CPO's

----

Introduction to linear logic
================================================================================

Not diving into proof rules and judgments.

What do we mean when carrying out an inference about a system?

Presentation based on paper "Judgmental Analysis of Linear Logic"
[Cheng/Chaudhuri/Pfenning 2003] and Pfenning's lecture notes from first few
lectures.

`Linear types can change the world!` (Wadler 1990)

Deductive systems
--------------------------------------------------------------------------------

Goals:

- ???

- ???

- See how thinking about resources affect perspective

Propositional logic
--------------------------------------------------------------------------------

Come up with some propositions, then uses rules of inference and use them to
build proof. If logic is sound and we can build a proof, then truth correspond
to reality.

Suppose reasoning about graphs. Need some notion of node (constants: a, b, c, d)
and some notion about an edge.

Can think of a graph as a model or structure about which we wish to reason. So
we code up ideas about structure as propositions in logic.

- Might have proposition ``node(x)`` where x ranges over the nodes. ``node(a)``,
  ``node(b)``, etc.

- Might have proposition ``edge(x, y)``. eg. ``edge(a, b)``. Can add rule of
  inference: ``edge(x, y) => edge(y, x)``.

- ``path(x, y)``. ``edge(x, y) => path(x, y)``. ``path(x, y), path(y, z) =>
  path(x, z)``.

Comparison

ll:

- ephemeral

- linear

- true

- contingently true

propositional:

- persistent

- unrestricted

- valid

- necessarily true

Question is, in LL, is how to mix them?
