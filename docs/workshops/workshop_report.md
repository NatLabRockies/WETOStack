(workshop_report_top)=
# 2023 Workshop Report

The first portfolio coordination workshop for wind energy software model owners, sponsored by the Wind Energy Technology Office (WETO) within the U.S. Department of Energy (DOE), was held September 7, 2023, at the Golden Campus of the National Renewable Energy Laboratory (NLR).  The workshop technical program was organized by Rafael Mudafort, Pietro Bortolotti, and Garrett Barter, as part of the 
*Holistic, Multi-Fidelity Wind Farm Design Optimization and Model Coordination* project, with the vision that a similar event will be held annually.  Significant thanks and appreciation to Ashley Shamus and Kara Bethea for their help in the planning and logistics of the workshop day.

This report summarizes the workshop sessions, presentations, and discussion highlights.  The material is presented in the chronological order of the [agenda](workshop_agenda).  All notes, presentations, recordings, and transcripts of the workshop are archived and digitally available upon request.

## Session 1: DOE HQ Perspective on WETO-Funded Software

After opening comments from the workshop organizer, Rafael Mudafort, the first session of the workshop featured remarks from Ben Hallissy, the WETO Program Manager who oversees the majority of the projects that develop open-source software.  Ben first explained what he considers to be the "WETO Software Stack", which is any software that advances the mission of WETO that is written by a WETO-funded laboratory, another federal agency, or university subcontract.  More succinctly, the stack ideally seeks "A tool or software package (including any user or theory documentation) that is used directly, benchmarked against as a trusted resource, or even stripped for parts (algorithms) to advance the mission of WETO at low to no recurring cost".  Ben explicitly stated that WETO views software models as a key engine of research, both internally and in the larger community, and a tool to make key policy decisions.

For the laboratories, WETO sees the software stack as constantly in development via directly funded (AOP) projects, or even industry-funded or internally-funded projects where the software will have a role for DOE down the line.  The most helpful materials for WETO in managing projects that oversee a software tool are clear road-maps and capabilities, with identified connections across tools, and open communication about resource needs.  At the same time, there is recognition of the challenges that arise in a research-environment.  This includes long-term sustainability (avoiding a "lifetime mortgage"), achieving usability by generic wind community members, the misalignment of time spent on software engineering versus a researcher's career objectives, the overlap in code capabilities across laboratories, among other points.

Ben made clear that WETO wants to be a partner in the long-term objectives of the workshop to achieve better software coordination and adoption of software development best practices.  Two big ideas that Ben offered to kick off the larger discussion include:

  + A "tiered system" for WETO software tools that come with different standards and expectations of software quality and process.
  + Encouraging the workshop attendees to brainstorm ideas for externally funded user support, either through small contracts or even a non-profit entity that is responsible to much of the day-to-day software maintenance and user engagement.  This last approach has been used by WETO over its history before for other community engagements (utilities, standards, wildlife, etc).

The discussion that followed covered the following themes:

  + Other DOE offices have been wrestling with this topic for a while and might have something to offer.  The Advanced Scientific Computing Research (ASCR) office is very focused on software sustainability and its proposal guidelines and AOPs have sections and expectations on software quality.  If WETO wants to make this a priority, it has to be part of the core fabric of a project too.  The Water Power Technology Office (WPTO) also started a portfolio coordination effort and have some good lessons learned.
  + Good software quality requires funding and the alignment of WETO program managers and laboratory PIs about priorities and costs.  Most often, project milestones and deliverables are research oriented, just like staff career incentives, so time spent of software quality (tests, documentation, usability) is put to the side when schedules or budgets are tight.  If there is nobody to pay for it upfront, then the users and developers pay for it down the road in the extra time required to answer questions and fix issues.
  + Willingness to support software quality and long-term maintenance is easier to come by with evidence of the community impact of these tools.  With GitHub delivery, it can be difficult to track users and downloads in the same way that other delivery methods might track traffic.  The shortcoming is felt more strongly by the fact that not all users are equal, meaning usage of the WETO software stack by industry is a sign of the highest level of impact.  Regardless, better user tracking will need to be part of the overall software best practices.


## Session 2: WETO Portfolio Overview

