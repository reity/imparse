=======
imparse
=======

Lightweight infinite-lookahead parser generator that supports basic grammars defined in a JSON format.

.. image:: https://badge.fury.io/py/imparse.svg
   :target: https://badge.fury.io/py/imparse
   :alt: PyPI version and link.

Purpose
-------
This library makes it possible to rapidly assemble and deploy a parser for a simple language. It is intended primarily for languages that have an `LL grammar <https://en.wikipedia.org/wiki/LL_grammar>`_.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install imparse

The library can be imported in the usual ways::

    import imparse
    from imparse import *
