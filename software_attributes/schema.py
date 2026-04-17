
import json
import os
import shutil
# import datetime

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

schema = {
    # "$schema": "https://json-schema.org/draft/2019-09/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {

        ## General
        "github_account": {
            "description": "The associated account on GitHub.\n"
                "In the web address, this is the middle component: "
                "https://github.com/<account>/<repo>.",
            "type": "string"
        },
        "github_repo": {
            "description": "The repository name.\n"
                "In the web address, this is the last component: "
                "https://github.com/<account>/<repo>.",
            "type": "string"
        },      
        "active_funding": {
            "description": "Has this project received funding to directly support "
                "software development in the current quarter?",
            "type": "boolean"
        },
        "development_status": {
            "description": "\n".join([
                "- `on_hold`: No active development or maintenance",
                "- `maintenance`:  Maintenance activities only including bug fixes",
                "- `new_features`: Actively planning and developing new features",
            ]),
            "enum": [
                "on_hold",
                "maintenance",
                "new_features"
            ]
        },
        "programming_language": {
            "description": "The primary programming language even though many projects "
                "contain source code in a few languages.",
            "enum": ["python", "fortran", "matlab", "c++", "rust", "julia", "r"]
        },
        "license_type": {
            "description": "Choose the corresponding license string from "
                "[this list of license types](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#searching-github-by-license-type).",
            "enum": [
                "afl-3.0",
                "apache-2.0",
                "artistic-2.0",
                "bsl-1.0",
                "bsd-2-clause",
                "bsd-3-clause",
                "bsd-3-clause-clear",
                "bsd-4-clause",
                "0bsd",
                "cc",
                "cc0-1.0",
                "cc-by-4.0",
                "cc-by-sa-4.0",
                "wtfpl",
                "ecl-2.0",
                "epl-1.0",
                "epl-2.0",
                "eupl-1.1",
                "agpl-3.0",
                "gpl",
                "gpl-2.0",
                "gpl-3.0",
                "lgpl",
                "lgpl-2.1",
                "lgpl-3.0",
                "isc",
                "lppl-1.3c",
                "ms-pl",
                "mit",
                "mpl-2.0",
                "osl-3.0",
                "postgresql",
                "ofl-1.1",
                "ncsa",
                "unlicense",
                "zlib",
            ]
        },
        "data_collection_methods": {
            "description": "\n".join([
                "- `modeling`: Retrieved from a numerical model",
                "- `laboratory`: Data from a controlled experiment such as RAAW",
                "- `field`: Data from systems \"in the field\", typically in a commercial setting",
            ]),
            "type": "array",
            "items": {
                "enum": [
                    "modeling",
                    "laboratory",
                    "field"
                ]
            }
        },
        "last_release_date": {
            "description": "Date of the last tagged release available on GitHub; "
                "use the following format: YYYY-MM-DD.",
            "type": "string"
            # "type": datetime.date,
            # "pattern": "date"
        },

        ## Modeling
        "scope": {
            "description": "The wind energy system scope of the software.  System implies engineering and cost coupling",
            "type": "array",
            "items": {
                "enum": ["turbine", "farm", "system", "atmosphere"]
            }
        },
        "system_type": {
            "description": "The wind energy system architectures supported by the software. "
                "Use `any` if the software is type-agnostic.",
            "type": "array",
            "items": {
                "enum": ["hawt", "vawt", "awes", "any"]
            }
        },
        "system_location": {
            "description": "The location of the wind energy system supported by the software. "
                "Use `any` if the software is location-agnostic and `offshore` for fixed + floating.",
            "type": "array",
            "items": {
                "enum": ["land", "offshore", "fixed_offshore", "floating_offshore", "any"]
            }
        },
        "time_domain": {
            "description": "Does the software support modeling or analysis in a dynamic "
            "time domain, steady-state, and/or the frequency domain? "
            "This is an array-type field, so include multiple elements, as needed.",
            "type": ["string", "array"],
            "items": {
                "enum": ["steady", "dynamic", "frequency"]
            },
            "examples": [
                {
                    "time_domain": [
                        "steady",
                        "dynamic",
                        "frequency",
                    ]
                }
            ],
        },
        "turbine_model": {
            "description": "The fidelity with which the turbine is represented in the software model (if at all).  Options are 'regression' (e.g. NLR CSM), 'lookup_table' (e.g. in FLORIS), 'momentum_sink' (e.g. in WRF), 'multibody_bem' (e.g. OpenFAST), 'vortex_method' (e.g. OLAF), 'actuator' (e.g. in CFD), 'geometry_resolved' (e.g. in CFD), 'SCADA' (e.g. FLASC/OpenOA)",
            "type": "array",
            "items": {
                "enum": [
                    "regression",
                    "lookup_table",
                    "momentum_sink",
                    "multibody_bem",
                    "vortex_method",
                    "actuator",
                    "geometry_resolved",
                    "SCADA",
                    "N/A"
                ]
            }
        },
        "wake_model": {
            "description": "The fidelity with which turbine wakes are represented in the software model (if at all).",
            "type": "array",
            "items": {
                "enum": [
                    "analytical",
                    "dynamic_meandering",
                    "vortex_method",
                    "navier_stokes",
                    "N/A"
                ]
            }
        },
        "does_controls": {
            "description": "Does the software model controls for wind energy or adjacent systems?",
            "type": "boolean"
        },
        "does_costs": {
            "description": "Does the software model or focus on costs?",
            "type": "boolean"
        },
        "does_data_analysis": {
            "description": "Is the software primarily a used for analyzing data separate from generating data?",
            "type": "boolean"
        },
        "does_design": {
            "description": "Is the software considered a design tool?",
            "type": "boolean"
        },
        "does_design_optimization": {
            "description": "Can the software conduct design optimization?",
            "type": "boolean"
        },
        "does_simulation": {
            "description": "Does the software generate characteristic data about it's relevant scope given a description of the system and initial and boundary conditions?",
            "type": "boolean"
        },
        "does_loads": {
            "description": "Does the software calculate system loads?",
            "type": "boolean"
        },
        "tags": {
            "description": "\n".join([
                "List tags describing the methods and underlying equations modeled in the "
                "software. These are free-form entries, and are not validated. "
                "This field is not currently used, but aggregating the tags throughout "
                "the software portfolio will allow for categorizing the tools later."
            ]),
            "examples": [
                {
                    "tags": [
                        "Euler bernoulli beam theory",
                        "Blade element momentum theory",
                        "Reynolds averaged Navier-Stokes",
                        "Large eddy simulation",
                        "Monte carlo methods",
                    ]
                }
            ],
            "type": "array",
            "items": {
                "type": "string"
            }
        },

        ## Distribution
        "supported_platforms": {
            "description": "List the type of computing platforms that are supported. "
                "Use `any` if the software is platform-agnostic.",
            "type": "array",
            "items": {
                "enum": ["linux", "windows", "macos", "HPC", "any"]
            }
        },
        "package_manager": {
            "description": "List the package managers leveraged to distribute the software.",
            "type": "array",
            "items": {
                "enum": ["homebrew", "pypi", "conda", "conda-forge", "spack_manager", "julia"]
            }
        },
        "package_manager_url": {
            "description": "For any package managers listed in `package_manager`, "
                "include the URL to the package listing.",
            "type": "array",
            "items": {
                "type": "string"
                # "format": "hostname" ?
            }
        },
        "installation_complexity": {
            "description": "\n".join([
                "Estimate the difficulty for a user with minimal context to install.",
                "- `1` is a downloadable executable that can be double clicked",
                "- `10` requires compiling from source code with numerous other compiled dependencies.",
            ]),
            "type": "integer",
            "minimum": 1,
            "maximum": 10,
        },

        ## Documentation
        "documentation_url": {
            "description": "Provide the URL to the project's online documentation.",
            "type": "string"
            # "format": "hostname" ?
        },
        "has_user_docs": {
            "description": "Does the documentation contain a section tailored to using "
                "(i.e. executing, developing inputs, understanding outputs) the software?",
            "type": "boolean"
        },
        "has_developer_docs": {
            "description": "Does the documentation contain a section tailored to developing "
                "(i.e. extending, maintaining, testing) the software?",
            "type": "boolean"
        },
        "has_api_docs": {
            "description": "Does the documentation contain a description of the public API's?",
            "type": "boolean"
        },
        "has_cli_docs": {
            "description": "Does the documentation contain a description of the "
                "command line interface?",
            "type": "boolean"
        },
        "has_installation_docs": {
            "description": "Does the documentation contain a section describing the "
                "installation procedures?",
            "type": "boolean"
        },
        "has_getting_started_docs": {
            "description": "Does the documentation contain a section to guide new users "
                "through the onboarding and getting started process?",
            "type": "boolean"
        },
        "has_examples_tutorials": {
            "description": "Are examples or tutorials included with the software either "
                "through the documentation or in the repository directly?",
            "type": "boolean"
        },
        "has_design_intent_statement": {
            "description": "Is a statement describing the holistic design intent and "
                "design considerations of the software available?",
            "type": "boolean"
        },
        "readability": {
            "description": "Estimate the readability of the documentation considering a "
                "user with minimal context.",
            "type": "integer",
            "minimum": 1,
            "maximum": 10,
        },
        "project_coverage": {
            "description": "Estimate the portion of the project covered by the documentation.",
            "type": "integer",
            "minimum": 1,
            "maximum": 10,
        },

        ## Testing
        "testing_framework": {
            "description": "Does the software leverage a testing framework?",
            "type": "boolean"
        },
        "continuous_testing": {
            "description": "Does the software have continuous testing in place?",
            "type": "boolean"
        },
        "test_coverage": {
            "description": "The portion of the project covered by formal tests.",
            "type": "integer",
            "minimum": 0,
            "maximum": 100,
        },
        "test_documentation": {
            "description": "Is documentation for the tests available?",
            "type": "boolean"
        },
        "performance_tests": {
            "description": "Are performance tests available?",
            "type": "boolean"
        },

        ## Interfaces
        "first_class_ui": {
            "description": "List the user interfaces that receive primary funding or developer "
                "attention.",
            "type": "array",
            "items": {
                "enum": [
                    "gui",
                    "input_files",
                    "library_interface",
                    "web",
                ]
            }
        },
        "has_cli": {
            "description": "Is a command line interface available?",
            "type": "boolean"
        },
        "language_interfaces": {
            "description": "List the connections available to interface the software "
                "to other languages.",
            "type": "array",
            "items": {
                "enum": ["python", "fortran", "matlab", "c++", "rust", "julia", "r"]
            }
        },
        "feature_accessibility": {
            "description": "How much of the project is reachable through a public API?",
            "type": "integer",
            "minimum": 1,
            "maximum": 100,
        },

        ## Input / Output
        "filetypes": {
            "description": "List the filetypes used in the project including inputs and outputs.",
            "type": "array",
            "items": {
                "enum": [
                    "csv",
                    "custom",
                    "hdf5",
                    "json",
                    "numpy binary",
                    "pvd",
                    "xdmf",
                    "yaml",
                    "xlsx",
                ]
            }
        },
        "file_structure_stability": {
            "description": "\n".join([
                "- `stable`: Never or rarely changes",
                "- `in_development`: Actively changing",
                "- `semantic_versioning`: Changes according to rules of semantic versioning"
            ]),
            "enum": [
                "stable",
                "in_development",
                "semantic_versioning"
            ]
        },

        ## WETO Integrations (downstream)
        "dependencies": {
            "description": "\n".join([
                "List other WETO software projects that this one depends on either "
                "through a direct or indirect connection.",
                " - `direct`: code-code integration",
                " - `indirect`: one uses the output of the other via output file or another workflow process",
                "",
                "This field is a 2D list. See the example below for syntax.",
                "",
                "An example of a real dependency is FLORIS requires a power coefficient and "
                "thrust coefficient look up table from a higher fidelity simulation or "
                "field data. This often comes from OpenFAST, so that tool is an indirect "
                "dependency of FLORIS."
            ]),
            "examples": [
                {
                    "dependencies": [
                        ("openfast", "direct"),
                        ("floris", "direct"),
                        ("exawind", "indirect"),
                    ]
                }
            ],
            "type": "array",
            "items": {
                "type": "array",
                "prefixItems": [
                    { "type": "string" },
                    {
                        "enum": [
                            "direct",
                            "indirect"
                        ]
                    }
                ]
            }
        },

    # TODO: These should be automatically compiled
    #     ## Community Health
    #     "open_issues": {
    #         "type": "integer",
    #         "minimum": 0,
    #     },
    #     "open_pull_requests": {
    #         "type": "integer",
    #         "minimum": 0,
    #     },
    #     "average_time_to_engage": {
    #         "type": "integer",
    #         "minimum": 0,
    #     },
    #     "outside_contributors": {
    #         "type": "integer",
    #         "minimum": 0,
    #     },
    }
}

