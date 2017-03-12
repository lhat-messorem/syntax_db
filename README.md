#SyntaxDB

[![Build Status](https://travis-ci.org/lhat-messorem/syntax_db.svg?branch=master)](https://travis-ci.org/lhat-messorem/syntax_db)

This is a small Python library for accessing the [SyntaxDB](https://syntaxdb.com/) API.

[SyntaxDB](https://syntaxdb.com/) is a programing language syntax database. See https://syntaxdb.com/about for more infomation.

Official document of the API can be found at https://syntaxdb.com/api/v1.

## Installation

```
pip install syntaxdb
```

## Usage

```Python
import syntaxdb
```

##Authentication

The usage of the API doesn't require any authentication.

##Queries

First, there is an example:

```Python
import syntaxdb

db = syntaxdb.syntaxdb()

#add parameters if neccessary:
db.parameters['language_permalink'] = 'python'

#query concepts of language (here is Python):
db.concept()
```

Before executing some queries, we need to add the parameters (if necessary).

```Python
db.parameters['parameter_name'] = value
```

Then call `concept()`, `language()`, `category()` to get what we want (in the example we get all concepts corresponding to Python).

After finishing query, we can change parameters to make another query.

See parameters list in API's document: https://syntaxdb.com/api/v1.

More detail about operations, parameter's type, required parameters, response content type ... can be found at the API documentation too.

To query an operation (listed in the API doc), we just simply add parameters mentioned in the doc (pay attention to required parameters),
then call `concept()`, `language()` or `category()`.

## Contributing
Bug reports and pull requests are welcomed at https://github.com/lhat-messorem/syntax_db.

## License
This library is a open source software licensed under the [MIT License](http://opensource.org/licenses/MIT).
Details provided in the LICENSE file.

SyntaxDB API copyrights © 2017 SyntaxDB