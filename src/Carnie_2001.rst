
.. include:: index

================================================================================
Syntax
================================================================================

:Author: Andrew Carnie

:Date: 2001

:Abstract:
    This book is intended as an introduction to syntactic theory. It takes the
    student through most of the major issues in Principles and Parameters, from
    tree drawing to constraints on movement.

.. contents::

.. sectnum::

################################################################################
Preliminaries
################################################################################

********************************************************************************
Generative Grammar
********************************************************************************

Preliminaries
================================================================================

Definitions are given for the following terms:

- Syntax_

- Language_

- Phonetics_

- Phonology_

- Morphology_

- Semantics_

Syntax as Cognitive Science
================================================================================

Defines `cognitive science`_ and states that language_ is a human property.

Modeling Syntax
================================================================================

We will mostly study the `Principles and Parts approach` version of `generative
grammar`_ although we will occasionally stray from this into `Minimalism`.

Syntax as Science: The Scientific Method
================================================================================

It is a mistake to believe that the study of language should be confined to a
humanistic approach. It is also possible to study language from a scientific
perspective; the domain of linguistics.

In syntax, we apply the scientific method to sentence structure. Syntacticians
start by observing data about the language they are studying, then make
generalizations about patterns in the data. They then generate a testable
hypothesis and test their hypotheses against more syntactic data.

The hypotheses are called rules, and the group of hypotheses that describe a
language's syntax is called a grammar.

We focus on descriptive rules (instead of prescriptive rules) since they give us
insight into how the mind uses languages.

An example is given with anaphors_, demonstrating how they must agree in person,
gender, and number with their antecedents, and showing how this rule evolves
from simpler hypotheses.

Defines `grammatical person`_.

Sources of Data
--------------------------------------------------------------------------------

The two main sources of data for experiments with syntax are corpora and
`grammaticality judgment tasks`_.

Corpora (singular *corpus*) are collections of either spoken or written text
(which sometimes need to be compiled by the research if for instance no literary
tradition exists).

The value of corpora is limited since they only contain instances of grammatical
(or more precisely well-formed) sentences. Due to the infinite and productive
nature of language, a corpus could never contain all the grammatical forms of a
language, nor could it even contains a representative sample.

To really get at what we know about our language, we have to know what sentences
are not well-formed. This kind of information is not available in corpora.

`Grammaticality judgment tasks`_ are used.
In this text, we will be concerned primarily with syntactic well-formedness.

Where do Rules Come From?
================================================================================

This is sort of a side issue, but affects the shape of our theory.

If we know how children acquire their rules, then we are in a better position
for a proper formalization of them. The theory of generative grammar makes
something very specific claims about this.

Learning vs. Acquisition
--------------------------------------------------------------------------------

Cognitive scientists make a distinction in how we get conscious and
subconscious knowledge. Conscious knowledge is *learned*. Subconscious knowledge
is *acquired*.

.. I can't find anything to support this claim.

Not all rules of grammar are acquired. Some facts about language seem to be
built into our brains, or *innate*.

Innateness: Language as an Instinct
--------------------------------------------------------------------------------

Instincts are subconscious knowledge that are built into us. For example,
walking.

Noam Chomsky controversially claims that Language is also an instinct. Many
part of Language are innate.

There are good reasons to believe that a human facility for Language (perhaps in
the form of a "Language organ" in the brain) is innate. We call this facility
`Universal Grammar`_.

The Logical Problem of Language Acquisition
--------------------------------------------------------------------------------

Here we show that from a logical perspective, an infinite productive system like
the rules of language cannot have been learned or acquired.

Infinite systems are neither learnable nor acquirable. Since we have such an
infinite system in our heads, and we can't have learned it, it must be the case
that it is built in. (The argument presented her is based on an unpublished
paper by Alec Marantz)

Language is an infinitely productive system; a speaker can produce and
understand sentences he has never hear before. This is because language is
recursive; it always possible to embed a sentence inside of a larger one.

It turns out that rule-generated infinite systems like language not learninable,
as a simple fact of logic.

Infinite systems are unlearnable because one never has enough input to be sure
one has all the relevant facts. This is called the logical problem of language
acquisition.

Generative grammar gets around this logical puzzle by claiming that Universal
Grammar helps children construct a knowledge of language by restricting the
number of possible functions that map between situations and utterances.

Other Arguments for UG
--------------------------------------------------------------------------------

