.. include:: index

================================================================================
Models for Reading Letters and Words
================================================================================

:Authors: Dominic W. Massaro

:Date: 1998

:Work: An Invitation to Cognitive Science - 2nd Edition

:Pages: 302-364 (63)

:Abstract:
    The goal of this chapter is to illustrate how developing and testing
    `computational models`_ can inform us about the psychological processes
    involved in perceiving, recognizing, and categorizing the world.

    To simplify the discussion, we focus on the question of how we perceive
    letters and words.

    This chapter promotes the value of computational models in the enterprise of
    understanding how humans accomplish feats such as pattern recognition.

    In the first few sections, Massaro reviews `pattern recognition`_,
    `computational models`_, and the two main approaches to `pattern
    recognition`_: `template matching`_ and `feature analysis`_.

    Then Massaro suggests that we test a core assumption of feature analysis:
    namely, whether feature detectors report discrete or continuous responses.

    To do this, he proposes an experiment using a rating task, where subjects
    are presented ambiguous letters on a ``c``-``e`` continuum and are asked to
    indicate where each test letter feel on a nine-point scale between ``c`` and
    ``e``. Massaro reviews the predictions of the discrete feature model and the
    continuous feature model, and then presents results that indicate the
    continuous feature model accurately predicts responses.

    In what follows, I show how both discrete and continuous feature recognition
    theories are consistent with the mean rating results shown in figure 7. Then
    we will see how extending the database and computational modeling can
    distinguish between the two alternatives.

.. contents::

.. sectnum::

Introduction
================================================================================
:Pages: 302-304 (2)

- When faced with a written word we seem to have no choice but to read it.
  (Stroop effect - 1935). Reading words is such an overlearned skill, it is not
  easily put on hold. Achieving this level of reading skill takes time. Reading
  is a remarkably complex skill.
  
- In addition to being experts in letter recognition, we are especially good at
  recognizing them when they spell words. Our knowledge of spelling and the
  context provided by other letters of a word help us recognize individual
  letters within words.

  .. image:: ../img/Massaro_1998_fig_1.png
     :align: center

Letter recognition
================================================================================
:Pages: 310-319 (10)

It has been hypothesized that feature detectors are binary: either a feature is
present or not. This assumption should be put to the test because it is can
central to how we think about feature. The alternative is that feature detector
detectors are continuous.

Fuzzy letters and continuous rating judgments
--------------------------------------------------------------------------------

Most studies of letter recognition do not address the assumption of discrete
features.

To test this idea, we want the subject to make errors.

One way to induce errors is to show a letter for a short duration followed by a
`visual mask`_. However, results of these experiment do not easily test whether
perception of features is continuous or discrete because the results are
consistent with either hypothesis.

----

Another approach is to crate ambiguous_ letters by varying the degree to which a
feature is present. For many pairs of letters, we can create ambiguous letters
that resemble both letters. For example, the lowercase letters ``c`` and ``e``
appear to differ in the presence of horizontal line feature for ``e`` but not
``c``. How readers process these ambiguous letters should help us decide whether
this feature is perceived discretely or continuously.

.. image:: ../img/Massaro_1998_fig_6.png
   :align: center
   :width: 50 %

In an experiment addressing the issue, each of the six letters shown in figure
8.6 was presented seventy times in random order, and the subject categorized
each presentation as an ``e`` or a ``c``. The results show that letters on the
``c`` side of the continuum were consistently categorized as ``c`` and letters
on the ``e`` side of the continuum were consistently categorized as ``e``.

.. image:: ../img/Massaro_1998_fig_7.png
   :align: center
   :width: 50 %

From this, it might be concluded that the horizontal line feature is perceived
discretely. However, this conclusion would not be justified because the
categorization task does not permit subjects to give a direct report of what
they saw.

.. todo: I do not understand why in figure 8.7 the probability go from 0 to 1.
   Surely, it would be slightly unequal?

----

Another possible task is to ask subjects where a present letters falls on a
continuous scale between ``c`` and ``e``. [*]_ The subject provided seventy
ratings for each of the six test letters.

