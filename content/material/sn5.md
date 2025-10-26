---
parent: Materials
title: SN5
nav_order: 7
layout: default
---

# SN 5 - Planning, Activity, Milestones

## 1. Lecture Questions

### 1.1 Planning Intro

1. **Mechanisms of Coordination**  
    Compare the three main coordination mechanisms — **hierarchies**, **shared representations**, and **communication** — giving an example of each in software teams.
2. **Purpose of Planning**  
    Beyond scheduling and budgeting, what are the key functions of planning in aligning people, work, and expectations?
3. **Qualities of a Good Plan**  
    The lecture says “a good plan is like a good program.” Explain this analogy using two of the listed plan properties (e.g., reliability, robustness, extensibility).
4. **Predictive vs. Agile Planning**  
    How do predictive and agile approaches differ in how they decide _what_, _when_, and _who_ — especially regarding task timing and team structure?
5. **Tracking and Reporting**  
    What are the main tracking artifacts used in predictive vs. agile planning, and what does each measure?
6. **Coordination and Control Philosophy**  
    Contrast the **control styles** and **goals** of predictive and agile approaches. How do they each achieve coordination?
7. **Sponsor-Oriented Planning**  
    What distinguishes a sponsor-oriented plan from a developer-oriented one? Why is this distinction important for project success?

### 1.2 Milestones

8. **Definition and Purpose**  
    What is a milestone in project planning, and how does it differ from a regular task or activity?
9. **Sponsor Perspective**  
    Why must a milestone be _verifiable_ and _relevant to the sponsor_? Give an example of each.
10. **Bad Milestone Examples**  
    Why are “Iteration 2 completed” or “Low-level design finished” considered poor milestone definitions?
11. **Outcome vs. Activity**  
    Summarize the key differences between **activity planning** and **milestone planning** in terms of focus, volatility, and required information.
12. **Sponsor-Oriented Plan**  
    In the example milestone table, what features make it a good sponsor-oriented plan rather than an internal schedule?
13. **Milestone Dependencies**  
    What does a **Finish-to-Finish (FF)** dependency between milestones mean, and how does it allow flexibility in scheduling?
14. **Hard vs. Soft Dates**  
    Explain the difference between a **hard date** and a **soft date** in milestone planning. Provide an example of each.
15. **Definition of Done (DoD)**  
    What is the role of the **Definition of Done** in verifying milestone completion, and how did it evolve from the ETVX model?
16. **Good Milestone Criteria**  
    What four attributes should every milestone meet (hint: Specific, Verifiable, Relevant, Timely)?  
    Why are these essential for project tracking?
17. **Resource and Effort Planning**  
    How is the **resource-use curve** used in milestone planning, and what factors should be considered when estimating total effort?

### 1.3 Activities

18. **Purpose of Activity Planning**  
    What is the main purpose of activity planning, and how does it convert milestones into an executable schedule?
19. **Visibility and Control**  
    What three aspects of project execution does activity planning make visible, and why are they essential for coordination?
20. **Pull vs. Push Mechanisms**  
    Explain the difference between the **pull** mechanism used in Scrum and the **push** mechanism used in plan-oriented approaches.  
    How do these mechanisms influence team autonomy and accountability?
21. **Scrum Planning Artifacts**  
    Which Scrum artifacts (e.g., Sprint Backlog, Task Board) support activity planning, and how do they help track progress daily?
22. **Rolling Wave Planning**  
    In plan-oriented projects, what is **rolling wave planning** and why is it used instead of defining all tasks at the project start?
23. **Dependency Types**  
    Describe the four primary dependency relationships: **Finish-to-Start (FS)**, **Finish-to-Finish (FF)**, **Start-to-Start (SS)**, and **Start-to-Finish (SF)**.  
    Give a practical software example for one of them.
24. **Definition and Role**  
    Define the **critical path**. Why do activities on this path have **zero float**, and how does this affect project risk?
25. **Calculations**  
    What is the difference between the **forward pass** and **backward pass** in CPM analysis?
26. **Float Concepts**  
    Distinguish between **total float** and **free float**. Which one is more useful for task-level decision making?
27. **Limitations of CPM (1)**  
    Why can CPM understate project completion time when there is **uncertainty** in activity durations?
28. **Limitations of CPM (2)**  
    What are the main assumptions behind CPM that make it unrealistic for complex software projects (e.g., fixed durations, independence, perfect estimates)?
29. **Limitations of CPM (3)**  
    Why can CPM fail to capture **iteration, rework, or overlapping tasks**, and how does this affect software project planning accuracy?
30. **Limitations of CPM (4)**  
    How does **merge path bias** distort CPM’s predicted finish date? Illustrate using a small example with parallel paths.
31. **Gantt Chart Complement**  
    How does a Gantt chart complement an activity network? What kind of additional information does it provide for managers and stakeholders?
32. **CCPM vs. CPM**  
    What additional factors does CCPM consider beyond task dependencies, and how does this change scheduling priorities?
33. **Merge Bias and Critical Chain**  
    Explain what **merge path bias** is and how **Critical Chain Project Management (CCPM)** helps mitigate its effects.
34. **Types of Buffers**  
    List and describe the three main types of buffers in CCPM — **project buffer**, **feeding buffer**, and **resource buffer**.  
    What purpose does each serve?
35. **Focus on Resources**  
    How does CCPM handle **resource contention** differently from CPM?
