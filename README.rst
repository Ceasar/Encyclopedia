
.. _figure: http://docutils.sourceforge.net/docs/ref/rst/directives.html#figure
.. _quickref: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _reStructedText: http://docutils.sourceforge.net/rst.html
.. _rest: reStructedText_

================================================================================
Encyclopedia
================================================================================

**Encyclopedia** is a tool that helps you write and maintain a private
hypermedia encyclopedia.

.. image:: http://i.imgur.com/B3d3XYQ.png

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

Set up
================================================================================

To set up Encyclopedia, simply:

.. code:: bash

     $ make server

Then navigate to http://localhost:5001 to access the search page.

Quickstart
================================================================================

In this section, we'll go over how to create a link between two files.

First, create a file ``src/index``. This file will be a mapping from
hyperlink anchors to their target HTML files. It should look like this::

    .. _programming language: Programming_language.html
    .. _Python: Python.html

Next, we'll create two reST_ files: ``src/Python.rst`` and
``src/Programming_language.rst``.

``src/Python.rst`` should look like this::

    .. include:: index

    ================================================================================
    Python
    ================================================================================

    **Python** is a `programming language`_.
    
``src/Programming_language.rst`` should look like this::

    .. include:: index

    ================================================================================
    Programming Language
    ================================================================================

    A **programming language** is a formal language for communicating
    instructions to a machine.

    Examples
    ================================================================================

    - Python_

Finally, run ``make``. ``build`` should contain two files,
``Programming_language.html`` and ``Python.html`` which contain working links to
each other.

At this point you're reading for creating your own documents. You'll want to
expand your knowledge of restructedtext_ with the quickref_. It takes some
getting to used to, but in time it should be as natural as writing Markdown.

Philosophy
================================================================================

This section documents why Encyclopedia is designed the way it is.

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

2. It is easier to read and write than HTML.

3. It is far more powerful than Markdown. Some important examples:
   
   - Directives, (e.g. ``contents``, which builds a table of contents)
     
   - Multiple levels of section headers (Markdown supports only ``=`` and ``-``
     and then requires ``#`` prefixes, which are hard to read. reST provides
     any non-alphanumeric character. e.g. ``=-`:.'"~^_*+#``)

Usage
================================================================================

Using Encyclopedia involves writing (reST_) documents in ``src`` and then
building them for presentation as HTML in ``build``.

To build HTML files, simply:

.. code:: bash

    make

This will scan ``src`` for any files with the ``.rst`` extension and build them
into HTML.

To automatically rebuild HTML when a source file changes:

.. code:: bash

    make watch

To search documents (by filename or contents), simply:

.. code:: bash

    ./scripts/search <keyword>

Tips
================================================================================

- Use the figure_ directive when including images; avoid using ``image`` or
  setting any attributes to ensure a consist style that can be changed with CSS.

- Underlines and overlines for section headers should always be **80**
  characters. This looks good, and avoids any pain that might come from trying
  to match the number of adornment character with the number of character in the
  title.