The evidence for UG doesn't rely on the logical problem alone.

TODO: Return

Explaining Language Variation
--------------------------------------------------------------------------------

Choosing among Theories about Syntax
================================================================================

One last preliminary before actually doing syntax.

How do we know what is a good hypothesis and what is a bad hypothesis?


Generative grammar strives toward explanatorily adequate grammars.

Summary
================================================================================

In this chapter we've done very little syntax but talked a lot about the 

Ideas, rules, and constraints introduced in this chapter:

1. Syntax

2. Language (capital L)

3. language (lower case l)

4. Generative Grammar

5. The Scientific method

6. Grammar

7. Prescriptive grammar

8. Descriptive grammar

9. Anaphor

10. Antecedent

11. Asterisk

12. Number

13. Person

14. Case

15. Nominative

16. Accusative

17. Corpus

18. Native speaker judgements

19. Semantic judgement

20. Syntactic judgement

21. Learning

22. Acquisition

23. Recursion

24. Observationally adequate grammar

25. Descriptively adequate grammar

26. Explanatorily adequate grammar

27. Innate

28. Universal Grammar (UG)

29. The Logical Problem of Language Acqusition

30. Undetermination of the Data

31. Universal

********************************************************************************
Fundamentals: Rules, Trees, Parts of Speech
********************************************************************************

Introduction
================================================================================

Word in a sentence are group into units (called constituents) and that these
constituents are grouped into larger constituents, and so until you get a
sentence.

Parts of speech
================================================================================

Before we we can look at these phrases, we have to briefly look at the kinds of
words that compose them.

If we have categories for words that can appear in certain positions and
categories for those that don't we can make (scientific) generalizations about
the behavior of different word types. This is why we need parts of speech.

We cannot use semantic definition for parts of speech. This is evident for a
number of reasons, including that one can know the part of speech of a word
without even knowing what it means.

The definitions for the various parts of speech are not semantically defined.
Instead, when they are appear in the sentence and by its morphology.

Structure
================================================================================

We have an intuition that certain words are more closely connected than others.
The notion we use to capture these intuitions are *constituency* and *hierarchical
structure*.

Defines constituent_.

Constituency is the most important and basic notion in syntactic theory.

Constituents are embedded in one another to form larger and larger constituents.
This is hierarchical structure. Hierarchical constituent structure can be
represent with a pair of brackets, but they are much harder to read.

Rules and trees
================================================================================

In `generative grammar`, generalizations about structure are represented by
rules, which are said to generate the tree in the mind. So if we draw a tree a
particular way, we need a rule to generate that tree. We consider `phrase
structure rules`_ in this chapter.

:Definition:
    The Golden Rule of Tree Structures: Modifiers are always attached within the
    phrase they modify.

Noun phrases
--------------------------------------------------------------------------------

The simplest noun phrases (NP) only contain a noun. More complex noun phrases
optionally contain a determiner, adjective phrases, and preposition modifiers.

    NP -> (D) (AP+) N (PP+)

    the big book of poems

Adjective phrases and adverb phrases
--------------------------------------------------------------------------------

An adjective phrases (AP) might be something like "a [very yellow] book"

    AP -> (AP) A

    very yellow

In much work on syntactic theory, there is no significant distinction between
adjectives and adverbs. This is because it is isn't clear that they are really
distinct categories.

Prepositional phrases
--------------------------------------------------------------------------------

Most prepositional phrases (PP) take the form of a preposition followed by an
NP. For example "to the store" or "with an ax". Thus the rule appears to be:

    PP -> P NP

There might actually be some evidence for treating the NPs in PP as optional.
There are a class of prepositions, traditionally called particles, that don't
require a following NP. For example, "I haven't see him before" or "It blew up".

    PP -> P (NP)

Verb phrases
--------------------------------------------------------------------------------

Minimally a verb phrase (VP) consists of a single verb. Verbs may be modified by
adverbs which are of course optional. Many adverbs can appear on either side of
the verb and one can have as many adjective phrases as one likes. Verbs can also
take a noun phrase (called the direct object in traditional grammar). Verbs can
also take multiple prepositional phrases.

    VP -> (AP+) V (NP) (PP+) (AP+)

    [frequently] [got] [his buckets] [from the store] [for a dollar]

Clauses
--------------------------------------------------------------------------------

