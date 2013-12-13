.. include:: ../shorthand/psycholinguistics.rst

.. _McClelland: James_L_McClelland.html

================================================================================
TRACE model of speech |PER|
================================================================================

TRACE is a `connectionist model` of |sp|, proposed by `McClelland`_ and Elman in
1986.

TRACE was made into a working computer program for running perceptual
simulations.

.. contents::

Processing in TRACE
================================================================================

Processing is carried out in a network consisting of a large number of
interconnected elements called *nodes*.

Different classes of nodes represent acoustic/phonetic features, phonemes, and
words:

- At the |fl|, there is a node for each feature at each of a large number of
  time slices relative to the onset of an utterance.

- At the |pl|, there is a node for each phoneme in each time slice.

- At the |wl|, there is a node for each word, starting in each time slice.

Each node has an activation value which is taken to be translatable into an
estimate of the strength of the hypothesis that the concept the node represents
is present in the signal in the time slice or slices that the node covers.

Thus the pattern of activation over these nodes in the network is the system's
representation of the content of the utterance it is currently processing.

Activations of nodes are continuously updated in TRACE, based on activations of
nodes that project to them.

The activations of nodes are determined by a simple two-part activation
function. When a node's activation exceeds a certain threshold value, it excites
or inhibits other nodes in a way which reflects the mutual consistency or
inconsistency of the concepts represented by each node.

1. Adding together all of the inputs to the node to obtain what is called its
   net input.

2. The net input is then used to update the activation of the node.


Context effects in TRACE
================================================================================

How does TRACE account for |ce|_ on phoneme identification?

.. image:: ../../img/elman_mcclelland_1988_fig_1.png

Like other models, TRACE requires a |rp| to translate activations of nodes into
overt responses. For now, it is sufficient to note that the red assumptions of
TRACE and the interactive-activation model allow the models to approximate the
quantitative predictions of models in which information from lexical and
featural inputs is integrated in a postperceptual decision |m| of the kind
described by Massaro.

Two feature of operation that are relevant to the use of testing the claim,
inherent in the model, that there is feedback from the |wl| to the |pl|:

1. |td| input influences processing by combining additively with |bu| input in
   determining the total, or net input, to the node.

2. The |td| information |p| influences the activation of a phoneme node takes
   time.

We these two points in mind, we can evaluate two different sorts of evidence
that been offered for assessing whether an effect is truly |td| or not.

1. The first is based on signal detection theory... Thus far we have seen that
   TRACE is consistent with evidence that lexical content often operates like
   other cues to phoneme identity, producing an affect which can show up as a
   bias effect in signal detection analysis.

2. Another line of argument that has been offered in support of a
   postperceptual, response-stage view of context effects in phoneme |PER| is
   the fact that they often take time to build up.

We seen then that previous evidence taken in support of models in which the
|ce|_ operate on decision |m| does not in fact constitute evidence that is
inconsistent with the TRACE.

|cfc| in TRACE
================================================================================

TRACE accounts for |ci|_ on phoneme identification by allowing active phoneme
nodes to modulate the connections between the |fl| and |pl| in an adjacent time
slices in just such a way as to |pc|_ for their |ci|_.

TRACE assumes that these |ci|_ occur in basic |ms| of |sp|_.

.. nonessential:

This assumption is generally quite shared.  |ci|_ are ubiquitous, and it has
been suggested that one of the essential functions of the |sp|_ |ms| is to |pc|_
for |ci|_ and recover the underling phonetic code.

Triggering |ter| effects via |tra| influences
================================================================================

In the past, we have studied the behavior of TRACE by always testing the model
under conditions where the |cfc|_ was triggered by the unambiguous presence of
some phoneme which was known to have |ci| on adjacent sounds.  However, in
TRACE, phonemes receive input from the |pl| and the |wl|.  Thus, it is possible
that activations at the |pl| might trigger |cfc|_ whether they are determined
purely by |bu| input or some mix of |bu| and |td| influences.

It is this possibility within TRACE for |td| processing to have indirect effects
on |ll| which suggests a way to answer the question: Are |td| effects real or
only apparent?

The logic is to test for the presence of a |td| effect not by seeing whether a
|hl| can alter an overt decision about a |ll|, but, rather, by seeing whether
the |hl| can actually reach into the |ll| and affect some |tra| |p| - in this
case, |cfc|.

The following two simulations from TRACE illustrate the model's prediction that
such effects will occur.