The second session of the day was to identify major overlaps or gaps in the WETO software stack, which could then inform future funding investments.  Garrett Barter presented an overview of the new WETO [model portfolio dashboard](https://a2e.energy.gov/code/repo), as well as the inter-dependencies between models such as depicted in the [](technical_areas).  Some of the portfolio overview slides that NLR has used in the past were also shown, with an aspiration that some of this material will migrate to the dashboard, while also acknowledging that there will still be a need for Powerpoint-based depictions of the portfolio.  The workshop participants had some helpful suggestions for additional comparison tables to include on the dashboard.

The overview presentation was followed by individual "lightning talks" intended to introduce the audience to segments or perspectives on the portfolio that might be less familiar:

  + Matt Shields: Cost model portfolio
  + Ann Almgren: High Fidelity Modeling
  + Emmanuel Branlard: OpenFAST and its family of tools
  + Paul Fleming: Control and Hybrids models
  + Pietro Bortolotti: Design optimization tools
  
After the presentations, the attendees divided up into breakout groups to facilitate deeper and more individualized conversation.  Across the breakout groups, the comments are categorized under the following themes:

**Portfolio Depiction**
  + In addition to what has been shown, it would help to know the intended computing platform for each model and whether it is GPU-ready
  + The dashboard Mindmap should have an "Operations and Analysis" section
  + The dashboard should include common workflows as that is often a struggle for users.  They think "I need to do X- which models do I use to get there".  There might be more than one way to get the answer within the portfolio.
  + The PNNL [Pinacles](https://github.com/pnnl/pinacles) code should probably be included
  + It would help to capture the pre- and post-processing ecosystem for a number of these tools
  + A number of new models and new project proposals are "frameworks" that wrap multiple models together with some additional code.  These are harder to describe from the dashboard or portfolio perspective and are also hard to maintain.
  + Should key datasets be a part of the dashboard?  Sometimes these are critical inputs or near-models in their own right with an ecosystem of data manipulation utilities.
  + It is one thing to list some tool characteristics, but the the limits of where one tool ends and another begins in capability or fidelity is not clear.  It also isn't clear how to easily capture this.

**Connections Between Models**
  + There should be a stronger connection between the cost models and the engineering models.  WISDEM has the strongest connection, but it could be better, and in some projects FLORIS has been connected as well.  Maybe modules in those two tools could be a guide or used directly in other models.
  + Multi-fidelity integration of the higher-fidelity tools into other tools is difficult because they have a complex list of dependencies and are intended for specialized HPC environments.  AI/ML could help as a surrogate model and bridge to higher-fidelity integration.
  + The WETO software models should be built with modularity in mind, as that provides entry points and easier integration into other models, even if they are used in the "stripped for parts" approach
  + More connections between models could be made if all models had better defined input and output lists (at the minimum) or schema (preferred).  Common data structures for outputs would also be preferred (e.g. NetCDF or HDF5 or Zarr)
  + Tighter integration could happen with intentional build out of APIs.  Most of the models are built with a narrow workflow in mind and the developers are not thinking that the code they are writing could be used as a library for a different purpose.  Python wrappers for compiled code make this even easier.

**Portfolio Overlap**
  + There are multiple tools that can do LES with actuator lines.  Most prominent is ERF (hasn't officially added actuator methods yet) and AMR-Wind.  ERF is compressible and AMR-Wind is incompressible.  WindSE also has capabilities in this area.
  + There is likely more overlap in pre- and post-processing tools, which often are doing similar things with similar data.
  + There is likely overlap that could be leveraged outside of WETO.  This could be with other EERE offices, such as known overlap in hydrodynamics modeling with WPTO, or university open-source tools.

**Gaps**
  + There is a gap in the lack of a strong workflow for blade and turbine structural analysis.  The aerodynamics analysis workflow, at all levels of fidelity, is well defined.  This is not the case for structural analysis.  Beamdyn is an example where the workflow would significantly benefit from automation.
  + The portfolio would benefit from a comprehensive benchmarking effort that captures the verification and validation of all tools.  This would benefit external users and demonstrate cohesiveness of the portfolio.
  + There is no clear support for cloud delivery of the models in the portfolio.  This could help reach new groups of users and address issues of usability by simplifying workflows.
  + There is no avenue for industry input into the portfolio as a whole.  Individual models or projects have varied levels of engagement with industry.  Standardizing this engagement and allowing industry to provide input on the whole portfolio would be beneficial.


## Session 3: Software Best Practices

Following lunch, Rafael Mudafort presented his perspective on best practices for research-driven scientific software.  This was a slide-based version of [this](bestpractices) material, so it is not summarized again here.  The presentation was followed by a breakout session where the groups brainstormed barriers and potential solutions to instituting the best practices with each of the WETO model development teams.  The comments in the breakout groups have been categorized under the following labels.  Some of the comments describe barriers to creating high quality software and others make recommendations.  There were strong voices in the groups, with some advocating best practices guidelines for all models and others resisting processes that would remove the flexibility to gauge the need for tests and documentation based on the project tasks.

**Scientific Software Challenges**
  + *(Barrier)* Models in the WETO Software Stack are typically "midsize" which means they are too big and mature for developers to move fast with frequent refactoring and minimal overhead.  At the same time, they can feel too small for extensive infrastructure and strict development guides and processes.
  + *(Barrier)* Software to enable cutting edge research is by definition complex.  Problems that arise can be quite complex and take more time than expected to debug.  Testing the software can also be a challenge, especially for high-fidelity models that depend on many libraries and are designed for GPUs.  It is both expensive and time consuming to test at scale, leading to long development and debug cycle times.

**Staffing Dynamics**
  + *(Barrier)* Career progression for laboratory researchers incentivizes journal publications, which places on emphasis on research-grade software that has many advanced features, but might lack all other characteristics of sustainability and usability.
  + *(Barrier)* Even for software that is meant for cutting edge research, much of the codebase deals with managing data, managing inputs, managing parallel processing, and other tasks which can feel like recreating the wheel.  On top of writing tests and documentation for these related functions, the tasks can feel a bit dry and a poor investment of time if the ultimate goal is journal-quality research.
  + *(Recommendation)* At LBNL, there is a career title and track for research software engineer where the emphasis is on software output (releases, tests, bugs or issues addressed, documentation) and not journal publications.  This is likely true at PNNL as well.  NLR seems a little behind in this regard.
  + *(Barrier)* When new staff join the laboratories and are put on the projects that develop WETO software, they are likely not coming from a software development or computer science background and are expected to learn those skills on the job.  There is no intensive or dedicated training in topics such as software architecture or GPU programming or git workflows or related best practices concepts.
  + *(Recommendation)* Training shouldn't just be focused on new staff.  As the best practices become more formalized, existing staff would also benefit from dedicated training too.
  + *(Barrier)* Researchers at all laboratories tend to be spread thin across multiple projects so that they are almost always multitasking.  This means they tend to prioritize on the most critical activities to meet project milestones and deliverables, which rarely target software quality.  Time intensive tasks such as writing tests and documentation are therefore always at the bottom of the priority list.
  + *(Barrier)* Researchers are by nature curious and often chasing fresh topics after spending years on a particular project.  They might also be directed by their management to shift focus.  This means that software teams sometimes lack the continuity and institutional knowledge required to address issues that arise in older code.

**Project Management**
  + *(Barrier)* Projects often over-plan for an ideal software solution instead of first working to a minimum viable product (MVP)
  + *(Barrier)* Projects seem too bound to the thinking in a proposal than can be 2+ years out of date, and lack the ability to pivot and adjust milestones and development task sequences based on staffing or team dynamics.
  + *(Barrier)* The stakes and severity of AOP milestones drives software technical debt as milestones are rarely software focused, usually they are capability focused and encourage all project members to concentrate on publishable demonstrations instead of usability and sustainability.
  + *(Barrier)* The time and effort required for quality software is not well understood among lab researchers, so projects are budgeted for the technical effort to develop a new capability.  There isn't usually enough time or funds to support testing, documentation, or user support.
  + *(Barrier)* Some tools are funded by multiple projects with competing requirements, time constraints, external politics, and long term visions.
  + *(Recommendation)* High quality software needs to start in the AOP with specific milestones and standards called out.  This is a burden that should be equally shared by WETO and the laboratory PIs.
  + *(Recommendation)* DOE should have more mutable and flexible milestones for software capabilities.
  + *(Recommendation)* New code capabilities must be tested and publicly available (merged to the primary repository & branch) to be declared "done" by milestone standards to avoid technical debt.


**Best Practice Guidelines**
  + *(Barrier)* It will be difficult for the Best Practices guide to strike the right balance of strict adherence vs flexibility for a situation.  If the processes are categorically strict, it can cost the project time, funds, and morale.  If they are too flexible, then they will be ignored and software quality will suffer.
  + *(Barrier)* There is already a broad spectrum of code culture across the WETO stack depending on the nature of the project and personalities of the project teams.  It will be hard to unify everyone under a single best practices guide.
  + *(Recommendation)* The Best Practices should be presented as a benefit so that all developers understand the long-term payoff for hard work on continuous integration test suites.
  + *(Recommendation)* One item that isn't mentioned in the best practices is for Github Pull Requests (PR) to be small, singular in scope, and easy to review.  Very large PRs are infeasible for review and get approved even when there are likely issues that otherwise would be caught in smaller reviews.  Smaller code blocks and functions are also easier to test than large, procedural code blocks.
  + *(Recommendation)* Code reviews should be prompt (within hours or at most a couple of days), since small PRs require quick approval in order to move onto the next development step.
  + *(Barrier)* There is not clear guidance for when tests are good or just repeating bug-prone model code and thereby giving a false sense of rigor.
  + *(Barrier)* It is unclear how good coding standards can be enforced.  A team member that is spread too thin might ask forgiveness for a PR that lacks tests and documentation.  Would there be negative consequences for this?
  
**Team Development Dynamics**
  + *(Recommendation)* A benevolent dictator at the head of each project tends to work the best.  Then there is a single voice and style that sets the expectation for software processes and quality throughout the team.  Otherwise, everyone will have a different standard for when a code, tests, and documentation are good enough.
  + *(Recommendation)* All software development teams should have a succession plan for their benevolent dictator.  Too often a software model becomes stale and unsupported once its champion moves on.
  + *(Recommendation)* Occasional or regular code sprints (i.e. "Hackathons") are a great way to build team camaraderie, train junior staff, overcome the limited mental focus of multitasking on normal days, and make otherwise dry software development tasks more enjoyable in a group setting.



## Session 4: Model Coordination

The final session of the day featured a group discussion of tangible activities that WETO, and specifically the *Holistic, Multi-Fidelity Wind Farm Design Optimization and Model Coordination* project, can do to further the impact of the WETO software portfolio and better coordinate capabilities and software practices among the developers.  This conversation was facilitated by Pietro Bortolotti, who set the stage for the group discussion by first describing the current work plan in the project.  This includes this first workshop as focused on the model owners, but the next workshop will likely include model users to get their perspective on similar questions of usability, portfolio gaps, etc.

The group brainstormed some ideas for project activities and priorities:

  + Defining common guidelines and recommended practices, which will likely evolve over time, and obtain buy in from WETO to encourage adherence by all developers.
  + Create training material for new staff that brings them up-to-speed on the best practices.  The training material might go further and help guide projects for which best practices to adopt at various stages of model maturity.
  + Work with model owners to create tutorials and software development road-maps for each tool.
  + Coordinate with WPTO and leverage existing tools to monitor usage, impact, and software quality.
  + Delineate avenues to fund software maintenance externally, such collaborations with industry, or adopting something similar to WPTO's "Teamer" system.
  + Hire an external consultant to review the projects and codes for recommendations
  + Develop software trainings across the portfolio. These should target external but also internal users. These events often help improve documentation and quality and improve the marketing.
  + Develop a portfolio-wide marketing and public outreach strategy that sells them as a family of tools instead of individual solutions for individual needs.  Other DOE offices may have lessons here.
  + Consolidate tools across the portfolio. This would help the marketing to WETO and would help WETO advertise the value of their research. It would also help public outreach.
  + Adopt approaches for product management, including cataloging and engaging the pool of users
  + Share benchmarks across a family of tools as many will had similar verification and validation approaches.
  + Identify connections to software tools or utilities that sit outside the WETO umbrella.

## Attendees

The attendees of the workshop were:

  + Andy Platt, NLR
  + Ann Almgren, LBNL
  + Ashesh Sharma, NLR
  + Chris Bay, NLR
  + Dan Zalkind, NLR
  + Dmitry Duplyakin, NLR
  + Eliot Quon, NLR
  + Emmanuel Branlard, NLR
  + Ernesto Camarena, SNL
  + Ethan Young, NLR
  + Garrett Barter, NLR
  + Jason Fields, NLR
  + Jason Jonkman, NLR
  + Jordan Perr-Sauer, NLR
  + Kelley Ruehl, SNL
  + Matt Shields, NLR
  + Mike Sprague, NLR
  + Misha Sinner, NLR
  + Paul Fleming, NLR
  + Paul Veers, NLR
  + Pietro Bortolotti, NLR
  + Rafael Mudafort, NLR
  + Rob Hammond, NLR
