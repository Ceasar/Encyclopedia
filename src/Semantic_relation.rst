
.. include:: index

================================================================================
Semantic Relation
================================================================================

A semantic relation is ...

A semantic relation usually ends in "-nym" meaning "name, word".

# Classification

- Synonym_

- Antonym_

## Homonym

.. code::

    (iff (homonym x y)
         (and (== (spelling x)
                  (spelling y))
              (== (pronunciation x)
                  (pronunciation y))
              (!= (meaning x)
                  (meaning y))))

Example: ("punch" (to hit), "punch" (a drink))
Example: ("dog" (an animal), "dog" (to follow closely))

Note: A homonym is a homophone (same sound)
Note: A homonym is a homograph (same spelling)

## Heteronym

.. code::

    (iff (heteronym x y)
         (and (== (spelling x)
                  (spelling y))
              (!= (pronunciation x)
                  (pronunciation y))
              (!= (meaning x)
                  (meaning y))))

Example: ("desert" (to abandon), "desert" (a dry region))

Note: A homonym is a homograph (same spelling)

## Hypernym

Hypernym refers to a general category.

Example: "vehicle" is a hypernym of "car"

## Hyponym

A hyponym is a specific instance of a category.

Example: "car" is a hyponym of "vehicle"

## Metonym

A metonym is a figure of speech in which a thing or concept is called not by its own name by the name of something associated.

Example: "Hollywood" for the US Film Industry
Example: "Silicon Valley"

## Capitonym 

A capitonym has a different meaning when capitalized.

Example: "polish" to shine; "Polish" from Poland
Example: "caterpillar" insect; "Caterpillar" machinery company

Note: Capitonyms may not be pronounced the same.
