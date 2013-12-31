
================================================================================
The Structure and Interpretation of Computer Programs
================================================================================

:Authors:
    Harold Abelson
    Gerald Jay Sussman
    Julie Sussman

:Abstract:
    ?

:Date: 1984

.. sectnum::

.. contents::
    :depth: 2

Building abstractions with procedures
################################################################################

A *computational processes* executes programs precisely and accurately.

*data*

The evolution of a process is directed by a pattern of rules called a *program*.

People create programs to direct processes.

Master software engineers have the ability to organize programs so they can be
reasonably sure the resulting processes will perform the tasks intended. They
can visualize the behavior of their system in advance. They know how to
structure programs so that unanticipated problems do not lead to catastrophic
consequences, and when problems do arise, they can *debug* their programs.
Well-designed computational systems, like well-designed automobiles or nuclear
reactors, are designed in a modular manner, so that the parts can be
constructed, replaced, and debugged separately.

We need an appropriate for describing processes, and we will use for this
purpose the programming language Lisp. Just as our everyday thoughts are usually
expressed in our natural language, and descriptions of quantitative phenomena
are expressed with mathematical notations, our procedural thoughts will be
expressed in Lisp.

The elements of programming
================================================================================

Expressions
--------------------------------------------------------------------------------

Naming and the environment
--------------------------------------------------------------------------------

Evaluating combinations
--------------------------------------------------------------------------------

Compound procedures
--------------------------------------------------------------------------------

The substitution model for procedure application
--------------------------------------------------------------------------------

Conditional expression and predicates
--------------------------------------------------------------------------------

Example: Square roots by Newton's method
--------------------------------------------------------------------------------

Procedures as black-box abstractions
--------------------------------------------------------------------------------

Procedures and the processes they generate
================================================================================

We don't yet know the common patterns of usage in our domain.

A procedure is a pattern for the *local evolution* of a computational process.

Linear recursion and iteration
--------------------------------------------------------------------------------

Linear recursive process.

Notice that carrying out this process requires that the interpreter keep track
of the multiplication to be performed later on, in computing ``n!``.

Tree recursion
--------------------------------------------------------------------------------

Orders of growth
--------------------------------------------------------------------------------

Exponentiation
--------------------------------------------------------------------------------

Greatest common divisors
--------------------------------------------------------------------------------

Example: Testing for primality
--------------------------------------------------------------------------------

Formulating abstractions with higher-order procedures
================================================================================

Procedures as arguments
--------------------------------------------------------------------------------

Constructing procedures using ``lambda``
--------------------------------------------------------------------------------

Procedures as general methods
--------------------------------------------------------------------------------

Procedures as returned values
--------------------------------------------------------------------------------

Building abstractions with data
################################################################################

Assignment and locate state
================================================================================

Local state variables
--------------------------------------------------------------------------------

The benefits of introducing assignment
--------------------------------------------------------------------------------

The costs of introducing assignment
--------------------------------------------------------------------------------

The environment model of evaluation
================================================================================

The rules for evaluation
--------------------------------------------------------------------------------

Applying simple procedures
--------------------------------------------------------------------------------

Frames as the repository of local state
--------------------------------------------------------------------------------

Internal definitions
--------------------------------------------------------------------------------

Modeling with mutable data
================================================================================

Mutable lists structure
--------------------------------------------------------------------------------

Representing queues
--------------------------------------------------------------------------------

Representing tables
--------------------------------------------------------------------------------

A simulator for digital circuits
--------------------------------------------------------------------------------

Propagation of constraints
--------------------------------------------------------------------------------

Concurrency: Time is of the essence
================================================================================

The nature of time in concurrent systems
--------------------------------------------------------------------------------

Mechanisms for controlling concurrency
--------------------------------------------------------------------------------

Streams
================================================================================

Streams are delayed lists
--------------------------------------------------------------------------------

Infinite streams
--------------------------------------------------------------------------------

Exploiting the stream paradigm
--------------------------------------------------------------------------------

Streams and delayed evaluation
--------------------------------------------------------------------------------

Modularity of functional programs and modularity of objects
--------------------------------------------------------------------------------

Modularity, objects, and state
################################################################################

Metalinguistic abstraction
################################################################################

Computing with register machines
################################################################################