36. **Human Behavior Factors**  
    CCPM was designed partly to address “Parkinson’s Law” and “Student Syndrome.”  
    Explain what these mean and how CCPM mitigates their effects.
37. **Buffer Management**  
    In CCPM, how does monitoring **buffer consumption** help teams control progress and uncertainty during project execution?
38. **Advantages of CCPM**  
    Summarize three key advantages CCPM provides compared to traditional CPM under conditions of uncertainty and multitasking.
39. **Limitations of CCPM**  
    What assumptions in CCPM may not hold in practice (e.g., individual safety times, independence of task risks)?  
    How could these limit its effectiveness in real-world software projects?

---

## 2. Reading Questions

### 2.1 Andersen, “Warning: Activity Planning is Hazardous to Your Project’s Health!” (1996)

1. **Core Argument**  
    Why does Andersen argue that early, detailed **activity planning** is hazardous to a project’s health?
2. **Uniqueness of Projects**  
    How does the uniqueness of most projects make it impossible to define all activities meaningfully at the start?
3. **Four Illusions of Activity Planning**  
    Andersen lists several reasons why planners believe early activity plans are possible (e.g., reuse of past projects, technical focus).  
    Which of these assumptions are most problematic in software or organizational projects?
4. **Focus Shift**  
    According to Andersen, how does activity planning divert attention from the more important question of **results**?
5. **Defining Milestones**  
    How does Andersen redefine a **milestone**, and in what way does this differ from the common “end of activity” view?
6. **Result Paths and Logical Planning**  
    What are **result paths**, and how do they help represent multiple, interdependent project outcomes?
7. **Responsibility and Ownership**  
    How does a **milestone responsibility chart** improve accountability compared to assigning responsibility for individual tasks?
8. **Scheduling Without Activities**  
    How can project time schedules be created without first listing every activity?  
    What criteria does Andersen suggest for allocating time between milestones?
9. **Timing of Activity Planning**  
    Andersen does not reject activity planning completely.  
    When should it be performed, and why should it wait until close to milestone execution?
10. **Modern Relevance**  
    In what ways does Andersen’s milestone-based approach anticipate ideas later found in **Agile** or **iterative** project planning?

### 2.2 DSMC Scheduling Guide For Program Managers

11. **Purpose and Context**  
    What problem in traditional **activity planning** does the DSM method aim to solve in complex engineering or software projects?
12. **Representation of Dependencies**  
    How does the **Design Structure Matrix (DSM)** represent task dependencies differently from an **Activity Network (CPM or PERT)**?
13. **Iterative and Coupled Activities**  
    Why are **iterations and feedback loops** difficult to capture in classical activity networks?  
    How does DSM make these visible?
14. **Information Flow Perspective**  
    DSM treats development as an **information flow problem**.  
    How does this view help identify more realistic sequencing of activities?
15. **Matrix Partitioning and Sequencing**  
    What is the goal of **partitioning** the DSM, and how does it assist planners in organizing and sequencing interdependent tasks?
16. **Clusters and Subsystems**  
    DSM often reveals **clusters of highly coupled tasks**.  
    How can recognizing these clusters improve planning and coordination compared to traditional work breakdowns?
17. **Iterative Loops and Planning Trade-offs**  
    When DSM identifies feedback loops, what are the typical management responses?  
    (e.g., restructuring tasks, overlapping iterations, or planning “design cycles.”)
18. **Comparison to Critical Path Method (CPM)**  
    In what ways is DSM more suitable than CPM for planning **research, design, or software development** projects?
19. **Activity Sequencing Under Uncertainty**  
    How can DSM support **rolling-wave or adaptive planning**, aligning with modern agile practices?
20. **Integration with Project Tools**  
    How might DSM complement or improve upon traditional activity planning tools like **Gantt charts** or **network diagrams**?

### 2.3 Critical Chain Project Management: Coming to a Radar Screen Near You!” (Cutter IT Journal, 2003)

21. **Adoption Gap**  
    Why was Critical Chain Project Management (CCPM) initially slow to spread among project managers,  
    despite claims of major performance improvements?
22. **Limits of Activity Planning**  
    What key weaknesses of traditional activity-based planning does CCPM attempt to overcome?
23. **The “Hurry-Up-and-Wait” Cycle**  
    What behavioral patterns like _student syndrome_ and _Parkinson’s Law_ cause project safety margins to fail?
24. **Pooled Safety Concept**  
    How does pooling safety time into a **project buffer** make schedules shorter and more reliable?
25. **Behavioral Change**  
    What does “relay-runner behavior” mean in CCPM, and how does it differ from typical task management in Gantt-based planning?
26. **Resource Constraints**  
    In multiproject environments, why does **bad multitasking** drastically reduce throughput,  
    even when every resource appears “fully utilized”?
27. **Organizational Case**  
    In the Abbott Diagnostics Division example, what cultural and structural changes were needed  
    to make CCPM succeed across multiple sites?
28. **Agile Integration**  
    How did the Segway project combine **Agile iteration** with **Critical Chain scheduling**,  
    and what benefits resulted from this hybrid approach?
29. **Bridging the “Reality Gap”**  
    According to Robert Newbold, what is the difference between the **Old Game** and the **New Game** of project management,  
    and how does CCPM support the latter?
30. **Modern Relevance**  
    How does CCPM anticipate ideas now common in **Agile** and **Lean** methods — such as flow, focus, and reduced waste?

---