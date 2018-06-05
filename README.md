# catnado-docgen

A Python documentation utility designed to work with `mkdocs`.

Originally built for [`gae-catnado`](https://www.github.com/tylertrussell/gae-catnado),
but it could be useful for other projects, too.

Install via `pip install catnado-docgen`.

**This is a work in progress!**

## Instructions


#### In conjunction with `mkdocs.yaml`

To document a package in a project that has a `mkdocs.yaml` file, simply run:
```
docgen build packagename mkdocs.yml --update-pages
```

This scans `packagename` recursively, extracting Python docstrings and building
Markdown source files from them.

The new Markdown files are written to a folder called `docgen-api` in your 
`docs_dir` (as specified in `mkdocs.yml`).

The `--update-pages` option updates the `mkdocs.yml` `pages` entry to contain a 
nested structure of packages and submodules under the heading `docgen-api`.


#### Without `mkdocs.yml`

If you want to do something else with the generated markdown documents, you can
just specify an output directory like so:

`docgen build packagename /my/path/here`

This will write the Markdown source to the specified directory.
