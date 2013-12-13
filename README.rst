scholar
=======

Notes on various documents and personal encyclopdia.

Usage
-----

To build html files, simply:

.. code:: bash

    make

To automatically build html from rst files, simply:

.. code:: bash

    python reload.py

This script watches ``/src`` and runs ``make`` if anything is modified.


To search for documents (title or contents), simply:

.. code:: bash

    ./scripts/search <keyword>
