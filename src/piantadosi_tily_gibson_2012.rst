
================================================================================
The communicative function of |a| in language
================================================================================

:Authors: Steven T. Piantadosi; Harry Tily; Edward Gibson

:Date: October 8 2011

:Journal: `Cognition`_ 122

:Pages: 280-291 (12)

:Keywords:
    |a|_, `language processing`_, `information theory`_, `rational
    design in language`

:Abstract:
    The goal of the present paper is to develop an explanation for |a|_
    which makes fewer assumptions than previous work, and is more generally
    applicable.

    The authors argue that:
    
    1. If context_ provides |i|_ about meaning, then an |ecs| will not redundant
       specify information_ provided by the context_ and will be ambiguous_ out
       of context_.

    2. |A|_ allows for greater ease of `language processing`_ by permitting
       re-use of easy-to-process linguistic units. If reused such that they are
       always well-disambiguated by context and if disambiguation is cheap,
       using the system will require less overall effort.

    The authors test predictions of (2) (that words and syllables which are most
    efficient will be preferentially re-used) in English, German, and Dutch, and
    confirm their hypotheses.

    The author interpret their results as strong evidence for the view that
    |a|_ results from a pressure for efficient communication.

    The authors conclude that their results explain the pervasiveness of |a|_ in
    language and show how |a|_ likely results from ubiquitous pressure for
    efficient communication.

.. contents::

Introduction
================================================================================

|A|_ is a pervasive phenomenon in language which occurs at all levels of
linguistic analysis. The existence of |a|_ provides a puzzle for `functionalist
theories`_. Indeed, the existence of |a|_ has been argued to show that the key
structures and properties of language *have not* evolved for purposes of
`communication`_ or use. Here we argue that this perspective on |a|_ is exactly
backward.

In Zipf's view, |a|_ fits within the framework of his unifying *principle of
least effort*, and could be understood by considering the competing desires of
the speaker and the listener.  Zipf suggest that `natural language`_ would
strike a balance between these two opposing forces of unification and
diversification, arriving at a middle ground with some but not total |a|_.
Zipf's hypothesis of the way |a|_ might arise from a trade-off between speaker
and hearer pressures has certain shortcomings. One example of that illustrates
this trade-off is the NATO phonetic alphabet.

Beyond Zipf, several authors have previously discussed the possibility that |a|_
is a useful feature for a `communication system`_.


Two benefits of |a|
================================================================================

In this section, we present two similar arguments that |ecss| will be ambiguous
when context_ is informative about meaning.

Both assume that:

1. |I|_ is typically present to resolve ambiguities

2. Disambiguation is not prohibitively costly; using |i| from the
   context_ to infer which meaning was intended does not substantially impede
   comprehension.

|A| in general communication
--------------------------------------------------------------------------------

In this section we motivate an `information-theoretic`_ view of |a|_. We argue
that when context_ is informative, any |ecss| will leave out |i|_ already in the
context_ and therefore necessarily appear ambiguous_ when examined out of
context_.

No assumptions are made about the linguistic system, or the distribution of
contexts or meaning, nor what the contexts or meanings actually are, and
therefore the argument applies at all levels of linguistic analysis.

A key assumption that is required is that speakers and listeners have the same
or very similar coding schemes and also the same ability to use contextual
information to constrain the possible meanings.

It is unclear how one might test this argument, since it is a mathematical
demonstration that |a|_ should exist; it does not make predictions about
language other than the presence of |a|_.

|A| and minimum effort
--------------------------------------------------------------------------------

In this section, the authors argue that ambiguity is a desirable property of a
linguistic systems because it potentially allows for ease of processing.

Ease of processing may be improved if linguistic form vary in ease of
processing, there are at least two meanings which are unlikely to occur in the
same context, and the cost of disambiguating is cheap. In this case, an
unambiguous system could be made more efficient by mapping the meanings onto
whichever of their corresponding linguistic forms was easiest to process.

Empirical evaluation of |a| and effort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section we empirically evaluate the prediction of the second argument
that |a|_ allows for re-use of efficient linguistics units by looking at
homophony_, polysemy_, and the |a|_ about meaning of different syllables, in
English, German, and Dutch.

Our basic approach is to measure the difficulty of words and syllables and see
if easier linguistic units are preferentially re-used in language.

We use three measures of linguistic difficulty for word and syllables:
length, frequency, and `phonotactic surprisal`_. [*]_ 

