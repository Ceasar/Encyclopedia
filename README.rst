
.. _personal information management: http://en.wikipedia.org/wiki/Personal_information_management
.. _quickref: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _reStructedText: http://docutils.sourceforge.net/rst.html
.. _rest: reStructedText_

================================================================================
Encyclopedia
================================================================================

**Encyclopedia** is a set of tools designed for lifetime `personal information
management`_; with active usage, it is intended to greatly speed up information
retrieval. To do so, scholar provides tools for building a personal encyclopedia
with hyperlink support.

Benefits
================================================================================

- Save time by eliminating redundancy

  Writing structured notes enables you to recall what was important about books
  or interests without needing to reread the sources of information that led you
  to them. Since sources tend to be redundant with each other, this potentially
  saves large amounts of time. Hyperlinks let you eliminate more redundancy by
  eliminating it entirely from your notes.

- Refine your understanding on everything you know

  Defining and relating terms reveals areas of your knowledge that are defined
  vaguely. By writing about a topic, you'll force yourself to understand it
  precisely, enabling you to better explain the topic to others and ask precise
  questions about what you don't understand.

Features
================================================================================

- reStructedText_ (reST) support

- Document search

Set up
================================================================================

To set up Encyclopedia, simply:

.. code:: bash

     $ make

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

This section documents why scholar is designed the way it is.

Why hyperlinks?
--------------------------------------------------------------------------------

Before writing `scholar` I used an extensive system of Markdown documents to
manage my notes. This system was deeply nested to capture relationships between
ideas. At some point however, they became unmanageable.

For one, a taxonomy of ideas often makes classification difficult because
certain ideas sit in the intersection of two others (e.g. psycholinguistics is
both a part of psychology and linguistics). To some extent, this can be fixed by
linking files in the filesystem, but doing so is inflexible.

Further, retrieval becomes difficult, since a file could be in a number of
locations.

`scholar` solves both of these problems by forcing everything into a flat
structure. (This risks ambiguity, but it is expected that to a large degree this
will not be the case, given that the encyclopedia is personal, and in the case
that is, names can disambiguated similar to Wikipedia (which appends the domain,
e.g. "Ball (mathematics)").)

Why reST?
--------------------------------------------------------------------------------

scholar uses reST (as opposed to other markup languages, such as HTML or
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

Using scholar involves writing (reST_) documents in ``src`` and then building
them for presentation as HTML in ``build``.

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

- If you open up the project in Finder and then drag ``build`` to your
  browser's bookmarks bar, you can access your files with relative ease (and get
  a very crude search).

- Underlines and overlines for section headers should always be 80
  characters. This looks good, and avoids any pain that might come from trying
  to match the number of adornment character with the number of character in the
  title.
