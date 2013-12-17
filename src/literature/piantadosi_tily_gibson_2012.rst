
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

    We argue that the generality of our results explains the pervasiveness of
    |a|_ in language, and shows how |a|_ likely results from
    ubiquitous pressure for *efficient communication*.

    The authors argue that:
    
    - If context_ provides |i|_ about meaning, then an |ecs| will be
      ambiguous_.

    - |a|_ allows for greater ease of `language processing`_ by
      permitting efficient linguistic units to be re-used.

    The authors test predictions of this theory in English, German, and Dutch.

.. todo:  what does efficient mean here?
.. todo:  what does meaning mean here?

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

In this section, we present two closely related arguments that |a|_ allows for
more |ecss|.

Both assume that:

1. |I|_ is typically present to resolve ambiguities

2. Using this |i|_ is relatively "cheap"

The first argument looked at |a|_ from the perspective of `coding theory`_,
arguing that when context is informative, any good `communication system` will
leave out |i|_ already in the context. It is unclear how one might test this
argument, since it is a mathematical demonstration that |a|_ should exist; it
does not make predictions about language other than the presence of |a|_.

The second argument assumed that codewords differ in their difficulty, and
argued that as long as there are some ambiguities that context can resolve,
|ecss| will use |a|_ to make communication easier. This argument directly
predicts that linguistic units which require "less effort" should be more
ambiguous.

We do not view these arguments as distinct alternatives, but rather as
complementary ways of understanding how |a|_ is useful.

|A| in general communication
--------------------------------------------------------------------------------

In this section we motivate an `information-theoretic`_ view of |a|_.

Intuitively, a linguistic form is ambiguous if it can map to more than one
possible meaning. For instance, the word "run" is ambiguous because it can refer
to a large number of possible meaning, including a run in a pantyhose, a run in
baseball, a jog, to run, a stretch of consecutive events, etc.

One can show the optimally |ecs| should look ambiguous by formalizing a notion
of uncertainty about meaning, as long as context is informative about meaning.

We quantify the uncertainty that listeners would have about intended meaning by
using `Shannon entropy`. `Shannon entropy` measures the amount of |i|_
required on average to disambiguate which meaning in M is intended.

`Shannon entropy` is dependent on `context`_. Actual `language use` takes place
with reference to the world and linguistic context. For instance, knowing that
the speaker is playing baseball, for instance, will change the expectations of
what meaning of "run" is intended. When the context is known and informative, it
necessarily decreases `entropy`_.

An optimally |ecs| will not convey unnecessary |i|_. An |ecs| will never be able
to disambiguate language out of context. This means that when the individual
units of an efficient communication_system

|A| and minimum effort
--------------------------------------------------------------------------------

Empirical evaluation of |a| and effort
================================================================================

In this section we empirically evaluate the prediction that |a|_ allows for
re-use of efficient linguistics units by looking at homophony, polysemy, and the
|a|_ about meaning of different syllables, in English, German, and Dutch.

Our basic approach is to measure properties of words and syllables and see if
easier linguistic units are preferentially re-used in language.

We investigate the influence of three simple and easy-to-measure properties of
words:

1. Length

2. Frequency

3. `Phonotactic probability`

We use several different techniques to analyze the influence on these factors on
|a|_.

Ideally, one would measure |a|_ using the `entropy`_ over meanings for a
given linguistic form. Unfortunately `entropy`_ is difficult to estimate without
statistical bias, which leads to results which are difficult to interpret.

For this reason, we primarily present count data: for each linguistic unit, we
count the number of possible meanings it has in order to measure its degree of
|a|_.

Homophony
--------------------------------------------------------------------------------

A homophone is a word that is pronounced the same as another word but differs in
meaning. The words may be spelled the same, such as "rose" (flower) and "rose"
(past tense of "rise"), or differently, such as "to", "two", and "too". The
words may different only in part of speech, such as "experiment" (the noun) and
"experiment" (verb).

:Question: 

:Prediction: Phonological forms which are high-frequency, phonotactically
             well-formed, and short will map to many different word `lemmas`_.

:Experiment: Examine homophones from CELEX_.

             - Word length was measured by number of syllables.

             - Word frequencies were taken from CELEX_.

             - Phonotactic surprisal?

:Observations:

    .. image:: ../../img/piantadosi_tily_gibson_2012_fig_1.png
       :width: 100%