We have not yet accounted for structure of the sentence (or more accurately
clause). A sentence minimally consists of a noun phrase and a verb phrase.

    S -> NP VP

Clauses can also include other items, including modal verbs and auxiliary verbs.
For example, "Alice might crash the boat" or "Alice has crashed the boat". For
lack of a better term, we'll call these items T, for tense, since they bear the
tense inflection in the sentence.

    S -> NP (T) VP

Clauses don't always have to stand on their own. There are items when clauses
are embedded inside other clauses. For example, "Alice said she crashed the
boat." Sometimes these clauses take a special introductory word, which we call a
complementizer (C).

    S' -> (C) S

For the moment we will assumes whether or not they have a complementizer.

Embedded clauses appear in a variety of positions. For instance, in the subject
position:

    [that he decked the janitor] is obvious

Because of this, we are going to have to modify our S and VP rules to allow
embedded clauses. Syntacticians use curly brackets ``{}`` to indicate a choice.
In the following rules you are allow either an NP or an S' but not both.

    S -> {NP / S'} T VP
    VP -> (AP+) V ({NP/S'}) (PP+) (AP+)

Summary
--------------------------------------------------------------------------------

In this section we looked at the `phrase structure rules`_ need to generate
trees that account for English sentences.

#. S' -> (C) S

#. S -> {NP / S'} T VP

#. NP -> (D) (AP+) N (PP+)

#. VP -> (AP+) V ({NP / S'}) (PP+) (AP+)

#. PP -> P (NP)

#. AP -> (AP) A

How to draw a tree
================================================================================

There are two ways to about drawing at tree. Starting at the bottom and working
one's way up to the S, or starting with the S and working down. The decision
depends on one's style.

Bottom-up trees
--------------------------------------------------------------------------------

This method often works best for beginners.

1. Write out the sentence and identify the parts of speech

2. Identify what modifies what.

3. Link together items that modify one another.

4. Keep applying rules until you have attached all the modifiers to the modified
   constituents until you get to the S.

5. Go back and check the tree is valid.

The top-down method of drawing trees
--------------------------------------------------------------------------------

1. Write out the sentence and identify the parts of speech

2. Draw the S with the NP and VP.

Bracketed diagrams
--------------------------------------------------------------------------------

Sometimes it is preferable to use bracketed notation instead of the tree
notation. This is especially true when there are large parts of the sentence
that are irrelevant to the discussion at hand. Drawing bracketing diagrams
essentially follow the same rules for tree drawing.

Modification and ambiguity
=================================================================================

Consider the following two sentences:

1. The man killed the king with a knife

2. The man killed the king with the red hair

Each of these sentences is ambiguous, but for the moment consider the least
difficult reading for each.

1. "The man used a knife to kill the king."

2. "The king with the red hair was killed by the man"

Note, the two original sentence have very similar surface forms.

A paraphrase is another way of saying the same thing.

Syntax trees allow us to capture the differences between ambiguous readings of
the same surface sentence.

See: constiuency tests

Summary and conclusion
=================================================================================

Appendix
=================================================================================

Open vs closed classes of speech


Linguistic theory distinguish two kind of lexical items. Parts of speech are
divided into open and closed class items. Membership in open classes (Nouns,
verbs, adjectives) categories is unlimited. New words may be coined at any time
if they are open class. Membership in closed class by contrast is limited and
coinages are rare.

********************************************************************************
Structural Relations
********************************************************************************

********************************************************************************
Binding Theory
********************************************************************************

################################################################################
The Base
################################################################################

********************************************************************************
X-bar Theory
********************************************************************************

********************************************************************************
Extending the Proposal: TPs, CPs, and DPs
********************************************************************************

********************************************************************************
Constraining X-bar Theory: Theta Roles and the Lexicon
********************************************************************************

################################################################################
Transformation Rules
################################################################################

********************************************************************************
Head to Head Movement
********************************************************************************

********************************************************************************
NP Movement
********************************************************************************

********************************************************************************
Raising, Control, and Empty Categories
********************************************************************************

********************************************************************************
Wh-movement
********************************************************************************

********************************************************************************
Towards Minimalism
********************************************************************************

################################################################################
Alternatives
################################################################################

********************************************************************************
Alternative Approaches: LFG
********************************************************************************

********************************************************************************
Alternative Approaches: HPSG
********************************************************************************

********************************************************************************
Conclusions
********************************************************************************

################################################################################
Where to Go From Here
################################################################################
