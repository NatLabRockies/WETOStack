(workshop_2024)=
# 2024 User Workshops

**This series of workshops has passed. See [](workshop_recaps) and [](workshop_2024_report_top) for more info.**

The Holistic Modeling Portfolio Coordination Project is hosting a series of workshops in June 2024
to discuss the current state and future direction of the WETO Software Stack.
Individual workshops will be held for different topic areas covering a subset of software
within the WETO Software Stack.
The workshops will be conducted via Microsoft Teams at the dates and times listed below,
and registration is required.
Anyone interested is encouraged to attend, and the target audience is current and prospective
users of WETO software.

| Date | Time | Topic Area | Relevant Software |
| ---- | ---- | ---------- | ----------------- |
| June 10 | 7-9 am MDT | Systems Engineering | WISDEM, WEIS, WindSE, pyNuMAD, SONATA |
| June 12 | 8-10 am MDT | TEA, cost modeling | ORBIT, LandBOSSE, WOMBAT, NRWAL, CORAL |
| June 18 | 7-9 am MDT | Controls | FLORIS, FLASC, Hercules, OpenOA |
| June 20 | 7-9 am MDT | OpenFAST+ | OpenFAST, FAST.Farm, ROSCO, and associated tools |
| Nov 13 | 10 am - 12 pm MST | HFM | ExaWind, AMR-Wind, Nalu-Wind, OpenTurbine, ERF |

`````{admonition} Contact
:class: tip
Please contact Rafael Mudafort (rafael.mudafort@nlr.gov) with any questions.
`````

<!-- `````{admonition} Schedule Changes
:class: warning

- The **HFM workshop** (AMR Wind, Nalu Wind, ERF, OpenTurbine) originally scheduled for June 13 has been postponed, and the rescheduled date will be announced soon.
- **WindSE** was initially included in the HFM workshop, but it has been moved to the Systems Engineering workshop on June 10.
- **OpenOA** was initially included in the TEA / Cost Modeling workshop, but it has been moved to the Controls workshop on June 18.
````` -->

## Registration

