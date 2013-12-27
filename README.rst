================================================================================
scholar
================================================================================

**scholar** is a set of tools designed for lifetime `personal information
management`_; with active usage, it is intended to greatly speed up information
retrieval. To do so, scholar provides tools for building a personal encyclopedia
with hyperlink support.

Features
================================================================================

- reStructedText_ (reST) support
- Document search

Usage
================================================================================

Using scholar involves writing (reST) documents in ``src`` and then building them
for presentation as HTML in ``build``.

To build HTML files, simply:

.. code:: bash

    make

To automatically rebuild HTML when a source file changes:

.. code:: bash

    make watch

To search documents (by filename or contents), simply:

.. code:: bash

    ./scripts/search <keyword>

Philosophy
================================================================================

This section documents why scholar is designed the way it is.

scholar uses reST (as opposed to other markup languages, such as HTML or
Markdown) for a few reasons. First, it is fairly popular in certain communities,
especially the Python community where it is standard for docs. Second, it is far
more readable and writable than writing directly in HTML. Third, it is both far
more powerful than Markdown, due to a number of factors including directives,
(e.g. ``contents``, which builds a table of contents), multiple levels of
section headers (Markdown supports only ``=`` and ``-`` and then requires ``#``
prefixes, which are hard to read-- reST provides also ``^`` and ``~`` and in
addition, headers surrounded by lines are treated as yet another level of
section header).

scholar discourages nesting documents because, anecdotally, they become
unmanageable. A taxonomy of ideas often makes classification difficult because
certain ideas sit in the intersection of two others (e.g. psycholinguistics is
both a part of psychology and linguistics). To some extent, this can be fixed by
linking files in the filesystem, but doing so is inflexible. Furthermore,
retrieval becomes difficult if linked files do not exist, since a file could be
in a number of locations. By forcing everything into the top-level, all files
are always immediately available. This can create ambiguity, but it is expected
that to a large degree this will not be the case, given that the encyclopedia is
personal, and in the case that is, names can disambiguated similar to Wikipedia
(which appends the domain, e.g. "Ball (mathematics)").

.. _personal information management: http://en.wikipedia.org/wiki/Personal_information_management
.. _reStructedText: http://docutils.sourceforge.net/rst.html
