
# WETO Stack

This repository contains the source files for the documentation of the WETO Software Stack, 
a software portfolio wholly or partially supported by the Department of 
Energy's [Wind Energy Technologies Office (WETO)](https://www.energy.gov/eere/wind/wind-energy-technologies-office).  
The source files include an entry guide for new users, multiple listings and categorization of the software models, 
software quality characterization, and notes from the developer and user engagement that created the WETOStack content. 
See [nrel.github.io/WETOStack/](https://nrel.github.io/WETOStack/) for more information.

Note that while a "software stack" usually refers to a set of integrated software codes, the portfolio of codes 
in the WETO Stack is diverse and can be used individually or integrated, depending on the use case. 

Copyright 2024 Alliance for Sustainable Energy, LLC.

## Repository Contents

This repository contains a variety of tools for analyzing the WETO Software Stack as well as
reports from community engagement meetings and the source code for the documentation site.
The repository is organized as follows:

- `.github/`: Configuration files for GitHub Actions jobs and GitHub Pages builds
- `best_practices_report/`: LaTeX source files for the WETO Software Best Practices technical report
- `docs/`: Source files for most of the content on the WETO Software Stack website
- `entry_guide/`: Source files for the WETO Stack Entry Guide project
- `software_attributes/`: Database files (YAMLs) and analysis scripts for portfolio analysis

## Dependencies

The Python-based analysis scripts and Jupyter Book project dependencies are listed in
`requirements.txt`. These can be installed with `pip`:

```bash
pip install -r requirements.txt`
```

The entry guide project is built with Node Package Manager (`npm`), and the dependencies are
listed in `entry_guide/package.json`. After installing `npm`, the dependencies are
installed by running the install command within the entry guide directory:

```bash
cd wetostack/entry_guide/
npm install
```

## Building the Website

The WETO Software Stack website consists of two distinct components:
- Jupyter Book project that creates the primary structure and the majority of the content
- WETO Stack Entry Guide implemented with VueJS

The Entry Guide should be built first, copied into the Jupyter Book project directory,
and then the Jupyter Book project can be compiled. Refer to the
[deploy_pages](https://github.com/NREL/WETOStack/blob/main/.github/workflows/deploy-pages.yaml)
GitHub Actions workflow for more information.

**Note:** The Jupyter Book table of contents links to the Entry Guide via a web URL. When
building the documentation locally, you should change the web URL for the Entry Guide in the
table of contents to point to the Entry Guide `index.html` file locally.

### Building the Entry Guide VueJS Project

The Entry Guide uses [VueJS](https://vuejs.org), [VueFlow](https://vueflow.dev),
[DagreJS](https://github.com/dagrejs/dagre), and a few other libraries in the TypeScript and
Vue ecosystems.
[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) is required to
compile the Entry Guide project and install the dependencies.

The Entry Guide can be compiled as production quality or development quality.
During active development, the development build is highly recommended as it provides a
hot reload capability where changes made to the project contents are automatically recompiled
and an open browser window will automatically render the changes.
Modifications to the project configuration will not be automatically compiled.

To compile the Entry Guide in development mode, move into the `entry_guide/` directory
and run the dev-build command:

```bash
cd wetostack/entry_guide/
npm run dev

# Terminal output:
#  VITE v6.2.2  ready in 200 ms
#
#  ➜  Local:   http://localhost:5173/
#  ➜  Network: use --host to expose
#  ➜  press h + enter to show help
```
This build process creates a local server accessible through the local URL shown
(`localhost` + port).
As changes are made to the source, the running build process automatically rebuilds.
If there are errors in the code, the terminal window will show them.
When they're fixed, the terminal will automatically rebuild and show the local URL again.

To do a production build, run the following command:

```bash
npm run build

# Terminal output:
# > entry_guide@0.0.0 build
# > vue-tsc -b && vite build
# 
# vite v6.2.2 building for production...
# ✓ 120 modules transformed.
# dist/index.html                   0.48 kB │ gzip:  0.32 kB
# dist/assets/index-C8-A469-.css    3.47 kB │ gzip:  1.19 kB
# dist/assets/index-DjNIX96g.js   298.55 kB │ gzip: 99.24 kB
# ✓ built in 616ms
```
The compiled files are put into the `entry_guide/dist/` directory. From there, the app can be
opened into a browser by opening `entry_guide/dist/index.html`.

Finally, the Entry Guide is included in the WETO Software Stack website by copying the
contents of the `dist` directory into `weto_stack/docs/_static/entry_guide`. Note that
the Jupyter Book project table of contents must be modified to point to the local path
to the Entry Guide's `index.html` file rather than the web URL that is set for the
deployed project.

### Building the Docs

The site is built using [Sphinx](https://www.sphinx-doc.org) with
[pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io).
To build the site, run the following command:

```bash
pip install -r requirements.txt

cd docs/

sphinx-build -b html . _build/html
```

The output will be at `docs/_build/html/index.html`.

Note that the `docs/_build` folder must be removed and a rebuild completed if there are changes to
the `software_attributes/database/` YAML files.

## Entry Guide Project Description

The Entry Guide project is built with [VueJS](https://vuejs.org) as a reactive front-end framework.
The language is TypeScript and a VueJS domain-specific language that is essentially HTML.
The Vue files have the `.vue` suffix and define the Vue components with three sections:

- script
- template
- style (optional)

The script section is TypeScript and defines the data and functions used to create the content
laid out in the template section.
The style section optionally contains CSS styling for the elements in the template section.

The app is structured as a main page with tabs that contain [VueFlow](https://vueflow.dev)
canvases that render the graphs.
The main entry point is `App.vue`, and it loads the tab elements and lays out the main page.
The tab bar itself (the row of tab names on the main page) is described in `Tabs.vue`.
The tab elements are defined in corresponding files in `tabs/`.
The tab elements load their corresponding graph data from `data/` and then create their layout
using the `layout` function from `Layout.ts` which uses [DagreJS](https://github.com/dagrejs/dagre)
to systematically produce the layout.
Some additional functionality for the graph reactivity is available in `utils.ts` and configured
in the tab elements.
All tabs are essentially the same code and structure but load a different data file.

The graph data are defined as nodes and edges.
A node can be either a `type: decision` or `type: tool`.
When the graph traversal routines reach a tool node, they stop traversing.
Decision-type nodes have "a" and "b" attributes to provide the switch functionality.
The edges must be defined as a source, target, and label.
The source and target are node IDs, and the label is either `a` or `b` to denote which state
of the switch activates the edge.

New tabs can be added by copying an existing tab and data file to new files.
The data should be updated as appropriate.
Then, the tab element should be imported in `App.vue` and added as an element to the
`tabList` variable.
From there, the app should include the new tab in the existing structure.

## License

WETO Software Stack is licensed under Apache 2.0.
