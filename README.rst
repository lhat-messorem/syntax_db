SyntaxDB
========

|Build Status|

This is a small Python library for accessing the
`SyntaxDB <https://syntaxdb.com/>`__ API.

`SyntaxDB <https://syntaxdb.com/>`__ is a programing language syntax
database. See https://syntaxdb.com/about for more infomation.

Official document of the API can be found at
https://syntaxdb.com/api/v1.

Installation
------------

::

    pip install syntaxdb

Usage
-----

.. code:: python

    import syntaxdb

Authentication
--------------

The usage of the API doesn't require any authentication.

Queries
-------

First, there is an example:

.. code:: python

    import syntaxdb

    db = syntaxdb.syntaxdb()

    #add parameters if neccessary:
    db.parameters['language_permalink'] = 'python'

    #query concepts of language (here is Python):
    db.concept()

Before executing some queries, we need to add the parameters (if
necessary).

.. code:: python

    db.parameters['parameter_name'] = value

Then call ``concept()``, ``language()``, ``category()`` to get what we
want (in the example we get all concepts corresponding to Python).

After finishing query, we can change parameters to make another query.

See parameters list in API's document: https://syntaxdb.com/api/v1.

More detail about operations, parameter's type, required parameters,
response content type ... can be found at the API documentation too.

To query an operation (listed in the API doc), we just simply add
parameters mentioned in the doc (pay attention to required parameters),
then call ``concept()``, ``language()`` or ``category()``.

Changelog:
----------

-  26/2/2017: **0.0.1**

   ::

            Inital release.

            Success build with Travis.

            Pip support.

-  9/3/2017: **0.0.6**

   ::

            Fix bug: function name "addparameters".

-  8/5/2017: **0.1.2**

   ::

            Add Python3 support.

Contributing
------------

Bug reports and pull requests are welcomed at
https://github.com/lhat-messorem/syntax\_db.

License
-------

This library is a open source software licensed under the `MIT
License <http://opensource.org/licenses/MIT>`__. Details provided in the
LICENSE file.

SyntaxDB API copyrights © 2017 SyntaxDB

.. |Build Status| image:: https://travis-ci.org/lhat-messorem/syntax_db.svg?branch=master
   :target: https://travis-ci.org/lhat-messorem/syntax_db
