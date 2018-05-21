# 




## Attributes
    
`FUNCTION`
    
`CLASS`
    
`MODULE`
    





## Functions
    
### `categorize_module_member`

 Determine what the category of the given `module_item` is.

  This categorization will determine how documentation how docs are built
  item
  Categories include:
    - class

  Args:
    module_item: an object out of a module's `__dict__`
  Returns:
    string classifier
  

    
### `get_modules_and_packages_to_document`

 Get a list of module and package names to document.

  Args:
    root_package: module object from `importlib.import_module`
  Returns:
    tuple of package names (str), module names (str) beneath `root_package` that
    should be documented.
  

    
### `categorize_members`

 Get a mapping of key -> type for all items in the given module.

  Dunder items (those whose names begin and end with `__`) are never documented.

  Private items (those whose names begin with `_`) can be included in
  documentation by setting `include_private=True`.

  Args:
    module_class_or_func: module, class, or function whose members should be
      categorized
    include_private: optional bool, whether to include "private" variables (i.e.
      those whose names start with a leading underscore).
  Returns:
    `dict` mapping 'types' to lists of keys from `__dict__`, i.e...
    ```
    {
      'class': ['TestClass', 'OtherClass'],
      'function': ['test1', 'test2']
    }
    ```
  

    
    



