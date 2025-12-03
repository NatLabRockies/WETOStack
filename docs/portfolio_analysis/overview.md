(technical_areas)=
# Portfolio Overview

The set of software under the WETO umbrella is detailed and categorized in the nested pages below.  There are many ways to subdivide the WETO Stack.  Some models are focused on a single turbine component, others on the whole turbine, others on the farm, and others on an even larger spatial scale.  Some models deal with the engineering, others on the cost.  For the engineering models, there is a range of fidelities from low-fidelity models intended for conceptual design, to the highest fidelity models that take hours or days to complete, and many mid-fidelity models that are common tools for industry.  Additionally, many larger models are comprised on individual modules that could be used as standalones.

An overview of the WETO Stack is provided in the image and table below, with more comprehensive listing and categorization in the nested pages.


## WETO Stack Mind Map

```{mermaid}
%%{init: { 'logLevel': 'debug', 'theme': 'forest' } }%%

mindmap
    root("WETO Software Portfolio")
        ps(Engineering-fidelity Physics Models)
            OpenFAST
            FAST.Farm
            RAFT
            OWENS

        hfm(High Fidelity Models)
            ExaWind
            ERF
            kynema
            pyNuMAD

        do(Design & Optimization)
            WEIS
            WISDEM
            WindSE
            HOPP
			   Ard

        ctrl(Controls)
            ROSCO
            FLORIS
            FLASC
            hercules

        ra(Resource Assessment)
            DW TAP

        cost(Cost Models)
            LandBOSSE
            ORBIT
            CORAL
            NRWAL

        wild(Wild Life Impact)
            SSRS

        om(Operation and Maintenance)
            OpenOA
            WOMBAT
```


## Engineering Model Categorization

|Application      |Design Exploration |Detailed Design   |Highly Resolving |
|:----------------|:------------------|:-----------------|:----------------|
|                 |                   |                  |                 |
|**Single Turbine** |WISDEM, RAFT (WEIS)|OpenFAST (WEIS), Owens  |ExaWind          |
|**Full Wind Plant**|FLORIS       (Ard) |FAST.Farm, WindSE (Ard) |ExaWind, ERF     |