We measure re-use by measuring the number of possible meanings a word or
syllable has. [*]_

We then use several different techniques to analyze the influence of these
factors on |a|_.

Homophony
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Question:
    Are phonological forms reused as a function of difficulty?

:Prediction:
    Easier phonological forms should be reused more often than harder
    phonological forms, across languages.

:Experiment:
    - Word length was measured by syllables.

    - Word frequencies were taken from CELEX_ and were transformed to negative
      log probabilities.

    - `Phonotactic surprisal`_ was computed using a simple triphone language
      model. This measure was divided by word length to prevent it being
      collinear with length, and therefore can be interpreted as surprisal per
      phoneme, averaged over the entire word.

    - Number of homophones was taken from CELEX_.

:Observations:

    .. image:: ../../img/piantadosi_tily_gibson_2012_fig_1.png
       :width: 100%

:Results: Prediction confirmed. [*]_ [*]_


Polysemy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Question: 
    Are word forms reused as a function of difficulty?

:Predictions:
    Easier word forms should be reused more often than harder word forms, across
    part of speech. [*]_

:Experiment:
    - The length of a word form was measured as phonological length.

    - Frequency of a word form was computed as in the homophony analysis.

    - `Phonotactic surprisal`_ was computed as in the homophony analysis.

    - The number of word senses_ was taken from WordNet.

:Observations:

    .. image:: ../../img/piantadosi_tily_gibson_2012_fig_2.png
       :width: 100%

:Results: Prediction confirmed.

Syllables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Question:
    Are syllables reused as a function of difficulty?

:Prediction:
    Easier syllables should be reused more often than harder syllables, across
    languages.

:Experiment:
    - The length of a syllable was measured as the number of phones in its
      phonological transcription.

    - Syllable frequencies and phonotactic log probabilities were computed using
      the same procedures as the previous two sections.

    - Phonotactic surprisal?

    - Reuse was measured as the number of words a syllable appears in.

:Observations:

    .. image:: ../../img/piantadosi_tily_gibson_2012_fig_3.png
       :width: 100%

:Results:
    Syllables pattern similarly to words, except in the case of phonotactic
    predictability. [*]_

:Conclusion:
    Predictors of ease extend to syllable units, although not in the case of
    German syllable length.

General discussion
================================================================================

- We have presented two related arguments that show a well-designed
  `communication system`_ will be ambiguous_, when examined out of context_.

- We tested predictions of this theory, showing that words and syllables which
  are more efficient are preferentially re-used in language through ambiguity,
  allowing for greater ease overall. Our regressions on homophones, polysemous
  words, and syllables -- though similar -- are theoretically and statistically
  independent. We therefore interpret positive results in each as strong
  evidence for the view that ambiguity exists for reasons of communicative
  efficiency. [*]_

- Our analyses used regressions, which means that coefficients can be
  interpreted as the effect of one covariate while controlling for others. This
  is important because if one finds a relationship between, say, ambiguity_, and
  length, it is important to show that this is not due to correlation between
  ambiguity and frequency, and frequency and length.
  
- We found large, independent and statistically-significant effects of
  phonotactic probability, length, and frequency. This provides that these
  factors each influence the degree of ambiguity_, rather than simple beying
  correlated with a single underlying. This verifies a prediction of the
  minimal-effort explanation for ambiguity: each factor we tested which we
  predicted to increase each of processing, also increase ambiguity.

Conclusion
================================================================================

- We have provided several kinds of evidence for the view that ambiguity results
  from a pressure for efficient communication.

- We argued that any efficient communication system will necessarily be
  ambiguous_ when context_ is informative about meaning. The units of an
  efficient communication system will not redundantly specify information
  provided by the context; when examined out of context, these units will appear
  not to completely disambiguate meaning.

- We have also argued that ambiguity_ allows efficient linguistic units to be
  preferentially re-used, decreasing the overall effort need to use a linguistic
  system.

- We test predictions of this theory by showing that ambiguity_ allows re-use of
  the easiest linguistic units. These results are hard to explain with anything
  other than a theory based on efficient communication: what theory would posit
  that ambiguity should preferentially be found in these linguistic units, but
  not that it results for efficiency? Our results argue for a rational
  explanation of ambiguity and demonstrate that ambiguity is not mysterious when
  language is considered as a cognitive system designed in part for
  communication.

Footnotes
================================================================================

