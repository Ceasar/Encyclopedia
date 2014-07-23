

********************************************************************************
Style guide
********************************************************************************

This document gives writing conventions for reStructuredText documents.

Section title adornment
********************************************************************************

Sections are identified through their titles, which are marked up with
adornment: "underlines" below the title text, or underlines and matching
"overlines" above the title.

Adornment should always be 80 characters. This looks good in the text editor and
is simpler than trying to match the number of adornment characters with the
number of characters in the title.

Yes::

    Background
    ================================================================================ 

    Heavy cruiser development steadied between World War I and World War II
    thanks to the terms of the Washington Naval Treaty and successor treaties
    and conferences, where the United States, Britain, Japan, France, and Italy
    agreed to limit heavy cruisers to 10,000 tons displacement with 8-inch main
    armament...

No::

    Background
    ==========

    Heavy cruiser development steadied between World War I and World War II
    thanks to the terms of the Washington Naval Treaty and successor treaties
    and conferences, where the United States, Britain, Japan, France, and Italy
    agreed to limit heavy cruisers to 10,000 tons displacement with 8-inch main
    armament...

One-time anchors
********************************************************************************

If you want to create a non-standard anchor, use an `anonymous hyperlink
target`_::

    .. _Python: http://www.python.org/

    Python_ is `my favourite programming language`__.

    __ Python_


.. _anonymous hyperlink target: http://docutils.sourceforge.net/docs/user/rst/quickref.html#indirect-hyperlink-targets