.. list-table:: Letter-rating task
    :header-rows: 1
    :widths: 10 45 45

    - - 

      - Discrete feature model

      - Continuous feature model

    - - Assumptions

      - - Subjects recognize each stimulus presentation as ``c`` or ``e`` and
          nothing in between.

        - Perception_ is probabilistic. Probability is influenced by
          resemblance.

        - Predicts subjects would choose ratings toward the ``c`` end of the
          scale for the perception_ of ``c`` and vice-versa for ``e``.

      - - Subjects perceive the degree to which a letter resembles each
          alternative.

        - Expect a distribution of rating judgments due to random variability in
          perceptual memory or response systems.

        - Predicts a systematic and continuous change across the six test
          letters.

    - - Hypothetical distribution of rating responses

      - |Figure8|

      - |Figure10|

    - - Results

      - |Figure11|

      - |Figure12|

.. list-table:: Meaning rating responses
    :header-rows: 1

    - - Hypothetical

      - Observed

    - - |Figure9|

      - |Figure13|


Experimental test
--------------------------------------------------------------------------------

We can analyze the observed distributions of the rating responses.

As can be seen, the distributions of the observed ratings are unambiguously
characterized by the having a single peak as predicted by the continuous model.

Consider the third stimulus level on the ``c``-``e`` continuum. Figure 11 shows
that the subject consistently rated the stimulus as a four along the ``c``-``e``
continuum. As shown in figure 8.8, the discrete model would predict that the
subject should have rated some of the time toward the ``c`` end and some of the
time toward the ``e`` end of the ``c``-``e`` rating continuum.

In order to determine whether the observed distributions of the ratings were
best fit by the continuous or the discrete model, the two models were formulated
to predict the distributions of ratings. That is, instead of using the
hypothetical distributions, Massaro found the distributions for each model that
would do the best job of predicting the observed rating judgments.

The continuous model does a much better job of fitting the observed
distributions of ratings. We conclude that letter features are perceived
continuously rather than discretely.

**What is important for our purposes is that his conclusion required
computational modeling to provided a definitive test of a long standing
assumption about the processing of letter features.**

Multifactor experiments
================================================================================
:Pages: 319-321 (3)

In the ``c``-``e`` study, we varied just a single feature, and although we
described it as a test of whether features are perceived as discrete or
continuous, the results are consistent with both feature and template theories;
the results tell us only that subjects responded to the information in the task
as if it were continuous.

If we design our experiment to be somewhat more realistic, we should
systematically vary two or more features independently to try to isolate the
influence of each feature. Furthermore, we should also vary the degree to which
each feature is is present.

Two categories, ``G`` and ``Q`` were chose as the alternatives in a letter
processing task.

.. image:: ../img/Massaro_1998_fig_14.png
   :align: center
   :width: 50 %

From a featural perspective:

1. ``Q`` has a closed oval and ``G`` has an open oval.

2. ``Q`` has an oblique line and ``G`` has a horizontal line.

We can create novel test letters by varying the degree to which each feature
resembles its normal appearance in the letters:

In a factorial experimental design with two factors, each level of one factor is
combined with every level of the factor.

`Massaro and Harry (1986)` carried out this experiment. In the categorization
task, the 49 test letter were presented 12 times for 400 ms in random order to
each of 9 subjects.

Models of recognition
================================================================================
:Pages: 321-338 (18)

Template model
--------------------------------------------------------------------------------

A template account of this task appears to have very little predictive power.

Each of the forty-nine test stimuli is a new holistic event and recognition
cannot be predicted on the basis of the two separate properties, gap size and
angle line.

This version of the template theory predicts a consistent division of the
forty-nine letters into two sets, but this predictions conflicts with the
variability of human nature; we can expect that a stimulus will not always
receive the same categorization response.

One place where variability might occur in a template model is in the decision
operations. For example, if decisions are based on a goodness-of-match rule
(RGR). [*]_

However, another aspect of these predictions is not realistic. Given that the
response probability is still based on the objective overlap between the
stimulus and the template, the model must make the same prediction for each
subject, but observations confirm that subjects differ from one another. (Which
makes sense, given that there is no reason for each subject's template to be the
same.) Given different templates, subjects should categorize stimuli
differently. Thus, any reasonable template model cannot be based on objective
overlap that can be measured directly in the stimuli; it must assume subjective
overlap that will be unique for each subject. In this case, each test letter
require independent estimates of the amount of subjective overlap with the
templates for each subject. Thus, the template model can only predict the
categorization probably for a test letter by estimating a subjective overlap
value for that test letter. Therefore, we cannot predict performance on the test
letters without first measuring how subjects respond to each of the 49 stimuli.
With this stipulation, we are left without a testable template model for the
``G``-``Q`` task.

