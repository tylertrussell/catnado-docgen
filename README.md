# catnado-docgen

A Python documentation utility designed to work with `mkdocs`.

Originally built for [`gae-catnado`](https://www.github.com/tylertrussell/gae-catnado),
but it would coul be useful for other projects, too.

Install via `pip install catnado-docgen`.

## Instructions


#### Building Docs for a Python module
Since this project is built to work in conjunction with `mkdocs`, the intended
way to build documentation for a package would be to specify a `mkdocs.yml` file:

`docgen build packagename mkdocs.yml`

Doing so creates all documentation in the `mkdocs` source directory (specified 
by the `docs_dir` key in `mkdocs.yml`) in a folder called `docgen-api`.

At this point you could update the `pages` section of your `mkdocs.yml` file
manually, but for large projects that could quickly become impractical.

If `--update-pages` is specified, the provided `mkdodcs.yml`'s `pages` section 
is updated to contain a `docgen-api` section containing the created docs.


#### Without `mkdocs.yml`

If you want to do something else with the generated markdown documents, you can
just specify an output directory like so:

`docgen build packagename /my/path/here`


#### Support for [Google-style](https://google.github.io/styleguide/pyguide.html#Comments) Python Docstrings

Google docstrings display poorly in markdown.  Take this example:

```
Args:
    test: optional boolean indicating this is a test
Returns:
    Random number
Raises:
    Assertion error if this function is called in production
```

It displays very poorly in Markdown, normally:

Args:
    test: optional boolean indicating this is a test
    test2: optional boolean that is totally unused
Returns:
    Random number
Raises:
    Assertion error if this function is called in production

But this library (which was originally written to document a Python library written
specifically for Google App Engine) will format it nicely:

#### Args

`test`: optional boolean indicating this is a test

`test`: optional boolean indicating this is a test

#### Returns
Random number

#### Raises
Assertion error if this function is called in production
