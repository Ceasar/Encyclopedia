
================================================================================
Propositional logic
================================================================================

Propositional logic is ...

Notation: Let P, Q, R, etc. be propositions.

Do not want to consider paradoxes. For instance, "This sentence is false." A
paradox is a proposition which cannot be decided as either true or false.

Connectives:

1. And (/\ or &&)

2. Or (\/ or ||)


:Definition:
    A theorem in propositional logic is a tautology.

Implications:

Goal: Understand better ``P -> Q``

:Definition:
    In any conditional statement, P -> Q, the statement P is called the
    hypothesis or antecedent and  is called the conclusion or consequent.

:Theorem:
    ``(P -> Q) <-> (not P or Q)``
:Proof:
    By truthtable.

Proofs end with Q.E.D. (quod erat demonstradum "that which was to be shown")

:Definition:
    Given any conditional statement, P -> Q:

    The statement ``Q -> P`` is called its converse.

    The statement ``not P -> not Q`` is called its inverse.

    The statement ``not Q -> not P`` is called its contrapositive.


    If you're over 21, you can drink beer.

    Converse: If you can drink beer, you're over 21.

    Inverse: If you're not over 21, then you can't drink beer.

    Contrapositive: If you can't drink beer, then you're not over 21.

:Theorem:
    A conditional is equivalent to its contrapositive.
:Proof:
    By truth table.

:Corollary:
    The converse is equivalent to the inverse.

Etiquette
================================================================================

Some theorems are more important than others (the fathers of many other
theorems).

Corollaries are less important.

----

Question: How do we state "P is sufficient for Q" and "S is necessary for R" as
implications?

Sufficient: P -> Q

Necessary: R -> S

Bicondtionals:

Task: Understand more about bicondtionals and how they can be stated in plain
English.

:Theorem:
    P <-> Q is equivalent to P -> Q (Q if P, or P only if Q) and Q -> P
:Proof:
    Truthtable.

Ways of expressing in plain English:

1. P iff Q (iff means "if and only if")

2. P is necessary and sufficient for Q.

3. P is equivalent to Q.

4. P and Q are equivalent.

5. P is true only when Q is true. (Bad style.)

Proofs in proposition logic
================================================================================

All proofs that we right are ultimately abbreviations for truth table
calculation.

:Task:
    Use tautologies to write proofs in propositional logic that are more
    complicated than would be reasonable for a me to ask you to on a problem set
    by hand using a truthtable.
 
Is faster (saves us writing) and permits a more human touch to proofs and bears
an individual mark.

:Remark:
    There are infinitely many tautologies, so we usually only remember the
    easiest ones.

Tautologies
================================================================================

The law of the excluded middle: P or not P

Constructivism denies this law. Most mathematicians don't touch this. (This
denies truthtables.)

Law of non-contradiction: not (P and not P)

Law of double-negation: not not P iff P

(P and Q) -> P, (P and Q) -> Q

P -> P or Q

Q -> (P -> Q)

Modus (ponendo) ponens: (P and (P -> Q)) -> Q, "in the way that it is put"

If we prove tautologies by truthtable, how does constructivism deny one that we
can prove is true?

Module tolens: contrapostive of modus ponens

De Morgan's law.

:Definition:
    A statement Q is called a propositional consequence of statement P, ..., P_n
    iff the statement (P and ... and P_n) -> Q

:Definition:
    The assertion that Q is a consequence of some list of statements is called
    an argument.

    The statement in the list are called the premises or hypotheses or givens
    of the argument. Q is called the conclusion. If Q is indeed a consequence of
    the premises, then we call the argument valid.
