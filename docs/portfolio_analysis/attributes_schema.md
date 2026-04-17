
(schema)=
# Attribute Schema

The Portfolio Coordination project is constructing a database of all WETO software to facilitate
the portfolio-wide analysis.
Initially, only actively-funded software is included, but it will expand to all software under WETO.
The database consists of attributes of each software project expressed in a YAML file
in the https://github.com/natlabrockies/wetostack repository.
The attributes should conform to the JSON schema (YAML is a superset of JSON) described in
the documentation below.
See the [FLORIS entry](https://github.com/natlabrockies/WETOStack/blob/main/software_attributes/database/floris.yaml)
for an example.

To add or update a project entry, submit a pull request to this repository modifying an
existing project file or creating a new one.
All entries should be in the
[./software_attributes/database](https://github.com/natlabrockies/WETOStack/tree/main/software_attributes/database)
directory.
A [validation script](https://github.com/natlabrockies/WETOStack/blob/main/software_attributes/validate_schema.py)
is available, and it is run automatically upon creation and update of the pull request.

````{admonition} How to read the schema docs
:class: tip, dropdown

The schema docs provide the following information:
- The list of required fields
- A short description, where necessary
- Value data types
- Set of valid values
- An example, where necessary

```{raw} html
<div class="accordion" id="accordionsystem_type">
    <div class="card">
        <div class="card-header" id="headingsystem_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#system_type"
                        aria-expanded="" aria-controls="system_type" onclick="setAnchor('#system_type')"><span class="property-name">system_type</span></button>
            </h2>
        </div>

        <div id="system_type"
             class="collapse property-definition-div" aria-labelledby="headingsystem_type"
             data-parent="#accordionsystem_type">
            <div class="card-body pl-5">
                <span class="badge badge-dark value-type">Type: array of enum (of string)</span><br/>
                <span class="description">
                    <p>The wind energy system architectures supported by the software. Use <code>any</code> if the software is type-agnostic.</p>
                </span>
                <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
                <div class="card">
                    <div class="card-body items-definition" id="system_type_items">
                        <span class="badge badge-dark value-type">Type: enum (of string)</span><br/>
                        <div class="enum-value" id="system_type_items_enum">
                            <h4>Must be one of:</h4>
                            <ul class="list-group">
                                <li class="list-group-item enum-item">"hawt"</li>
                                <li class="list-group-item enum-item">"vawt"</li>
                                <li class="list-group-item enum-item">"awes"</li>
                                <li class="list-group-item enum-item">"any"</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

Each attribute in blue text is a drop-down element.
Try clicking the attribute text "system_type" above to open the element.

The first line indicates the data type required for the value.
In this case, `Type: array of enum (of string)` means the value must be an array where each
element is a string matching one of a predefined set of options.

The next line is a description of the attribute.

Then, contextual information for the data type and available options for the value is provided.
Finally, an example is given in some cases.
````

````{admonition} Quick tips
:class: tip

- Attributes with null values (None) must be removed or commented, such as:
```yaml
key1: value1
# key2:
key3: value3
```
- Boolean values are either `true` or `false`.
- Strings do not require quotes.
````

```{raw} html
:file: schema_doc.html
```

