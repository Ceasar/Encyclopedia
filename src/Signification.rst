
================================================================================
Signification
================================================================================

The denotation of an expression is ...

# Terms

## Denoting Phrase

Denotation, in other words, is a semantically inert property, in this view.

Russel claims propositions must have existent things as their constituents.

According to the conceptualist view, the denotation of a sign is a concept.

Example: (denotation "the present king of France")  == THE_PRESENT_KING_OF_FRANCE
Example: (denotation "the present king of England") == THE_PRESENT_KING_OF_ENGLAND
Example: (denotation "a man")                       == MAN
Example: (denotation "the round square")            == ???

According to the referentialist view, a sign `s` denotes a thing `x` iff `x` satisfies the logical form of `s`.

Example:
    (denotes "the present king of France") :: Being -> Bool

    For all Being's, this is False.
Example: (denotation "the present king of England") :: Being -> Bool
Example: (denotation "a man") ==
Example: (denotation "the center of mass of the solar system") ==

```
>>> meaning("The author of Waverly")
(exists (x)
        (and (forall (y) (if (is_author_of_waverly x) (= x y))) ; uniqueness
             (is_author_of_waverly(x))))
>>> meaning("The author of Waverly was a man")
(exists (x)
        (and (forall (y) (if (is_author_of_waverly x) (= x y))) ;; uniqueness
             (is_author_of_waverly x)
             (man x)))
```

# Referent

The object denoted by a referential expression is called the referent.

Example: (referent "man" (idea man))
Example: (referent "man" Socrates)

# Extension

The extension of a sign is the set of all things it denotes.

```
>>> (extension Pegasus)
{}
>>> (extension a_round_square)
{}
>>> (extension the_present_king_of_France)
{}
>>> (extension the first king of England)
{Alfred the Great}
>>> (extension a man)
{Socrates, Bill Clinton, Alfred the Great}
>>> (extension white)
{snow, cloud, The White House, chalk}
```

# Connotative (Denominative) Names

A name is connotative iff implies (or connotes) an attribute of its denotation.

Example: "white" denotes all things white and no things not white and implies they are white
Example: "long" denotes all things long and implies they are long
Example: "virtuous" denotes all things virtuous and implies they are virtuous
Example: "man" denotes all men and implies they are men (rational, animal)

A name is connotative if it is defined intensionally.

> The word man, for example, denotes Peter, iJanei , John, and an indefinite number of other individuals, of whom, taken as a class, it is the name. But it is applied to them, because they possess, and to signify that they possess, certain attributes. These seem to be, corporeity, animal life, rationality, and a certain external form, which for distinction we call the human. Every existing thing, which possessed all these attributes, would be called a man; and anything which possessed none of them, or only one, or two, or even three of them without the fourth, would not be so called. For example, if in the interior of Africa there were to be discovered a race of animals possessing reason equal to that of human beings, but with the form of an elephant, they would not be called men. Swift’s Houyhnhnms[*]jwould not bej so called. Or if such newly-discovered beings possessed the form of man without any vestige of reason, it is probable that some other name than that of man would be found for them. How it happens that there can be any doubt about the matter, will appear hereafter. The word man, therefore, signifies all these attributes, and all subjects which possess these attributes. But it can be predicated only of the subjects. What we call men, are the subjects, the individual Stiles and Nokes; not the qualities by which their humanity is constituted. The name, therefore, is said to signify the subjects directly, the attributes indirectly; it denotes the subjects, and implies, or involves, or indicates, or as we shall say henceforth connotes, the attributes. It is a connotative name. (Mill, Of Names)

If an object possesses a certain attribute, a connotative name can be applied to it.
If a connotative name applies to an object, that it possesses a certain attribute is signified.

# Properties

A single object may have many names.

Example: {"Sophroniscus", "the father of Socrates", "a man", "a Greek", "an Athenian", "a sculptor", "an old man", "an honest man", "a brave man"} are all names of Sophroniscus (though not necessarily him alone). Each name can be applied to emphasize a different aspect of him.

Generally, the more specific the connotation, the less specific the denotation.

# Mechanism

Names connote because their definitions are intensional and biconditional.

Example: A thing is a bachelor iff it is an unmarried man. Therefore, when we call something an bachelor, we connote it is an unmarried man.

Names connote a comprehension.

# Purpose

Connotative names are applied for different reasons.

Anyone who understands the meaning of a connotative names apprehends a distinct fact concerning its reference.

Connotation can emphasize certain attributes over others.

Example: "Trilateral" and "Triangle" emphasize different attributes.

SEE: Implicature

Note: Names must convey information/meaning through connotation, not denotation since coextensive terms (aliases) may have different meanings.

Example: "Trilateral" and "Triangle" have different comprehensions but the same extension.

Claim: "Whenever the names given to objects convey any information, that is, whenever they have properly any meaning, the meaning resides not in what they denote, but what they connote. The only names of objects which connote nothing are proper names; and these have, strictly, speaking, no signification." - Mill
