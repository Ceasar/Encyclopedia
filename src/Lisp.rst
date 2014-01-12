.. include:: index

================================================================================
Lisp
================================================================================

**Lisp** (LISt Processing) is the second oldest `programming language`_ (only
Fortran_ is older).

Lisp was invented in 1958 as a formalism for reasoning about the use of certain
kinds of logical expressions, called *recursion equations*, as a `computational
model`_. [1]_ Despite its inception as a mathematical formalism, Lisp is a
practical programming language.

The language was conceived by `John McCarthy` and is based on his paper
`Recursive Functions of Symbolic Expressions and Their Computation by Machine`.
[1]_

The first Lisp interpreter_ was implemented by McCarthy with the help of
colleagues and students in the Artificial Intelligence Group of the MIT Research
Laboratory of Electronics and in the MIT Computation Center. [1]_

Lisp was designed to provide symbol-manipulating capabilities for attacking
programming problems such as the symbolic differentiation and integration of
algebraic expressions. It included for this purpose new data objects known as
atoms and lists, which most strikingly set it apart from all other languages of
the period. [1]_

Lisp was not the product of a concerted design effort. Instead, it evolved
informally in an experimental manner in response to user's needs and to
pragmatic implementation considerations. Lisp's information evolution has
continued through the years, and the community of Lisp users has traditionally
resisted attempts to promulgate any "official" definition of the language. [1]_

Because of its experimental character and its emphasis on symbol manipulation,
Lisp was at first very inefficient for numeric computations, at least compared
to Fortran_. Over the years, however, Lisp compilers have been developed that
translate programs into `machine code`_ that can perform `numerical
computations`_ reasonably efficiently.

Lisp is used in many applications where efficiency is not a concern. For
example, Lisp has become a language of choice for operating-system shell
languages and for extension languages for editors and computer-aided design
systems. [1]_

Lisp possesses unique features that make it an excellent medium for studying
important programming constructs and data structures and relating them to to the
linguistic features that support them. The most significant of these features is
the fact that Lisp descriptions of processes, called *procedures*, can
themselves by represented and manipulated as Lisp data. The importance of this
is that there are powerful program-design techniques that rely on the ability to
blur the traditional distinction between 'passive' data and 'active' processes.


.. [1] `Abelson Sussman 1984`_
