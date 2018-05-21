# {{ module.name }}

{{ module.docstring }}

{% if attributes|length > 0 %}
## Attributes
    {% for attr_data in attributes %}
`{{ attr_data['name'] }}`
    {% endfor %}
{% endif %}


{% if functions|length > 0 %}

## Functions
    {% for func_data in functions %}
### `{{ func_data['name'] }}`

{{ func_data['docstring'] }}

    {% endfor %}
    
{% endif %}


{% if classes|length > 0 %}
## Classes
    {% for class_data in classes %}
    
###`{{ class_data['name'] }}`

{{ class_data['docstring'] }}

        {% if class_data['functions'] > 0 %}
        
            {% for func in class_data['functions'] %}

`{{ func['name'] }}`

{{ func['docstring'] }}

            {% endfor %}

        {% endif %}

    {% endfor %}
{% endif %}
