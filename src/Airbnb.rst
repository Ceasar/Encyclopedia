
================================================================================
AirBnB
================================================================================

- Founded 08; raised $120M; ? engineers
- Asks _very_ specific front-end engineering questions.
- Just started intern program in 2013

Screens
================================================================================

Phone Screen 1:

1. Lookup by distance problem.

    Given a dictionary (list of words), write a function "similar" that takes a query "q" and returns
    all words in the dictionary that are edit distance <= 1 from q.

    dictionary: [bat, batt, cat, beetle]

    q: "bat"
    similar(q) => [bat, cat, batt]

    q: "cats"
    similar(q) => [cat]

    q: "cat"
    similar(q) => [bat, cat]

    Edit distance: minimum number of edits required to turn one word into another
    Edit: add a character, remove a character, or change a character

.. code::


    var dictionary = ['bat', 'batt', 'cat', 'beetle'];

    function similar(q) {
      return dictionary.filter(function (word) {
        return (isEditDist(word, q) || isInsertDist(word, q));
      });
    }

    // word1: ball, word2: aball

    function isEditDist(word1, word2) {
      var numEdit = 0;
      if (word1.length !== word2.length) return false;
      for (var i = 0; i < word1.length; i++) {
        if (word1[i] !== word2[i]) {
          numEdit++;
        }

        if (numEdit > 1) {
          return false;
        }
      }
      return true;
    }

Phone Screen 2:

1. Implement binary search tree. `insert`, `exists`, `delete`.

Onsite interview:

1. Nontechnical with engineer.
2. SRE. Implement a subset of regular expressions that just boolean matches and uses `a-z`, `.`, `*`, and `?`.
3. Encode March Madness brackets efficiently.
4. Given a dictionary of alien words, figure out an alphabet.
5. Behavioral.
6. Behavioral.