:Results:
    Every factor predicted to increase ease of use also increases the number of
    meanings assigned to phonological forms.

    - Fig. 1a shows that shorter |pfs| are assigned more meanings across all
      languages.

    - Fig. 1b shows that higher frequency (lower negative log probability)
      |pfs| tend to be mapped to many more word meanings than lower frequency
      |pfs|, across all languages. [*]_

    - Fig. 1c shows that as average `phonotactic surprisal` per phoneme
      increases, words also tend to have fewer meanings. This effect tends to
      level out, showing no differences between the highest surprisal words or
      slight increases. These effects may result from poorer estimation in the
      highest phonotactic surprisal words, which have the lowest frequency
      phonotactic trigrams.

:Conclusions:


Polysemy
--------------------------------------------------------------------------------

Here we consider similar predictions about the number of word senses each word
has as a function of the word's length.

:Question:

:Prediction:

:Experiment:
    Look at words forms found in the English version of WordNet and CELEX_.

    We chose to look at part of speech categories separately to ensure the
    finding are not driven by a single part of speech category and also to check
    that these effects go beyond effects of homophony.

    For each word and part of speech, we computed the number of senses using
    WordNet.

    For each word, CELEX_ was used to find the phonological length of each word,
    as well as its phonotactic probability and frequency (negative log
    probability) using the same methods as the previous section.

:Observations:

    .. image:: ../../img/piantadosi_tily_gibson_2012_fig_2.png
       :width: 100%

.. todo: I'm not sure I understand how this differs.

:Results:
    Fig. 2 shows predicted effects in each part of speech, and for each measure.
    This reveals the predicted trends in nearly the full range of measures. For
    the majority of bins across the range of variables, factors which should
    increase each also increase the number of word senses.

    - Longer words have fewer senses.

    - Lower frequency words have fewer senses.

    - Higher phonotactic surprisal have fewer senses.

    We argue that frequent word -like phonotactically well-formed and short
    words - have more meanings because they are easier to process. In contrast,
    Zipf argued that frequent words have more meanings because such a
    relationship optimally balances concerns of speakers and listeners.

Syllables
--------------------------------------------------------------------------------

Given just one syllable, one will have some incomplete information about what
word the speaker is attempting communicate. In this sense, individual syllables
are ambiguous about meaning, and it is only when they are heard in the context
of other syllables, words, and discourse situations that they can be used to
unambiguously communicate meaning.


In general, this syllable analysis is interesting in part because syllables are
not generally taken to be ambiguous in the same way that words or sentences are.
Syllables are not, on their own, meaningful units of language. However,
syllables are informative about intended meanings. In this case, we take the
intended meaning to be the word lemma which being communicated.

:Question:

:Prediction:
    Easier syllables should convey less information than about meaning than
    harder syllables. In this case, we take syllables to be informative about
    the words that they appear in.

:Experiment:

    We analyzed syllables in words from CELEX_.
    
    In each language, we computed the number of words each syllable appears in.

    Syllable frequencies and phonotactic log probabilities were computed using
    the same procedures as the previous two sections.

    - The length of a syllable was measured as the number of phones in its
      phonological transcription.

    - Phonotactic log probability was computed using a trigram model, the
      negative log probably of each syllable was computed according to its total
      token count in CELEX_.

    - Phonotactic surprisal?

:Observations:

    .. image:: ../../img/piantadosi_tily_gibson_2012_fig_3.png
       :width: 100%

:Results:
    Syllables pattern similarly to words, except in the case of phonotactic
    predictability.

    - Increasing length decreases the numbers a syllable appears in.

    - Higher negative log probability (lower frequency) decreases the number of
      words.

    - Increasing phonotactic surprisal tends to decrease the number of words.
      [*]_

:Conclusion:
    Predictors of ease extend to syllable units, although not in the case of
    German syllable length.

    It is likely that at the syllable level, other kinds of constraints such as
    articulation exert a stronger influence on the design of lexical systems.

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

This is not say there is no cost to ambiguity.

1. Comprehends must actively use context_ to disambiguate meaning. However,
   considerable evidence from `language processing`_ indicates that
   comprehenders are able to quickly use contextual information in the form
   of discourse context, local linguistic context, or more global world
   knowledge in disambiguating language. These systems may be useful for normal
   language comprehension, as they are for disambiguating language.

   `Levinson (2000)` has argued explicitly that speaker articulation, not
   hearer inference, is the principal bottleneck in human language. Inference is
   "cognitively cheap": therefore, normal human communication requires the
   comprehender to make continual inferences about speaker intention, and does
   not require the speaker to fully articulate every shade of meaning.

