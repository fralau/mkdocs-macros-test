# Test pluglet for mkdocs-macros

## What it is
This is a test **pluglet** for mkdocs-macros.
Its purpose is to serve as a template
for pluglets.

It exports three macros, which can be used in markdown pages, and aren't particularly
interesting:

- `test_fn(x:float)`: an arithmetic expression.
- `say_hello(s:str)`: displays Hello followed by the string, in italics.
- `test_fn2(s:str)`: same as `say_hello()`but does it slightly differently

For example, you could write:

    He said {{ say_hello('Joe') }}.

Which will be translated into HTML as:

    He said <i>Hello Joe</i>

## How to install it

Directly from pypi:
`pip install mkdocs-macros-test`

Or directly from the github repository: download
the package and run:
`python setup.py install`

## How to call it from an MkDocs project

In the config (`mkdocs.yml`) file:

```yaml
plugins:
  - search
  - macros:
      modules: ['mkdocs_test`] 
```