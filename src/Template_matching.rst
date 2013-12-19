.. include:: index

================================================================================
Template matching
================================================================================

Template matching is a form of `pattern recognition`_ in which the units of
analysis are the same size as the patterns to be recognized. [`Massaro 1998`_]

Template matching has some limitations:

- Template matching has no way to evaluate importance of matches. For example,
  in English the pitch of a speaker's voice is not important in identifying a
  spoken word.

- Simple template matching has no way to evaluate the importance of mismatches.


  .. figure:: ../img/Massaro_1998_fig_2.png

     About one-third of the letter ``H`` and ``N`` can be eliminated either by
     removing the middle line both of the letters or by making the letters out
     dashed line segments. However, the same absolute amount of distortion can
     produce dramatically different results: we cannot recognize which letter is
     which in the first case, but we can in the second.

The problems with template matching become unwieldy when there many patterns to
be recognized because patterns tend to be similar to one another and the number
of template comparisons becomes very large.
