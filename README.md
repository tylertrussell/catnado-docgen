# catnado-docgen

A Python documentation utility designed to work with `mkdocs`.

Originally built for [`gae-catnado`](https://www.github.com/tylertrussell/gae-catnado),
but it could be useful for other projects, too.

Install via `pip install catnado-docgen`.

**This is a work in progress!**

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