.. [*]
    Both frequency and length are know to influence on-line language processing
    with longer and lower-frequency words taking longer to process.

    Intuitively, words that are re-used through ambiguity should have very low
    `phonotactic surprisal`_ in order to decrease cognitive and articulatory
    difficulty.

    While we only examined these three predictors, our theory predicts that any
    other measure which increases processing ease should also increase
    ambiguity.

.. [*]
    Ideally, one would measure |a|_ using the `entropy`_ over meanings for a
    given linguistic form. Unfortunately `entropy`_ is difficult to estimate
    without statistical bias, which leads to results which are difficult to
    interpret.

.. [*]
    This is somewhat difficult to interpret because |pfs| with more meaning
    should be seen more simply because they can be used in more situations.
    However, that interpretation predicts a linear relationship between number
    of meanings and frequency-- a word ``k`` meanings should be used ``k`` more
    times than word with 1 meaning. The figure demonstrates a linear
    relationship between number and log frequency, corresponding to a
    super-linear relationship between number of homophones. We therefore argue
    such a relationship likely results from the ease of processing more frequent
    word-forms, rather than merely the fact that phonological forms with more
    meanings can be used in more situations.

.. [*]
    This effect on phontactic surprise tends to level out, showing no
    differences between the highest surprisal words or slight increases. These
    effects may result from poorer estimation in the highest `phonotactic
    surprisal`_ words, which have the lowest frequency phonotactic trigrams.

.. [*]
    We chose to look at part of speech categories separately to ensure the
    finding are not driven by a single part of speech category and also to check
    that these effects go beyond effects of homophony.

.. [*]
    The syllables with lowest `phonotactic surprisal`_ do appear in the most
    word; however, very high `phonotactic surprisal`_ syllables also tend to
    appear in many words.
    
    We believe this trend is an artifact of our `phonotactic surprisal`_ model,
    which has increased estimation error for the high `phonotactic surprisal`_.
    This interpretation is supported by the absence of a quadratic trend using a
    two-phone model.
    
    Alternatively, it may be the case that other articulatory effects are
    present at the syllable level and that this trend results from other kinds
    of articulatory constraints (which exert a stronger influence).

.. [*]
    We note, however, that the languages tested are historically-related,
    meaning that further work will be needed to establish stronger typological
    generalizations.

Glossary
================================================================================

.. _context:

Context
    discourse context, world context, world knowledge, syntactic information,
    etc.

.. _functionalist theories:

Functionalist theory
    A theory which attempts to explain properties of linguistics systems in
    terms of `communicative pressures`_.

    See: `functionalism`

.. _communicative pressure:
.. _communicative pressures:

Communicative pressure
    Any cause that reduces communicative success in a proportion of a
    population, potentially exerts communicative pressure.


.. _CELEX:

CELEX
    A particular lexical database.

.. _phonotactic surprisal:

Phonotactic surprisal
    Phonotactic surprisal refers to how phonetically probable a word is, given
    all other words in the language (measurable using a Markov model).

    A word with low phonotactic surprisal may be called "phonotactically
    well-formed".

.. _ambiguous: ../encyclopedia/Ambiguity_.html
.. _ambiguity: ../encyclopedia/Ambiguity_.html
.. _coding theory: ../encyclopedia/Coding_theory.html
.. _cognition: ../encyclopedia/Cognition_\\(journal\\).html
.. _communication: ../encyclopedia/Communication.html
.. _communication system: ../encyclopedia/Communication_system.html
.. _communication systems: ../encyclopedia/Communication_system.html
.. _entropy: ../encyclopedia/Entropy.html
.. _homophony: ../encyclopedia/Homophony.html
.. _homophones: ../encyclopedia/Homophony.html
.. _information: ../encyclopedia/Information.html
.. _information theory: ../encyclopedia/Information_theory.html
.. _information-theoretic: ../encyclopedia/Information_theory.html
.. _language processing: ../encyclopedia/Language_processing.html
.. _lemmas: ../encyclopedia/Lemma.html
.. _natural language: ../encyclopedia/Natural_language.html
.. _sense: ../encyclopedia/Word_sense.html
.. _senses: sense_

.. |A| replace:: Ambiguity
.. |a| replace:: ambiguity
.. _a: ambiguity_
.. |I| replace:: Information
.. |i| replace:: information
.. _i: information_
.. |ecs| replace:: efficient `communication system`_
.. |ecss| replace:: efficient `communication systems`_
.. |pf| replace:: phonological form
.. |pfs| replace:: phonological forms