**To register, complete this form: [WETO Software Stack workshop registration](https://docs.google.com/forms/d/1Pbk34YmhjRBEsnPteqY8OLgjxsq82TkWULCVhABwuHY/edit).**

Prior to the workshop, registered participants will receive an email with a link
to the Microsoft Teams meeting.

## Workshop Format

Each workshop will start with an overview of the WETO Software Stack followed by
a high-level description of the specific software and capabilities for the relevant
topic area.
A 30-minute portion will be reserved for community feedback and discussion with model owners.
A sample agenda is provided below, but specific agendas will vary.

| Time Slot | Duration | Topic |
| --------- | -------- | ----- |
| 0:00 - 0:05 |  5 min | Welcome and intro |
| 0:05 - 0:15 | 10 min | Intro to Portfolio Coordination Project, WETO Software Stack overview |
| 0:15 - 0:30 | 15 min | WETO Software Stack Q&A |
| 0:30 - 1:20 | 50 min | Model introductions, capabilities and workflow demo, future roadmap |
| 1:20        |  2 min | Poll on usability issues, voting for roadmap priorities |
| 1:20 - 1:50 | 30 min | Community discussion, Q&A |
| 1:50 -  end | 10 min | Outro and Methods for community engagement |

The software included in the workshops are organized slightly differently than the [](software_listing).
Rather than organizing the workshops by the thing that each software does, the workshops are
organized by the technical area in which each software is used.
This allows the workshop attendees to have a more common interest in the software being discussed.

```{mermaid}
%%{init: { 'logLevel': 'debug', 'theme': 'default' , 'themeVariables': {'git0': '#CF784B', 'cScale1': '#B5B867', 'cScale2': '#FFEA59', 'cScale3': '#B7DBDB', 'cScale4': '#335B8E', 'cScale5': '#6CA18F'} }  }%%

mindmap
    root("WETO Software Portfolio")
        ps(Systems Engineering)
            WEIS
            WISDEM
            WindSE
            pyNuMAD

        hfm(High Fidelity Modeling)
            AMR Wind
            Nalu Wind
            OpenTurbine
            ERF

        ctrl(Wind Farm Controls and Analysis)
            FLORIS
            FLASC
            hercules
            OpenOA

        cost(TEA & Cost Models)
            LandBOSSE
            ORBIT
            CORAL
            NRWAL
            WOMBAT

        do(OpenFAST+)
            OpenFAST
            FAST.Farm
            ROSCO
            openfast_toolbox
```

(workshop_recaps)=
## Recordings and Slides

The workshop recordings are hosted on [YouTube](https://www.youtube.com/playlist?list=PL6ksUtsZI1dwRXeWFCmJT6cEN1xijsHJz),
and they are embedded on this page.
A PDF version of the slides that were presented at each workshop are included here, as well.

### Systems Engineering

The sections presented in this workshop are:
- [WETO Software Stack](https://natlabrockies.github.io/WETOStack) by Rafael Mudafort
- [WISDEM](https://github.com/WISDEM/WISDEM) by Pietro Bortolotti
- [WEIS](https://github.com/WISDEM/WEIS) by Dan Zalkind
- [pyNuMAD](https://github.com/sandialabs/pyNuMAD) by Ernesto Camarena
- [WindSE](https://github.com/NatLabRockies/WindSE) by Jeff Allen and Ethan Young

Garrett Barter co-hosted the workshop and facilitated the discussion.

{download}`Click here to download the slides.<../_static/UserWorkshops2024_SE.pdf>`

```{youtube} urab_dN12Ws
```

### TEA and Cost Modeling

The sections presented in this workshop are:
- [WETO Software Stack](https://natlabrockies.github.io/WETOStack) by Rafael Mudafort
- [LandBOSSE](https://github.com/WISDEM/LandBOSSE) by Rob Hammond
- [ORBIT](https://github.com/WISDEM/ORBIT) by Nick Riccobono
- [CORAL](https://github.com/NatLabRockies/CORAL) by Sophie Bredenkamp
- [WOMBAT](https://github.com/WISDEM/WOMBAT) by Rob Hammond
- [WAVES](https://github.com/NatLabRockies/WAVES) by Rob Hammond
- [NRWAL](https://github.com/NatLabRockies/NRWAL) by Rob Hammond

Garrett Barter co-hosted the workshop and facilitated the discussion.

{download}`Click here to download the slides.<../_static/UserWorkshops2024_TEA.pdf>`

```{youtube} keT7KcBHmgM
```

### Wind Farm Controls and Analysis

The sections presented in this workshop are:
- [WETO Software Stack](https://natlabrockies.github.io/WETOStack) by Rafael Mudafort
- [FLORIS](https://github.com/NatLabRockies/FLORIS) by Misha Sinner
- [FLASC](https://github.com/NatLabRockies/FLASC) by Paul Fleming
- [OpenOA](https://github.com/NatLabRockies/OpenOA) by Eric Simley and Rob Hammond
- [Hercules](https://github.com/NatLabRockies/Hercules) by Misha Sinner and Gen Starke

Garrett Barter co-hosted the workshop and facilitated the discussion.

{download}`Click here to download the slides.<../_static/UserWorkshops2024_WFCA.pdf>`

```{youtube} f-w6whxIBrA
```

### OpenFAST Ecosystem

The sections presented in this workshop are:
- [WETO Software Stack](https://natlabrockies.github.io/WETOStack) by Rafael Mudafort
- [OpenFAST](https://github.com/NatLabRockies/FLORIS) by Jason Jonkman
- [ACDC](https://github.com/NatLabRockies/FLASC) by Derek Slaughter
- [ROSCO](https://github.com/NatLabRockies/OpenOA) by Dan Zalkind

Garrett Barter co-hosted the workshop and facilitated the discussion.

{download}`Click here to download the slides.<../_static/UserWorkshops2024_OpenFAST.pdf>`

```{youtube} cadiJ4_FGXc
```

### High Fidelity Modeling

The sections presented in this workshop are:
- [WETO Software Stack](https://natlabrockies.github.io/WETOStack) by Rafael Mudafort
- [ExaWind](https://exawind.github.io) by Mike Sprague
- [ExaWind:OpenTurbine](https://github.com/exawind/openturbine) by Mike Sprague
- [ExaWind:AMR-Wind](https://github.com/exawind/amr-wind) by Michael Kuhn
- [ExaWind Software and Performance](https://exawind.github.io/amr-wind/walkthrough/compiling.html) by Jon Rood and Marc Henry de Frahan
- [Energy Resource and Forecasting (ERF)](https://github.com/erf-model/erf) by Eliot Quon

Garrett Barter co-hosted the workshop and facilitated the discussion.

{download}`Click here to download the slides.<../_static/UserWorkshops2024_HFM.pdf>`

```{youtube} N7oH9IG3occ
```
