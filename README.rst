
.. _AUTHORS: https://github.com/Ceasar/Encyclopedia/blob/master/AUTHORS.rst
.. _figure: http://docutils.sourceforge.net/docs/ref/rst/directives.html#figure
.. _quickref: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _reStructedText: http://docutils.sourceforge.net/rst.html
.. _rest: reStructedText_
.. _Homebrew: http://brew.sh/
.. _`the repository`: https://github.com/Ceasar/Encyclopedia
.. _`open a fresh issue`: https://github.com/Ceasar/Encyclopedia/issues

================================================================================
Encyclopedia
================================================================================

.. image:: https://travis-ci.org/Ceasar/Encyclopedia.svg
    :target: https://travis-ci.org/Ceasar/Encyclopedia

**Encyclopedia** is a tool that helps you write and maintain a private
hypermedia encyclopedia.

.. figure:: http://i.imgur.com/J8b6bX3.png

Benefits
================================================================================

- Save time by eliminating redundancy

  Documents on the same subject tend to be mostly redundant. By writing
  hyper-linked notes, you can eliminate this redundancy so that future queries
  get straight to the point.

- Refine your understanding on everything you know

  Encoding ideas forces you to understand them precisely, enabling you to better
  explain the topic to others and ask precise questions about what you don't
  understand.

Features
================================================================================

- reStructedText_ (reST) support

- Document search

.. figure:: http://i.imgur.com/FXUUSNo.jpg

Requirements
================================================================================

- Install Homebrew_

- Install Python and set up the virtualenv:

.. code:: bash

  $ brew install python
  $ pip install virtualenv
  $ make env

To check if everything is set up correctly, go through Quickstart and try to
``make web``.

Quickstart
================================================================================

In this section, we'll go over how to get started with all the major features of
Encyclopedia.

First, we need to create the index: a mapping from hyperlink anchors to target
HTML files. Simply ``touch config/index.rst`` and then edit it to look like
this::

    .. _programming language: Programming_language.html
    .. _Python: Python.html

Next, we'll create two reST_ source files: ``src/Python.rst`` and
``src/Programming_language.rst``.

``src/Python.rst`` should look like this::

    ********************************************************************************
    Python
    ********************************************************************************

    .. figure:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png

    :Date: 1991
    :Developer: Guido van Rossum
    :Website: http://www.python.org/

    **Python** is a `programming language`_ that is interpreted and dynamically
    typed.

    .. contents::

    History
    ********************************************************************************

    Python was created by Guido van Rossum in 1991.


``src/Programming_language.rst`` should look like this::

    ********************************************************************************
    Programming Language
    ********************************************************************************

    A **programming language** is a formal language for communicating instructions
    to a machine.

    For example, Python_.

    .. contents::

    History
    ********************************************************************************

    The first programming language was FORTRAN (1957), followed by Lisp (1958).

Next, run:

.. code:: bash

     $ make web

This will both compile your source files into HTML and start a small server to
view them. If you need to stop the server, hit control-C.

Finally, head over to http://localhost:5001 to access the search page.

.. image:: http://i.imgur.com/B3d3XYQ.png

Just type in "Python" or "Programming Language" to find your pages.

.. image:: http://i.imgur.com/Kcd1jhK.png

At this point, you're ready to start adding your articles.

Philosophy
================================================================================

This section documents why Encyclopedia is designed the way it is.

.. figure:: http://i.imgur.com/toZhI3Q.jpg

Why hyperlinks?
--------------------------------------------------------------------------------

Before writing `Encyclopedia` I used an extensive system of Markdown documents
to manage my notes. This system was deeply nested to capture relationships
between ideas. At some point however, they became unmanageable.

For one, a taxonomy of ideas often makes classification difficult because
certain ideas sit in the intersection of two others (e.g. psycholinguistics is
both a part of psychology and linguistics). To some extent, this can be fixed by
linking files in the filesystem, but doing so is inflexible.

Further, retrieval becomes difficult, since a file could be in a number of
locations.

`Encyclopedia` solves both of these problems by forcing everything into a flat
structure. (This risks ambiguity, but it is expected that to a large degree this
will not be the case, given that the encyclopedia is personal, and in the case
that is, names can disambiguated similar to Wikipedia (which appends the domain,
e.g. "Ball (mathematics)").)

Why reST?
--------------------------------------------------------------------------------

Encyclopedia uses reST (as opposed to other markup languages, such as HTML or
Markdown) for a few reasons.

1. It is already popular in certain communities, especially the Python community
   where it is standard for docs.

2. It is both easier to read and write than HTML (too verbose) and Markdown
   (the link syntax is verbose, e.g.: ``This is [an example](http://example.com/
   "Title") inline link.``).

3. It is more powerful than Markdown. Some important examples:

   - Directives, (e.g. ``contents`` injects a table of contents)

   - Multiple levels of section headers (Markdown supports only ``=`` and ``-``
     and then requires ``#`` prefixes, which are hard to read. reST provides any
     non-alphanumeric character. e.g. ``=-`:.'"~^_*+#``)

Tips
================================================================================

- Expand your knowledge of restructedtext_ with the quickref_. It will take some
  getting used to, but in time it should be more natural than writing Markdown.

- Use the figure_ directive for rendering images; avoid using ``image`` or
  setting any attributes to ensure a consist style that can be changed with CSS.

Contribute
================================================================================

#. Check for open issues or `open a fresh issue`_ to start a discussion
   around a feature idea or a bug.

#. Fork `the repository`_ on GitHub to start making your changes to
   the **master** branch (or branch off of it).

#. Send a pull request and bug the maintainer until it gets merged and
   published. :) Make sure to add yourself to AUTHORS_.
