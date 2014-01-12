.. include:: index

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

A *computational process* executes programs precisely and accurately.

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

We need an appropriate language for describing processes, and we will use for
this purpose the programming language Lisp_. Just as our everyday thoughts are
usually expressed in our natural language, and descriptions of quantitative
phenomena are expressed with mathematical notations, our procedural thoughts
will be expressed in Lisp. The dialect of Lisp used in this book is called
Scheme.

The elements of programming
================================================================================

A powerful `programming language`_ is more than just a means for instructing a
computer to perform task. The language also serves as a framework within which
we organize our ideas about processes. Thus, when we describe a language, we
should pay particular attention to the means that the language provides for
combining simple ideas to form more complex ideas.

Every powerful language has three mechanism for accomplishing this:

1. Primitive expressions, which represent the simplest entities the language is
   concerned with

2. Means of combination, by which compound elements are built from simpler ones

3. Means of abstraction, by which compound elements can be named and
   manipulated as units

In programming, we deal with two kinds of elements: procedures and data.
Informally, data is stuff that we wish to manipulate, and procedures are
descriptions of the rules for manipulating data. Thus, any powerful
programming language should be able to describe primitive data and primitive
procedures and should have methods for combining and abstracting procedures and
data.

Expressions
--------------------------------------------------------------------------------

When the user types an expression, the interpreter responds by displaying the
result of its evaluating that expression.

Expressions formed by delimiting a list of expressions withing parenthesis in
order to denote procedure application, are called *combinations*. The leftmost
element in the list is called the *operator* and the other elements are called
*operands*. The value of a combination is obtained by applying the procedure
specified by the operator to the *arguments* that are the values of the
operands.

The convention of placing the operator to the left of the operand is known as
*prefix notation*. Prefix notation has several advantages. One of them is that
it can accommodate procedures that may take an arbitrary number of arguments; no
ambiguity can arise, because the operator is always the leftmost element. A
second advantage is that it extends in a straightforward way to allow
combinations to be *nested* (to have combinations whose elements are themselves
combinations).

We can help ourselves by writing expressions following a formatting convention
known as *pretty-printing*, in which each long combination is written so that
the operands are aligned vertically.

Naming and the environment
--------------------------------------------------------------------------------

A critical aspect of a programming language is the means it provides for using
names to refer to computational objects. We say that a name identifies a
*variable* whose *value* is the object.

Definition associates a name with a value.

Names are a language's simplest means of abstraction, for they allow us to use
simple names to refer to the results of compound operations. In general,
computational objects may have very complex structures, and it would be
extremely inconvenient to have to remember and repeat their details each time we
want to use them.

The possibility of associating values with symbols and later retrieving them
means that the interpreter must maintain some sort of memory that keeps track of
the name-object pairs. This memory is called the *environment*.

Evaluating combinations
--------------------------------------------------------------------------------

One of our goals of this chapter is to isolate issues about thinking
procedurally.

The "percolate values upward" form of the evaluation rule is an example of a
general kind of process known as *tree accumulation*.

Exceptions to the general evaluation rule are called *special forms*. Each
special form has its own evaluation rule. The various kinds of expressions (each
with its associated evaluation rule) consitute the syntax of the programming
language.

Compound procedures
--------------------------------------------------------------------------------

The substitution model for procedure application
--------------------------------------------------------------------------------

To evaluate a combination whose operator names a compound procedure, the
interpreter follows much the same process.

Conditional expression and predicates
--------------------------------------------------------------------------------

The expressive power of the class of procedures that we can define at this point
is very limited, because we have no make to make tests and to perform different
operations depending on the result of a test.

The word *predicate* is used for procedures that return true or false, as well
as expressions that evaluate to true or false.

Example: Square roots by Newton's method
--------------------------------------------------------------------------------

Procedures as black-box abstractions
--------------------------------------------------------------------------------

The problem of computing square roots breaks up naturally into a number of
subproblems. Each of these tasks is accomplished by a separate procedure.

The importance of the decomposition strategy is not simply that one is dividing
the programs into parts. After all, we could take any large program and divide
it into parts (e.g. the first ten lines, the next ten lines, the next ten lines,
and so on). Rather, it is crucial that each procedure accomplishes an
identifiable task the can be used as a module in defining other procedures.

When we treat a procedure as a black-box, we are not at the moment concerned
with *how* the procedure computes its result, only with the fact that it *does*.
The details can be suppressed, to be considered at a later time. Indeed,
as far as clients are concerned, services are not quite procedures but rather an
abstraction of a procedure, a so-called *procedural abstraction*. At this level
of abstraction, any procedure that computes the expected result is equally good.

A procedure definition should be able to suppress detail. A user should not need
to know how the procedure is implemented in order to use it.

Local names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One detail of a procedure's implementation that should not matter to the user of
the procedure is the implementer's choice of names for the procedures formal
parameters. Thus the following procedures should be indistinguishable:

    (define (square x) (* x x))

    (define (square y) (* y y))

.. todo: Interesting. Debatable.

This principle, that the meaning of a procedure should be independent of the
parameters names used by its author, seems on the surface to be self-evident,
but its consequences are profound. The simplest consequence is that parameter
names of a procedure must be local to the body of the procedure.

Such a name is called a *bound variable* and we say the procedure definition
*binds* its formal parameters. The meaning of a procedure definition is
unchanged if a bound variable is consistently renamed throughout the definition.

If a variable is not bound, we say that it is *free*.

The set of expressions for which a binding defines a name is called the *scope*
of that name. In a procedure definition, the bound variables declared as the
formal parameters of the procedure have the body of the procedure as their
scope.

Internal definitions and block structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
