
.. _morphology:

==========
Morphology
==========

Morphology is the study of word forms.

Morphology consists of two parts:

1. Lexical morphology (Word formation)
2. Inflectional morphology (grammar, conjugation/declination)

Derivational (Lexical)
------------

Derivational morphology is the study of the formation of new words.

Either a word formation processes is productive or a word formation process is non-productive.

Lexicalization is the process of adding words, set phrases, or word patterns to a language.

- Quasi-systematicity
- Irregular meaning change
- Changes of word class

- Word similarity
    - Morphologically related words are similar
    - In a much different sense than that in statistical semantics
    - They are similar as strings
        Example: {"hospital", "hospitalize", "hospitalization"}

Inflectional
------------

Inflectional morphology is the study of combinations of stems and affixes where the resulting word:

- Has the same word class as the original
- Serves a grammatical/semantic purpose that
    - Different from the original
    - But is nevertheless transparently related to the original

Ambiguity
---------

What's the right parse (segmentation) for "unionizable":

Case: Union-ize-able
Case: Un-ion-ize-able

Each is a valid path through a derivational morphology machine.

Number of way to deal with problem:

- Simply take the first output found
- Find all possible outputs and return them all
- Bias the search so that only one or a few likely paths are explored


# Morphological analysis

# Finite State Transducer (FST)

Finite state traducers map between one representation and another.

Sequential traducers are efficient 

# Stemming & Lemmatization

The goal of stemming and lemmatization is to reduce inflection form and sometimes derivationally related forms of a word to a common base form.

Example: {am, are, is} => be
Example: {car, cars, car's, cars'} => car
Example: "the boy's car are different color" => the boy car be differ color

## Stemming

Stemming is the process of reducing words to their stems.

- Crude heuristic process
- Chops off the ends of words
- Often include the removal of derivational affixes
- Most commonly collapses derivationally related words
-
Lemmatization:

- Does morphological analysis and return the dictionary form of a word
- Commonly only collapses the different inflectional forms of a lemma

---

# Natural Production

Slips of the tongue reveal that affixes can be produced separately from stems.

Example: "It's not only us who have screw looses" (for "screws loose")
Example: "Words of rule formation" for "rules of word formation"
Example: "easy enoughly" for "easily enough"

- Priming tests for verifying hypotheses

A word is recognized faster if it has been seen before recently

----


---

# Regular & Irregular

A regular word follows the rules of morphological transformation.

Example: (walk, walks, walking, walked, walked)

A irregular word does not follow the rules of morphological transformation.

Verbs:

Example: (eat, eats, eating, ate, eaten)
Example: (catch, catches, catching, caught, caught)
Example: (cut, cuts, cutting, cut, cut)

Noun:

Example: (mouse, mice)
Example: (goose, geese)
Example: (ox, oxen)
Example: (go, went)
Example: (fly, flew)
