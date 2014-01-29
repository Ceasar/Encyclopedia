
.. include:: index

================================================================================
Antonym
================================================================================

An **antonym** is a `semantic relation`_.

A pair of words_ are antonyms iff they have opposite meanings.

.. code::

    (iff (synonym x y)
         (and (!= (spelling x)
                  (spelling y))
              (!= (pronunciation x)
                  (pronunciation y))
              (== (meaning x)
                  (opposite (meaning y)))))

Example: ("short", "tall")
Example: ("short", "long")

Often, antonyms can be formed with prefix.

Example: ("real", "unreal")
Example: ("flexible", "inflexible")
Example: ("mortal", "immortal")

Kinds
================================================================================

Four type of antonyms exist:

1. Gradable antonym
2. Complementary antonym
3. Relational antonym
4. Auto-antonym (contronym) (antagonym)

An antonym is gradable iff there is degree of variation.

Example: ("slow", "fast")
Example: ("hot", "cold")

An antonym is complementary iff is no degree of variation.

Example: ("mortal", "immortal")
Example: ("sane", "insane")

An antonym is relational iff it is a converse.

Example: ("parent", "child")

An antonym is an auto-antonym iff the opposite word are homonyms.

Example: ("fast" (moving quickly), "fast" (stuck in place))
Example: ("cleave" (to stick together), "cleave" (to split apart))
