
.. include:: glossaries/psycholinguistics.h

.. _rumelhart mcclelland 1981:
.. _reicher 1969: ../build/reicher_1969.html 
.. _fig 2.3: ../img/rumelhard_mcclelland_1981_fig_2.3.png

================================================================================
Interactive Processing through Spreading Activation
================================================================================

:Authors: David E. Rumelhart; James L. McClleand
:Date: 1981
:Book: Interactive Processes in Reading. Chapter 2.
:Pages: 37-60 (24)
:Abstract:
    ?

.. contents::

Introduction
================================================================================
:Pages: 37-38 (2)

A central issue in the development of a model of the reading process is *the way
the context in which a linguistic element is found affects the way that element
is processed and ultimately interpreted*.

The authors previously proposed an `interactive model`_, but:

1. It was very general

2. It suffered from a lack of direct connection to an empirical base, and

3. It suffered from a lack of specificity of how the brain might actually out
   such complex computations.
   
Here, the authors attempt to propose a model that addresses these concerns.

Some important facts about word perception
================================================================================
:Pages: 38-43 (6)

`Reicher 1969`_ conclusively demonstrated that |LP|_ in |Ws| and |-Ws| is
dependent on |WC|_. [*]_

The literature provides several important clues to the processes at work in
|WP| that have been central to the development of our model:

