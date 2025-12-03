---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Software Attributes

The sections here tabulate the software attribute database.
Each attribute (column) is described in the [](schema).
Some columns contain lists of strings which means that they cannot be fully sorted.
Instead, they can be filtered by searching for a string in the search box

```{code-cell} ipython3
:tags: [hide-cell]

from pathlib import Path
import yaml
from itables import init_notebook_mode
import pandas as pd

init_notebook_mode(all_interactive=True)

software_attr_dir = Path("..", "..", "software_attributes")
model_list_inputs = yaml.safe_load( open(software_attr_dir / "database_list.yaml", "r") )
models = model_list_inputs["active"]

model_attributes_map = {
    model: yaml.safe_load( open(Path("..", "..", "software_attributes", "database", f"{model}.yaml"), "r") )
    for model in models
}

df = pd.DataFrame.from_dict(model_attributes_map, orient="index")
# print(list(df.columns))
# print(df)
```

## General
```{code-cell} ipython3
:tags: [hide-input, full-width]

# Get all columns that begin with "does_"
does_columns = [col for col in df.columns if col.startswith("does_")]

# Make a list of all the "does_" columns that are True for each row dropping the "does_" prefix
# Add this to the dataframe
for i, row in df.iterrows():
    does_list = [col.replace("does_", "") for col in does_columns if row[col]]
    # print(f"{i}: {does_list}")
    df.at[i, "does"] = does_list

general_df = df[[
    "does",
    "programming_language",
    "license_type",
    "data_collection_methods",
    "last_release_date"
]]
general_df
```

## Turbine Modeling
```{code-cell} ipython3
:tags: [hide-input, full-width]

turbine_df = df[[
    "scope",
    "system_location",
    "time_domain",
    "turbine_model",
    "does_loads",
    "does_design_optimization",
    "does_costs",
]]
turbine_df = turbine_df[ pd.DataFrame( turbine_df["scope"].tolist() ).isin( ["turbine", "any"] ).any(axis=1).values ]
turbine_df
```

## Farm Modeling
```{code-cell} ipython3
:tags: [hide-input, full-width]

farm_df = df[[
    "scope",
    "system_location",
    "time_domain",
    "turbine_model",
    "wake_model",
    "does_loads",
    "does_design_optimization",
    "does_costs",
]]
farm_df = farm_df[ pd.DataFrame( farm_df["scope"].tolist() ).isin( ["farm", "any"] ).any(axis=1).values ]
farm_df.dropna()
```

## Cost Modeling
```{code-cell} ipython3
:tags: [hide-input, full-width]

cost_df = df[[
    "scope",
    "system_location",
    "does_design_optimization",
    "does_costs",
    "tags",
]]
cost_df = cost_df[ cost_df["does_costs"] == True]
cost_df.dropna()
```

## Full Suite Modeling Comparison
```{code-cell} ipython3
:tags: [hide-input, full-width]

modeling_df = df[[
    "scope",
    "system_location",
    "time_domain",
    "turbine_model",
    "wake_model",
    "does_controls",
    "does_costs",
    "does_data_analysis",
    "does_design",
    "does_design_optimization",
    "does_simulation",
    "does_loads",
    "tags",
]]
modeling_df
```

## Distribution
```{code-cell} ipython3
:tags: [hide-input, full-width]

distribution_df = df[[
    "supported_platforms",
    "package_manager",
    "package_manager_url",
    "installation_complexity",
]]
distribution_df
```

## Documentation
```{code-cell} ipython3
:tags: [hide-input, full-width]

documentation_df = df[[
    "documentation_url",
    "has_user_docs",
    "has_developer_docs",
    "has_api_docs",
    "has_cli_docs",
    "has_installation_docs",
    "has_getting_started_docs",
    "has_examples_tutorials",
    "has_design_intent_statement",
    "readability",
    "project_coverage",
]]
documentation_df
```

## Testing
```{code-cell} ipython3
:tags: [hide-input, full-width]

testing_df = df[[
    "testing_framework",
    "continuous_testing",
    "test_coverage",
    "test_documentation",
    "performance_tests",
]]
testing_df
```

## Interfaces
```{code-cell} ipython3
:tags: [hide-input, full-width]

interfaces_df = df[[
    "first_class_ui",
    "has_cli",
    "language_interfaces",
    "feature_accessibility",
]]
interfaces_df
```

## Input / Output
```{code-cell} ipython3
:tags: [hide-input, full-width]

io_df = df[[
    "filetypes",
    "file_structure_stability",
]]
io_df
```