2. A more substantial cost for ambiguity_ arises when inference fails, causing
   actual confusion. However, some researchers have claimed that genuine
   ambiguity_ is vanishingly rare. Indeed, polysemy and homophony appear to be
   soo well-disambiguated by context that we often consciously notice genuine
   ambiguity as humorous. Therefore, we believe the potential for
   miscommunication is rare enough that the potential for miscommunication is
   rare enough relative to the degree of ambiguity that is reasonable to ignore
   this communicative cost, at least an approximation.

Language users do not appear to go to great lengths to avoid linguistic
ambiguities, despite actively avoiding conceptual ambiguities_. Ferreira, Slevc,
and Rogers (2005) found that experimental participants chose to produce
descriptions of objects that avoided conceptual ambiguities, such as saying
"small bat" rather than just "bat" when a large bat was also present. However,
speakers much less often went to similar lengths to avoid purely linguistic
ambiguities (such as "baseball bat" when an animal bat was also present).

These findings suggest that ambiguity is not enough of a problem to real-world
communication that speakers would make much effort to avoid it. This may well be
because actual language in context provides other information that resolves the
ambiguities most of the time. Such information could be prosodic, or it may be
given by context, meaning that in real language use there is rarely much need to
actively choose linguistic forms which are unambiguous in isolation.

Our arguments are closely related to `Uniform Information Density` (UID) which
holds that speakers are more likely to choose words and structures which
maintain a roughly constant rate of information transmission, UID and closely
related theories have been used to explain phenomena such as discourse-level
predictability and reduction.

An ambiguous_ linguistic form conveys less information about its intended
meaning than unambiguous linguistic form. Therefore, to keep the entropy rate
constant, one might choose ambiguous linguistic units which are *less*
surprising in other way which match our findings: this strategy would result in
ambiguous words being more phonotactically predictable, higher-frequency (less
surprising), and shorter (to maintain constant information-per-ptime). However,
we argue that the results presented above are not merely a consequence of UID,
though they rely on similar ideas and theoretical basis. Most importantly, UID
does not directly predict that efficient language *should* be ambiguous_, since
there are other ways to construct a linguistic system with constant information
rate.

Conclusion
================================================================================

We have provided several kinds of evidence for the view that ambiguity results
from a pressure for efficient communication.

We argued that any efficient communication system will necessarily be ambigious
when context is informative about meaning. The units of an efficient
communication system will not redundantly specify information provided by the
context; when examined out of context, these units will appear not to completely
disambiguate meaning.

We have also argued that ambiguity allows efficient linguistic units to be
preferentially re-used, decreasing the overall effort need to use a linguistic
system.

We test predictions of this theory by showing that ambiguity_ allows re-use of
the easiest linguistic units.

Footnotes
================================================================================

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
    The syllables with lowest phonotactic surprisal do appear in the most word;
    however, very high phonotactic surprisal syllables also tend to appear in
    many words. We believe this trend is an artifact of our phonotactic
    surprisal model, which has increased estimation error for the high
    phonotactic surprisal. This interpretation is supported by the absence of a
    quadratic trend using a two-phone model. Alternatively, it may be the case
    that other articulatory effects are present at the syllable level and that
    this trend results from other kinds of articulatory constraints.

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

.. _sense:

Sense
    Word senses separate related meanings, such as those in "John runs to the
    store", "she runs her finger through her hair", and "the train runers
    between Boston and New York".

.. _CELEX:

CELEX
    A lexical database.

.. _ambiguous: ../encyclopedia/Ambiguity_.html
.. _ambiguity: ../encyclopedia/Ambiguity_.html
.. _coding theory: ../encyclopedia/Coding_theory.html
.. _cognition: ../encyclopedia/Cognition_\\(journal\\).html
.. _communication: ../encyclopedia/Communication.html
.. _communication system: ../encyclopedia/Communication_system.html
.. _communication systems: ../encyclopedia/Communication_system.html
.. _entropy: ../encyclopedia/Entropy.html
.. _information: ../encyclopedia/Information.html
.. _information theory: ../encyclopedia/Information_theory.html
.. _information-theoretic: ../encyclopedia/Information_theory.html
.. _language processing: ../encyclopedia/Language_processing.html
.. _lemmas: ../encyclopedia/Lemma.html
.. _natural language: ../encyclopedia/Natural_language.html