1. |WP| seems to rely on the arrangement of |Ls| rather than familiar visual
   forms. [#]_

2. |~Ws| have |Wa| over |-Ws| and |1Ls|. [#]_

3. |WA| is greatly affected by the details of the visual conditions used. [#]_

These findings seem to be compatible with a model in which partial preattentive
activations of letters give rise to the activation of words, which in turn
produce feedback reinforcing the letter activations.

The model
================================================================================
:Pages: 43-50 (8)

Here we review the model we have worked out to achieve this result.

.. image:: ../img/rumelhart_mcclelland_1981_fig_2.1.png
   :height: 350px
   :align: right

Assumptions:

1. Perception consists of a series of interacting levels, each level
   communicating with those immediately above and below it. [*]_

2. Communication proceeds through a spreading activation mechanism in which
   activation at one level "spreads" to neighboring levels.

3. Communication can consists of both `excitatory`_ messages and `inhibitory`_
   messages.

4. Intralevel `inhibitory`_ relationships represent a kind of relationship in
   which certain units at the same level compete. [#]_  
   
Although we assume that there are many levels that might be important in
|WP|, we have found that we can account for many of the major phenomena by
considering only the interactions between "letter-level" and "word-level"
elements. Thus, we elaborate the model only on these two levels, and assume that
the other levels merely generate input to these levels.

Specific assumptions
--------------------------------------------------------------------------------
:Pages: 43-46 (4)

.. image:: ../img/rumelhart_mcclelland_1981_fig_2.2.png
   :height: 500px
   :align: right

For every relevant unit in the system there is an entity called a "node".

Word nodes are located at the word level and letter nodes are located at the
letter level.

Each node has two-way `excitatory`_ or `inhibitory`_ connections to a number of
other nodes, both within levels and between adjacent levels.

Connections within the word level are mutually `inhibitory`_ since only one word
can occur any one time. Connections between the word level and letter level may
be either `inhibitory`_ or `excitatory`_ depending on whether or not the letter
is a part of the word in the appropriate letter position.

Each node has a momentary level of activation. Every moment, the influences of
node's `active`_ `neighbors`_ are combined by a simple weighted average to yield
a net input to the node, which drives its activation.  In the absence of
`active`_ `neighbors`_, nodes are assumed to decay back to an inactive state.

Upon presentation of a stimulus, a set of features inputs are assumed to be made
available to the system. [#]_ As features are detected, they excite letter-level
nodes that contain them and inhibits those that do not. The probability of
detection and the rate at which the feature excites or inhibits the relevant
letter nodes represent the clarity of the visual display.

The operation of the model
--------------------------------------------------------------------------------
:Pages: 46-46

Now we consider what happens when an input reaches the system.

Assume that all prior inputs have had an opportunity to decay, that the entire
system is in its quiescent state, and that each node is at resting level.

The presentation of a stimulus initiates a chain in which certain features are
extracted and excitatory and inhibitory pressures begging to act upon the
letter-level nodes.

The activation levels of certain of the letter nodes are pushed above their
resting levels.

Others receive predominantly inhibitory inputs and are pushed below their
resting levels. These letter nodes, in turn, will begin to send activation to
those word-level nodes of which they are a part and inhibit those word nodes
with which they are not consistent.

In addition, the various letter-level nodes attempt to suppress each other, with
the strongest ones getting the upper-hand. As word-level nodes become active,
they in turn compete with one another and send excitation and inhibition back
down to the letter-level nodes.

If the input features are close to those for one particular set of letter are
consistent with those forming a particular word, the positive feedback in the
system will work to converge rapidly on the appropriate letter set and word. If
not, they will compete will each other; and perhaps no single letter set nor
single word will get enough activation to dominate the others, and their
inhibitory relationships might strangle each other. The details of the process
are greatly affected by the values of various parameters of the model.

Simulations
--------------------------------------------------------------------------------
:Pages: 46-49

Though the basic idea of the model are simple, its behavior is quite complex and
cannot be understand without actually "running" it.

We have been able to do this by simulating the performance on the model using a
computer. To do we have to make several simplifying assumptions.

1. The simulation of the model operates in discrete time slices, or ticks,
   updating the activations of all the nodes in the system one each cycle, on
   the basis of the values on the previous cycle. We have endeavored to keep the
   time slice "thin" enough so that the model's behavior is continuous for all
   intents and purposes.

2. The weight of the excitatory and inhibitory effects of one node on another
   depend only on the levels at which the nodes are located. In other words, the
   strength of the connections between all letter nodes and all words nodes of
   which they are part are assumed to be the same, independent of the identity
   of the words.

3. Simulations have been restricted to four-letter words.


EXAMPLE IS GIVEN

On making responses
--------------------------------------------------------------------------------
:Pages: 49-50

One of the more problematic aspects of a model such as this one is a
specification of how these relatively complex patterns of activity might be
related to the content of percepts and the sorts of response probability as
observe in experiments.

The model assumes that the percept corresponds to a temporal integration of the
pattern of activation over all the nodes.

The integration process is assumed to occur slowly enough that very brief
activations may come and go without necessarily entering perceptual experience
or being accessible for purposes of responding; the longer an activation last,
the more likely it is to be reportable.

Applications of the model to the literature
================================================================================
:Pages: 50-58

Below we try to illustrate a few of the major features of the model's operation
in account for of the most important facts.

The word advantage and its dependence on masking
--------------------------------------------------------------------------------
:Pages: 51-51

It is commonly observed that subjects are able to report the letters in a dim,
degrade, or parafoveal presentation of a word more accurately than letters in
unpronounceable |-Ws|. However there is very little advantage for letters in
words compared to nonwords under these conditions in Reicher.

Perception of pronounceable nonwords
--------------------------------------------------------------------------------
:Pages: 51-54

The flexibility of the perceptual system
--------------------------------------------------------------------------------
:Pages: 54-54

Other effects in the literature
--------------------------------------------------------------------------------
:Pages: 54-56

Context enhancement effects
--------------------------------------------------------------------------------
:Pages: 56-58

Summary and conclusion
================================================================================
:Pages: 58-59

A complete model of the role of context in |LP| would be considerably more
complex.

The processes carried out by the model are clearly not beyond the capability of
simple neural circuits that we already know exist in the brain and nervous
system.

Through the use of computer simulation procedures we have been able to generate
specific predications from out model for nearly all the important phenomena of
word perception. For the most part, these predictions have compared very
favorably with observed results in a wide range of experimental studies.

Footnotes
================================================================================

.. [*]
    Historical findings support the view that |LP|_ in |Ws| and |-Ws| is not
    independent of |WC|. [1]_ However, it is possible to interpret them in terms
    of `postperceptual guessing` [2]_ or `postperceptual forgetting processes`
    [3]_.  `Reicher 1969`_ eliminated these nonperceptual interpretations and
    conclusively demonstrated that |WC|_ facilitates |LP|_. [4]_

.. [*]
    In general, of course, a given level may have more than one level
    immediately above or below it, but for simplicity we now consider the case
    in which there is a linear ordering of levels.

.. [1]
    - |WP|_ is possible in conditions where accurate |LP|_ is not.

    - At a given exposure level, |WP|_ is more accurate for common |Ws| than
      uncommon |Ws|.

    - |LP|_ is more accurate in |~Ws|_ than |-~Ws|_.

.. [2]
    Word perception might be better than nonword perception simply because
    |Ss| could guess imperfectly perceived words based on their knowledge of
    English.

.. [3]
    |WP| might be better than |-WP| simply because a large number of unrelated
    |Ls| might pose a memory load that would limit accuracy of identification,
    even if all the |Ls| were perceived accurately

.. [4]
    Postperceptual guessing can be eliminated because |LP| was more
    accurate in words despite the fact that both alternatives would have formed
    a word.

    Postperceptual forgetting can be eliminated because |LP| was more accurate
    in words than with single |Ls|.

.. [#]
    Recently, researchers found that recognition of familiar visual forms does
    not facilitate |WP|_ over |-WP|_, which suggests that |WP|_ relies on the
    arrangement of |LS|.

    This seems to create a paradox: If |WP|_ relies on the arrangement of |LS|,
    then it seems to follow that |WP|_ relies on the results of |LP|_. But if
    |WC|_ facilitates |LP|_ as in `Reicher 1969`_, then it seems to follow that
    |LP|_ relies on the results of |WP|_. The paradox can be resolved if we
    consider that |LP|_ may be incomplete when interacting with |WK|. Perhaps
    what |WK| does is allows us to reinforce partial |LP| that is consistent
    with |Ws| in our vocabulary.

.. [#]
    Researchers have found that |~Ws| have |WA|_ over |-Ws| and |1Ls|.

    One view that has often been taken concerning these findings holds that
    |WK| is not directly used in |WP|, but the findings that |W| have |WA| over
    |~W| refute that.

    **Would it be possible to get by with a model that makes use of knowledge of
    specific words only?**

    Recent work on the process of constructing pronunciations of |~Ws| suggested
    to us that it might. Research has found that when constructing
    pronunciations of both |Ws| and |-Ws|, our knowledge of the pronunciation of
    specific words similiar to the target word seem to influence the time and
    accuracy of our responding, which suggests pronunciations of |~Ws| are
    synthesized out of activations of pronounciations of |Ws| that are similar
    to the target. (If not enough activations of pronunciations of |Ws| are 
    available, the word is not pronouncable.)
    
    A similar process could be happening in |~WP|, and if so, we might be able
    to explain |WP| and |~WP| based on |WK|.

.. [#]
    Researchers have found that |WA| of |Ws| over |-Ws| is greatly affected by
    visual conditions.

    In particular, two sorts of visual conditions have been widely used:

    1. The target display itself is either very dim or very brief or both, and
       is followed either by **no mask** or **a simple light mask**. [#]_

    2. The target display is a bright, clear, high-contrast presentation of the
       word but is followed quickly by **a high-contrast patterned mask**.

    Under (1) it seems reasonable to imagine that performance is limited largely
    by the quality of the information that can be extracted from the visual
    display.

    When a free-report measure of performance is used, |WA| are large. When a
    `forced-choice`_ task is used, |WA| over |-Ws| is small and only slight
    advantages for |1Ls| compared to letters in words are obtained.

    Under (2), large advantages for |Ws| and |~Ws| compared to |-W| and |1L| are
    observed.

    A variety of different interpretations have been offered for the dependence
    of the |WA| on |VMASK|.

    Possibilites:

    1. The fact that the stimulus is a word makes it possible to maintain
       activations of a representation capturing the information in the display
       longer than would otherwise be the case, thereby increasing the chance
       that the |S| would have enough time to translate the activated
       representation into a form suitable for overt report.

       The feedback mechanism we have been describing might have just such an
       effect; feedback from activations of |Ws| could keep the representations
       of the |L| active longer in the face of |VMASK| than would otherwise be
       the case.

       In no-mask conditions, this feedback:
       
       - would tend to reinforce |Ls| consistent with the |S|'s |WK|

       - would tend to reinforce |Ls| consistent with both the |S|'s |WK| and
         the visual information that he or she has extracted from the display

.. [#]
    This characterizes most of the early work (pre-1970) on word perception.

.. [#]
    Thus, for example, since a string of four letters can be interpreted as, at
    most, one four-letter word, the various possible words mutually inhibit one
    another and in that way compete as possible interpretations of the string.

.. [#]
    For simplicity, inputs consist of letters written in a simple geometric
    font.

    .. image:: ../img/rumelhart_mcclelland_1981_fig_2.3.png
       :height: 200px

Glossary
================================================================================

.. _interactive model:

Interactive model
    A model in which data-driven, bottom-up processing combines with
    conceptually-driven, top-down, processing to cooperatively determine the
    most likely interpretation of the input, proposed by Rumelhart (1977) to
    explicate the role of context during reading.

    Roughly speaking processing in an interactive model proceeds in the
    following way:

    1. The reader begins with a set of expectations about what information is
       likely to be available through visual input.
    2. These expectations, or initial hypotheses, are based on our knowledge of
       the structure of letters, words, phrases, sentences, and larger pieces of
       discourse, including nonlinguistic aspects of the current contextual
       situation.
    3. As visual information from the page begins to become available, it
       strengthens those hypotheses that are consistent with the input and
       weakens those that are inconsistent.
    4. The stronger hypotheses, in turn, make even more specific predications
       about the information available in the visual input.
    5. To the degree that these hypotheses are confirmed, they are further
       strengthened, and the processing is faciliated.

.. _interactive processing:

Interactive processing
    A form of cooperative processing in which all knowledge at all levels of
    abstraction can come into play in the process of reading and comprehension.

.. |LP| replace:: letter perception
.. _LP:
.. _letter perception:

Letter perception
    The process of recognizing letters.

.. |~W| replace:: pseudoword
.. _~W:
.. |~Ws| replace:: pseudowords
.. _~Ws:
.. |-~W| replace:: non-pseudoword
.. _-~W:
.. |-~Ws| replace:: non-pseudowords
.. _-~Ws:

Pseudoword
    A pronounceable nonword.

.. |WA| replace:: word advantage
.. _WA:

Word advantage
    The perceptual advantage of |Ws| over |-Ws| or |1Ls|.

.. |WC| replace:: word context
.. _WC:
.. _word context:

Word context
    A context containing a recognized word.

.. |WP| replace:: |W| perception
.. _WP:
.. |-WP| replace:: |-W| perception
.. _-WP:
.. |~WP| replace:: |~W| perception
.. _~WP:
.. |-~WP| replace:: |-~W| perception
.. _-~WP:
.. _word perception:

Word perception
    The process of recognizing words.

.. |WK| replace:: word knowledge
.. _WK:
.. _word knowledge:

Word knowledge
    Information about the structure of words, including the arrangement of
    letters and the statistical frequency of letters co-occurring in a word.

.. _excitatory:
.. _excitatory message:

Excitatory message
    A message which increases the activation level of its recipient.

.. _inhibitory:
.. _inhibitory message:

Inhibitory message
    A message which decreases the activation level of its recipient.

.. _neighbors:

Neighbors
    The set to which a node connects.

.. _active:

Active node
    A node with a positive degree of activation.
