
================================================================================
Referential opacity
================================================================================

Referential opacity refers to the inability to replace an expression withs its
value without changing the meaning of a text. The opposite of referential
opacity is referential transparency.

For instance, although "Cicero" and "Tully" both refer to the same person, we
cannot replace "Cicero" for "Tully" in the sentence "Mary believes that Cicero
is a great orator", since Mary might not know that "Cicero" and "Tully" are
coreferent. Such a sentence is called an opaque context.

Example: A function that relies on a global variable, which can have different
results even if called with the same parameters.

Example: Loops use a placeholder expression to holds the object of interest on
any particular iteration, and overwrite it on each iteration.

Note: In mathematics and functional programming, all functions are referentially
transparent.

Note: Referentially transparent expressions are necessarily deterministic.

If all functions involved in an expression are pure functions, then the
expression is referentially transparent.

Only referentially transparent functions can be memoized.