.. image:: ../img/Massaro_1998_fig_16.png
   :align: center
   :width: 50%

Discrete feature model
--------------------------------------------------------------------------------

Although our experiment cannot test template models, it is ideal for testing
feature models.

Why make an effort to test such a model when the idea of discrete featured was
already falsified in the ``c``-``e`` study? Several justifications:

1. It is important to know if conclusions reached in the single-factor
   ``c``-``e`` study generalize to a two-factor ``G``-``Q`` study.

2. A combining or integration process might occur in the two-factor study that
   is not needed in the single-factor ``c``-``e`` study, and the addition of an
   integration process to combine information about two or more features might
   limit the perceiver to only discrete information about each feature.

3. We will see that more complex experimental situation allows us to derive a
   more complex discrete feature model that warrants empirical test because the
   more complex model might give accurate predictions even though a simpler
   version has already been falsified.

With just a single feature we might postulate two psychological processes:
evaluation and decision. For example, in the ``c``-``e`` recognition task
described above, the horizontal line feature must be evaluated and then a
categorization or rating decision must be made.

But, given multiple features, such as in the ``G``-``Q`` recognition task just
described, there is possibility that an additional integration operation occurs
after evaluation but before decision. This integration operation combines or
integrates several features or sources of information that have been evaluated
before a decision is made.

.. image:: ../img/Massaro_1998_fig_17.png
   :align: center

1. Evaluation: Evaluate the stimulus to determine the values of the features;
   which features are present and which are absent. Evaluation is the analysis
   of each source of information by the processing system. It can be thought of
   as the transformation of the physical value of each source into a
   psychological value. (In the ``Q``-``Q`` task, for example, evaluation would
   give separate representations of the gap size and line angle components of
   the test letter.)

2. Feature integration: Compare each of the prototypes to the stimulus feature,
   and output a measure of how much each prototype matches the stimulus.
   Integration is defined as a combination of the information made available by
   the evaluation process.

3. Decision: Select a response based on the outcome of integration. The decision
   operation might simply select the prototype or category with the best
   goodness of match. Decision converts the outcome of integration into a
   response.

The three operations between presentation of a pattern and its categorization as
can be formalized mathematically.

.. image:: ../img/Massaro_1998_table_1.png
   :align: center

Free parameters and their estimation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we describe how values for these variables are determined. This involves
the concept of free parameters and their estimation.

In terms of the DFM, we do not the know ``p_i`` and ``q_j`` values because we
cannot state ahead of time how changes in the letter features will change these
probability values. However, the DFM makes some strong predictions that allow it
to be quantitatively tested.

Assumption:

- Independence: In the DFM model, the probability of classifying a particular
  feature depends on the physical characteristics of the feature, but not on the
  other features.
  
Without this assumption, the DFM would be essentially untestable.

With the independence assumption, we can see that there can be a unique value of
``p_i`` for each of the seven levels of gap size that is unaffected by line
angle. Similar for ``q_i``.

We do not know what these values are, and we must use the results given by a
subject to find them. 

Most computational or quantitative models have a set of free parameters. A free
parameter in a model is a variable that cannot be exactly predicted in advance.
The actual performance of a subject is used to set the value of the variable.

Predictions of behavior cannot be exact or even very accurate without first
knowing something about what is being predicted. This uncertainty would preclude
the quantitative test of letter recognition models if we were not able to
estimate free parameters.

In parameter estimation, we use our observations of the subject's behavior to
estimate the values of the free parameters of the model being tested. Because we
want to give every model its best shot, our goal should be to find the values of
the parameters that maximize how accurately the model is able to account for the
results.

Because we want to give every model its best shot, our goal should be to find
the values of the parameters that maximize how accurately the model is able to
account for the results. This is called "maximizing the goodness of fit" of the
model. When we compare competing models, each model should be predicting as well
as it can to increase the fairness of the test.

.. image:: ../img/Massaro_1998_fig_16.png
   :align: center
   :width: 50%

