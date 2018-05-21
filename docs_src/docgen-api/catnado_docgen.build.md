# 




## Attributes
    
`FUNCTIONS`
    
`PAGES`
    
`ERROR_OUTPUT_TARGET`
    
`DOCSTRING`
    
`ERROR_PAGES_YML`
    
`DEFAULT_DOCS_DIR`
    
`CLASS`
    
`FUNCTION`
    
`DOCGEN_API`
    
`MODULE`
    
`ERROR_IMPORT_FAILURE`
    
`CLASSES`
    
`VALUE`
    
`MKDOCS_YML`
    
`NAME`
    
`ATTRIBUTES`
    
`DOCS_DIR`
    





## Functions
    
### `main`

 See __main__.py for exhaustive list of arguments.

  `output_target` is either a `mkdocs.yml` file or a directory in which to dump
  the markdown files.

  If a `mkdocs.yml` file is provided, `--update-pages` will
  automatically update it with the newly-generated documentation.

  Raises:
    ValueError: if specified output target is invalid or specified mkdocs.yml file
      cannot be loaded.
  

    
### `build_pages_config`

 Delete any old documentation from an existing pages entry, if it exists,
  and return a configuration containing the new documentation entries that can
  be converted to YAML.

  Args:
    mkdocs_config: existing configuration from `mkdocs.yml`
    packages: list of package names
    modules: list of module names
  Returns:
    `list` of pages (formatted as `dict`s)
  

    
    



