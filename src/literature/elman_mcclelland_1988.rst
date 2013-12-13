.. include:: ../shorthand/psycholinguistics.rst

================================================================================
Cognitive penetration of the |ms| of |PER|
================================================================================
--------------------------------------------------------------------------------
|cfc| of Lexically Restored Phonemes
--------------------------------------------------------------------------------


:Authors: Jeffrey L. Elman; James L. McClelland
:Date: 1988
:Journal: Journal of Memory and Language 27
:Pages: 143-165 (23)

:Abstract:
    An important question in `language processing`_ is whether |hl| |ps| are
    able to interact directly with |ll| |ps|, as assumed by interactive
    models such as the `TRACE`_ model of |sp|_.

    The issue is addressed in the present study by examining whether putative
    |ter| phenomena can trigger the operation of |tra| |ps| at |ll|.

    The |tra| |p| involved the |pc|_ for the |ci|_ of one speech sound on
    another.

    `TRACE`_ predicts that |pc|_ can be triggered by illusory phonemes which are
    perceived as a result of |td|, lexical influences.

.. contents::

Introduction
================================================================================
:Pages: 143-144

What is the degree to which cognitive |ps| are modular?

The issue has been of great interest and controversy and a difficult one to
decide because there is considerable overlap in the predictions made by the two
accounts: the `interactive view`_ and the `modular view`_. [#]_ [#]_

In this paper we:

#. Describe `TRACE`_.

#. Describe `a technique` which provides a rigorous test of the existence of
   true |td| interactions in processing.

#. Using this technique, we find that |hl| contextual factors can trigger
   compensatory |ps| that are basic to |sp|_.
   
#. These findings demonstrate that more effect of |hl| knowledge of |PER| is
   possible than has been thought.


How can |ci|_ be used to test the assumption of `TRACE`_ that |hl| do indeed
feed activation back to |ll|.?

Experiment 1
================================================================================

Method
--------------------------------------------------------------------------------

Results
--------------------------------------------------------------------------------

Discussion
--------------------------------------------------------------------------------

Experiment 2
================================================================================

Method
--------------------------------------------------------------------------------

Results
--------------------------------------------------------------------------------

Discussion
--------------------------------------------------------------------------------

Experiment 3
================================================================================

Method
--------------------------------------------------------------------------------

Results
--------------------------------------------------------------------------------

Discussion
--------------------------------------------------------------------------------

Experiment 4
================================================================================

Method
--------------------------------------------------------------------------------

Results
--------------------------------------------------------------------------------

Discussion
--------------------------------------------------------------------------------

General discussion
================================================================================

Footnotes
================================================================================

.. [#]

    1. `Language comprehension` appears to involve the parallel processing of
       information at the semantic, syntactic, and phonological levels.

    2. This processing seems to be not only parallel but interactive; processing
       at each level appears to influence, and be influenced by, processing at
       other levels.

    3. Lexical information appears to play an active role in the |PER| of
       phonemes.

    4. The perceptual boundary between phonemes can be shifted as a function of
       lexical content.

.. [#]

    1. ?

    2. It is plausible that frequent sequences of events would result in stronger
       intramodule associations for these sequences.

.. [*]
    The answer will be relevant when we consider how one might test the
    assumption that influences really do feed back down from higher levels
    within the speech processing system.

Glossary
================================================================================

.. _language processing:

Language processing
    How the brain creates and understands language.

.. _TRACE:

TRACE model of speech |PER|
    TRACE is a connectionist model of |sp|, proposed by McClelland and Elman in
    1986.

    TRACE was made into a working computer program for running perceptual
    simulations.

Processing in `TRACE`_
    Processing is carried out in a network consisting of a large number of
    interconnected elements called `units`.

    Different classes of units represent acoustic/phonetic features, phonemes,
    and words:

    - At the |fl|, there is a `unit`_ for each feature at each of a large number
      of time slices relative to the onset of an utterance.

    - At the |pl|, there is a `unit`_ for each phoneme in each time slice.

    - At the |wl|, there is a `unit`_ for each word, starting in each time
      slice.

    Each unit has an activation value which is taken to be translatable into an
    estimate of the strength of the hypothesis that the concept the unit
    represents is present in the signal in the time slice or slices that the
    unit covers.

    Thus the pattern of activation over these units in the network is the
    system's representation of the content of the utterance it is currently
    processing.

    Activations of units are continuously updated in TRACE, based on activations
    of units that project to them.

    The activations of units are determined by a simple two-part activation
    function. When a unit's activation exceeds a certain threshold value, it
    excites or inhibits other units in a way which reflects the mutual
    consistency or inconsistency of the concepts represented by each unit.

    1. Adding together all of the inputs to the unit to obtain what is called
       its net input.

    2. The net input is then used to update the activation of the unit.

.. _ce:

Context effects

|ce| in `TRACE`_

    How does `TRACE`_ account for |ce|_ on phoneme identification? [*]_

    .. image:: ../img/elman_mcclelland_1988_fig_1.png

    Like other models, `TRACE`_ requires a |rp| to translate activations of
    units into overt responses. For now, it is sufficient to note that the red
    assumptions of `TRACE`_ and the interactive-activation model allow the
    models to approximate the quantitative predictions of models in which
    information from lexical and featural inputs is integrated in a
    postperceptual decision |m| of the kind described by Massaro.

    Two feature of operation that are relevant to the use of testing the claim,
    inherent in the model, that there is feedback from the |wl| to the
    |pl|:

    1. |td| input influences processing by combining additively with |bu|
       input in determining the total, or net input, to the unit.

    2. The |td| information |p| influences the activation of a phoneme unit
       takes time.

    We these two points in mind, we can evaluate two different sorts of evidence
    that been offered for assessing whether an effect is truly |td| or not.

    1. The first is based on signal detection theory... Thus far we have seen
       that `TRACE`_ is consistent with evidence that lexical content often
       operates like other cues to phoneme identity, producing an affect which
       can show up as a bias effect in signal detection analysis.

    2. Another line of argument that has been offered in support of a
       postperceptual, response-stage view of context effects in phoneme |PER|
       is the fact that they often take time to build up.

    We seen then that previous evidence taken in support of models in which the
    |ce|_ operate on decision |m| does not in fact constitute evidence that
    is inconsistent with the `TRACE`_.

|cfc| in `TRACE`_
    `TRACE`_ accounts for |ci|_ on phoneme identification by allowing active
    phoneme units to modulate the connections between the |fl| and |pl| in an
    adjacent time slices in just such a way as to |pc|_ for their |ci|_.

    `TRACE`_ assumes that these |ci|_ occur in basic |ms| of |sp|_.

    .. nonessential:
   
    This assumption is generally quite shared.  |ci|_ are ubiquitous, and it has
    been suggested that one of the essential functions of the |sp|_ |ms| is to
    |pc|_ for |ci|_ and recover the underling phonetic code.

Triggering |ter| effects via |tra| influences
    In the past, we have studied the behavior of `TRACE`_ by always testing the
    model under conditions where the |cfc|_ was triggered by the unambiguous
    presence of some phoneme which was known to have |ci| on adjacent sounds.
    However, in `TRACE`_, phonemes receive input from the |pl| and the |wl|.
    Thus, it is possible that activations at the |pl| might trigger |cfc|_
    whether they are determined purely by |bu| input or some mix of |bu| and
    |td| influences.

    It is this possibility within `TRACE`_ for |td| processing to have indirect
    effects on |ll| which suggests a way to answer the question: Are
    |td| effects real or only apparent?

    The logic is to test for the presence of a |td| effect not by seeing
    whether a |hl| can alter an overt decision about a |ll|, but, rather, by
    seeing whether the |hl| can actually reach into the |ll| and affect some
    |tra| |p| - in this case, |cfc|.

    The following two simulations from `TRACE` illustrate the model's prediction
    that such effects will occur.


.. _unit:

.. _sp:
.. _speech |PER|:

Speech |PER|:
    The process by which the sounds of language are heard, interpreted, and
    understood.

.. _modular view:
.. _autonomous view:
.. _autonomous model:

Modular view (or autonomous view)
    The view that cognitive processing of |PER| is essentially modular in
    nature.

    Claims:

    - Processing is autonomous.

    - |bu| |ps| make their output available to |hl| |ps|
      
    - |hl| |ps| do not affect |bu| |ps|

.. _interactive view:

Interactive view:
    The view that the cognitive processing of |PER| permits free flow of
    information.

    Claims:

    - |td| as well as |bu| interactions are possible.

Lexically restore phoneme
