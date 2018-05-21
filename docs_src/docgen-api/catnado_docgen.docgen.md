# 




## Attributes
    
`MKDOCS_YML` =  `mkdocs.yml`
    
`DOCS_DIR` =  `docs_dir`
    
`DOCGEN_API` =  `docgen-api`
    
`ERROR_OUTPUT_TARGET` =  `output_target must specify a mkdocs.yml file or an existing directory`
    
`PAGES` =  `pages`
    
`DEFAULT_DOCS_DIR` =  `docs`
    




## Functions
    
### `build`

 Build Markdown documentation for a specific Python package on the given
  directory.

  See __main__.py for arguments.

  Raises:
    ValueError: if specified output target is invalid or specified mkdocs.yml file
      cannot be loaded.
  

    
### `build_mkdocs_pages_config`


  Args:
    packages: a list of package names
    modules: a list of module names
  Returns:
    `list`; `pages` configuration that can be merged into a `mkdocs.yml` file
  

    



