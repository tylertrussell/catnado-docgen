# 




## Attributes
    
`env_instance`
    
`TEMPLATES_PATH`
    





## Functions
    
### `get_jinja_environment`

 Get the Jinja2 environment to use when rendering templates.

  One copy of the environment is kept at the module-level using `global`.

  Returns:
    jinja2.Environment
  

    
### `render_module_markdown`

 Render a markdown file for the given module.

  Args:
    module: module object to render documentation for
    target: str filename
  Returns:
    str containing rendered template
  

    
    



