
.. _expression:

==========
Expression
==========

An expression is any unit of language that can have meaning (significant).

Example: In natural language, words, phrases, sentences, and text, all are expressions.

An expression is a combination of data and operators that can be evaluated to produce a value.

# Meaning

Assuming a principle of semantic compositionality, the meaning of an expression is determined by the meanings of:

1. Its constituents
2. Its syntactic structure.

## Meaningless expressions

An expression is nonsense if it well-formed (syntactically valid) but not meaningful (semantically invalid).

Example: `1 / 0` is an expression, but has no meaning.
Example: "Colorless green ideas sleep furiously" (Chomsky, Syntactic Structures)
Example: "Blue is circular" (Chomsky, Syntactic Structures)

# Analysis

An expression is composed of:

1. Atoms
2. Expressions

An interpretation of an expression produces a value, which is determined in a systematic way the values it gives to the component expressions.

# Classification

## Simple & Complex

A simple expression is an expression that is composed of an atom.

Example: "4"
Example: "True"

A complex expression is an expression that is not atomic.

Example: "2 + 2"
Example: "not False"

## Referential Transparency & Referential Opaqueness

An expression is referentially transparent iff it can be replaced with its value without changing the behavior of a program.

An expression is referentially opaque iff it is not referentially transparent.

Example: A function that relies on a global variable, which can have different results even if called with the same parameters.
Example: Loops use a placeholder expression to holds the object of interest on any particular iteration, and overwrite it on each iteration.

Note: In mathematics and functional programming, all functions are referentially transparent.

Note: Referentially transparent expressions are necessarily deterministic.

If all functions involved in an expression are pure functions, then the expression is referentially transparent.

Only referentially transparent functions can be memoized.

Morpho-syntactic Hierarchy
==========================

1. Morpheme
2. Word
3. Phrase
4. Phase
5. Sentence (clause)
6. Text