.. image:: ../img/Massaro_1998_fig_18.png
   :align: center
   :width: 50%

Fuzzy logical model of perception
--------------------------------------------------------------------------------

.. image:: ../img/Massaro_1998_fig_19.png
   :align: center
   :width: 50%

.. image:: ../img/Massaro_1998_fig_20.png
   :align: center
   :width: 50%

Benchmark measures of goodness of fit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even if a model is a correct description of the psychological processes
involved, we cannot expect it to fit observations perfectly.

Context effects in pattern recognition
================================================================================
:Pages: 338-343 (6)

The pattern recognition experiments discussed up to this point have manipulated
one or two bottom up sources of information.

Bottom-up sources refer to sources conveying information more or less directly
from the stimulus such as the gap size and line angle variables.

Another source has been dubbed "top-down" to refer to other relevant information
that a perceiver has available, including word knowledge and the information
that emerges from the context accompanying the bottom-up sources.

The context coveys information because a perceiver has prior knowledge about how
the context constrains the bottom-up information.

.. image:: ../img/Massaro_1998_fig_21.png
   :align: center

.. image:: ../img/Massaro_1998_fig_22.png
   :align: center

Test of the FLMP
--------------------------------------------------------------------------------

Sentence context in word recognition
--------------------------------------------------------------------------------

.. image:: ../img/Massaro_1998_fig_23.png
   :align: center

Artificial neural network models
================================================================================
:Pages: 343-356 (14)

Connectionist model of perception
--------------------------------------------------------------------------------

Interactive activation model
--------------------------------------------------------------------------------

IAM with input noise and best-one-wins decisions rule
--------------------------------------------------------------------------------

Justification of computational modeling
================================================================================
:Pages: 356-360 (5)

Difficulties in psychological inquiry
--------------------------------------------------------------------------------

Implications for psychological inquiry
--------------------------------------------------------------------------------

Metatheoretical issues and the computational approach
================================================================================
:Pages: 360-362 (3)

Identifiability issue
--------------------------------------------------------------------------------

Optimality of pattern recognition
--------------------------------------------------------------------------------

Footnotes
================================================================================

.. [*]
    In proposing this, I am assuming that asking for a continuous rating rather
    than a discrete categorization judgment does not change the underlying
    perceptual processes. I think of letter and word recognition as automatic.
    The nature of the response should not greatly influence the perceptual
    processing that leads to the response.

.. [*]
    RGR calculated the probability of some alternative ``X`` against ``Y`` as
    ``M(X) / (M(X) + M(Y)`` where ``M(x)`` is the goodness of match of a test
    item with template ``x``.

    .. image:: ../img/Massaro_1998_fig_15.png
       :align: center
       :width: 50%

    One justification of the RGR is the probability matching that is often
    observed in decision making.

    The RGR also captures what appears to be a reasonable relationship between
    stimuli and responses in pattern recognition. Consider a case in which a
    test letter gives a reasonably good match only to the first alternative and
    a second case in which the test letter gives a good match to the first
    alternative and a somewhat less good match to the second alternative. If the
    absolute match were the important value for the decision, the probability of
    classifying the letter as the first alternative should be 1 in both cases.
    However, the RGR predicts that the probability of classifying the letter as
    the first alternative in the second case should be much less.

.. |Figure8| image::
    ../img/Massaro_1998_fig_8.png
    :align: middle
    :width: 100%

.. |Figure9| image::
    ../img/Massaro_1998_fig_9.png
    :align: middle
    :width: 100%

.. |Figure10| image::
    ../img/Massaro_1998_fig_10.png
    :align: middle
    :width: 100%

.. |Figure11| image::
    ../img/Massaro_1998_fig_11.png
    :align: middle
    :width: 100%

.. |Figure12| image::
    ../img/Massaro_1998_fig_12.png
    :align: middle
    :width: 100%

.. |Figure13| image::
   ../img/Massaro_1998_fig_13.png
   :align: middle
   :width: 100%

.. |Figure14| image::
   ../img/Massaro_1998_fig_14.png
   :align: middle
   :width: 50%

.. |Figure16| image::
   ../img/Massaro_1998_fig_16.png
   :align: middle

.. |Figure17| image::
   ../img/Massaro_1998_fig_17.png
   :align: middle

