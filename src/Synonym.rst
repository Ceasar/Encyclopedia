
.. include:: index

================================================================================
Synonym
================================================================================

A **synonym** is a `semantic relation`_.

A pair of words_ are synonyms iff they have similar meanings.

.. code::

    (iff (synonym x y)
         (and (!= (spelling x)
                  (spelling y))
              (!= (pronunciation x)
                  (pronunciation y))
              (== (meaning x)
                  (meaning y))))

Example: ("stone", "rock") (nouns)
Example: ("go", "leave") (verbs)
Example: ("quickly", "rapidly") (adverbs)
Example: ("long", "extended") (adjectives)
Example: ("war", "armed conflict") (noun phrases)