# "name": {"type": "string"},
# "age": {"type": "number"},
# "scores": {
#     "type": "array",
#     "items": {"type": "number"},
# },
# "address": {"$ref": "#/$defs/address"},
#     },
#     "required": ["name"],
#     "$defs": {
#         "address": {
#             "type": "object",
#             "properties": {
#                 "street": {"type": "string"},
#                 "postcode": {"type": "string"},
#             },
#             "required": ["street"],
#         },
#     },
# }


if __name__ == "__main__":

    # Export the schema defined above as a json file
    json.dump(schema, open("schema.json", "w"), indent=4)

    # Configure the docs
    config = GenerationConfiguration(
        minify=False,
        copy_css=True,
        expand_buttons=True,
        show_breadcrumbs=False,
        show_toc=True,
        collapse_long_descriptions=False,
        collapse_long_examples=False,
        description_is_markdown=True,
        examples_as_yaml=True,
        # template_md_options={
        #     "badge_as_image": True,
        #     "show_heading_numbers": False
        # },
        # template_name="md_nested"
    )

    # Using the json file and config from above, create the docs web page
    generate_from_filename("schema.json", "schema_doc.html", config=config)

    # Copy html, css, and js to the docs directory
    shutil.copy2("schema_doc.html", "../docs/portfolio_analysis")
    shutil.copy2("schema_doc.css", "../docs/portfolio_analysis")
    shutil.copy2("schema_doc.min.js", "../docs/portfolio_analysis")

    # Clean up the current directory
    os.remove("schema_doc.html")
    os.remove("schema_doc.css")
    os.remove("schema_doc.min.js")
    os.remove("schema.json")
