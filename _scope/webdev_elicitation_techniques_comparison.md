---
title: Comparative Analysis of Requirement Elicitation Techniques in Web Applications Development
author: Marina Ivanova
layout: page
permalink: /template/
---

# Title: Comparative Analysis of Requirement Elicitation Techniques in Web Applications Development

*Author: Marina Ivanova, Innopolis University, Innopolis, Russia  (<m.ivanova@innopolis.university>) 👤*

*Year: 2024*

### Abstract 📝

This paper provides an overview and analysis of requirement elicitation techniques in web application development, focusing on their effectiveness in addressing unique challenges of the domain. It identifies key requirements relevant to web systems, including navigational and content requirements, non-functional quality attributes such as usability, performance, and availability. Additionally, the study explores challenges like requirements volatility, stakeholder communication gaps, and rapid technological changes. Through a comparative analysis of widely used techniques, such as interviews, prototyping, JAD, and use case modeling, the paper highlights their strengths and limitations in capturing comprehensive and adaptable requirements. The findings underscore the importance of aligning elicitation approaches with the dynamic nature of web development and suggest directions for future research, including the techniques scope expansion and empirical validation of theoretical frameworks.


*Keywords — requirements elicitation, requirements engineering techniques, web applications, web development.*


<div id="Intro"></div>

## 1. Introduction 📖

### 1.1 Motivation 💡

With respect to the continuous demand for user-oriented web applications, the ability to accurately identify web and, in particular, frontend requirements is increasing significantly. The nature of web interfaces playing the role of middleware between users and the variety of different services and software causes their diverse applications and requirements, while unified in the specifics of the online systems. Moreover, the usability aspect, as usually implied, but not verbally defined non-functional requirement can be left uncaptured or uncharacterized, lacking measurable acceptance criterias {% cite rivero_approach_2013 %}. Efficient requirement gathering processes can help to shorten the development cycle and achieve better alignment with user expectations. In this context, it is highly important for the project success to choose the best-fit requirements gathering techniques, that are able to capture the requirements, most-likely to be met in web development. 

### 1.2 Problem Statement ❓

Quality requirement elicitation lays the foundation for development reliable, user-centric applications. Effective requirement elicitation ensures that developers understand user needs, system functionality, and performance standards, directly impacting the quality and success of the final product. The outcomes of this process highly depends on the choice of relevant elicitation technique, that is suitable for product context and is able to effectively overcome typical challenges in this domain, such as communication gaps between stakeholders and developers, constantly changing user expectations, and difficulties in capturing unstated or implicit requirements. The fast-paced evolution of web technologies and diverse user environments add layers of complexity and obstacles to the requirements gathering process. In this paper, I aim to address these challenges and identify the more suitable requirements elicitation approaches to navigate through the barriers and complications of web domain.

The objective of the research can be formulated via the GQM Goal Template. This study aims:

> **to analyse**	existing requirements elicitation techniques \
> **for the purpose of**	their comparative assessment \
> **with respect to**	their ability to capture relevant requirements and overcome typical challanges \
> **from the viewpoint of**	software engineer \
> **in the context of**	web applications development.

The following research questions were derived from this goal:

> **RQ1:** Which requirements are relevant in the context of web applications development? \
> **RQ2:** What challenges does the web domain present for the requirement engineering? \
> **RQ3:** Which requirements elicitation techniques should be chosen for the comparative analysis? \
> **RQ4:** Which of the chosen requirements elicitation techniques are the most and less useful to capture relevant in web requirements and avoid identified challenges?

### 1.3 Paper Structure 📑

This paper generally follows the IMRAD structure. <a href="#Intro">Section I</a> discusses the motivation, states the problem and goal, that this research aims to solve. <a href="#RelatedWorks">Section II</a> covers the state of art in the domain of web applications requirements and describes the most relevant requirements, challenges and approaches in the field of web development, identified and suggested by the previous works. <a href="#Techniques">Section III</a> states the methodology for the comparative analysis, describes the conduction process of the techniques comparison and analyses chosen requirements elicitation techniques, their strong sides and drawbacks. <a href="#Analysis">Section IV</a>  presents outcomes of the analysis and acknowledges its limitations. <a href="#Discussion">Section V</a> formulates key findings and discusses the implications of the study. Finally, <a href="#Conclussion">Section VI</a> summarizes the work done and explores possibilities for the future work. 

<div id="RelatedWorks"></div>

## 2. Related Work 🔗

### 2.1 Requirements Elicitation Tools and Techniques

Requirement Elicitation is one of the initial steps in requirement engineering. The requirement engineering process is usually described as a five-stages system of activities {% cite sajjad_issues_2010 kotonya_requirements_1998 %}, that includes feasibility study, requirements elicitation and analysis, requirements specification, verification and validation, and, finally, requirements management. Some researchers ommit feasibility study and requirements management steps, or extract them into a sepate entities. Major focus of this study will be directed towards the requirement elicitation stage, however, it is necessary to menttion, that all of the requirements engineering activities are not separate processes, but a mechanisms, that exist and work in complex, therefore tightly coupled by their incomes and outcomes. While quality of the elicited requirements is one of the key factor to the requirements engineering process success {% cite sajjad_issues_2010 %}, the elicitation and overall results will depend on the techniques, frameworks and outcomes, chosen in the other activities as well.

Overall, requirement elicitation aims to explore the needs, requirements, desires and expectations of the stakeholders towards the system to be developed, identify the application functional and non-functional properties, limitations in order for it to be able to meet the intendent goal, purpose, and expectations. Elicitation success depends on the ability to comprehensively identify relevant for the project stakeholders, such as:

- customers;
- users of pre-existing system; 
- end users;
- employees; 
- maintainers; 
- government;
- physical, organizational, legislation environment;
- etc.,

and their needs. Having different background, stakeholders often have different, or even conflicting goals, thus, critically rising the necessity to include all of the stakeholders groups in the requirements gatherering process, while covering their role, domain knowledge, and influence on the project.

The sources of requirements are formed by stakeholders, however, may exist in the different forms: as knowledge, embedded in human beings (end users, customers, domain experts, focus groups, etc.) and as knowledge, embedded in the physical environment (system-as-is documentation, operational workflow, customer's specifications, government laws, etc.) {% cite zhang_effective_2007 %}. Umber et al. {% cite umber_requirements_2012 %} highlights that requirements engineer should ensure that the chosen elicitation approach effectively explores the present sources of requirements, considering both the available data and the process for acquiring the necessary knowledge. In terms of interaction approaches the requirements techniques are classified as {% cite zhang_effective_2007 sajjad_issues_2010 umber_requirements_2012 %} :

* Conversational methods (interviews, surveys, questionnaires, workshops, etc.) — techniques, that involve direct verbal communication and interaction with stakeholders, therefore also refered as verbal methods. As a natural mean to express needs and ideas, conversational methods are effective to understand and develop problems {% cite zhang_effective_2007 %}, however the natural language, in which the requirements are convaid, may create interpretational issues, because words can be understood variably by individuals depending on the context and their backgrounds {% cite umber_requirements_2012 %}.
* Observational methods (observations, social analysis, ethnographic studies, ideation, etc.) — techniques, that explore unverbolized knowledge about system domain through observing human activities. While developing deep and rich understanding of application domain, including apparent for stakeholders, but difficult to verbalize, tacit requirements {% cite zhang_effective_2007 %}, they require much longer time periods in comparison wth other methods, as well as sensitivity and responsiveness to the physical environment in order to not only observe a work context, but analyze and understand stakeholders perception of it {% cite zhang_effective_2007 umber_requirements_2012 %}. Observational methods can be used for complex scenarios, but they do not tell the ways of how the workflow could be improved.
* Analytic methods (documentation analysis, requirements reuse, laddering, etc.) — techniques, that gather requirements by exploring the existing knowledge (such as expertises, information about regulations or legacy product) and conducting series of deduction to extract not directly expressed through requests or behavior knowledge {% cite zhang_effective_2007 %}. In order to be effectively exploted, these methods require expertise and skills to understand and elicit how experts structure and articulate their knowledge about a domain {% cite umber_requirements_2012 %}.
* Synthetic, or collaborative methods (use case scenarios, prototyping, JAD and RAD sessions, etc.) — techniques, that represent cohearent whole systematic synthesis of various methods from above into single ready-to-use method, instead of simple combinations of individual disjoint methods {% cite zhang_effective_2007 %}. These methods may provide the whole prospective on the application to be developed and its domain, however, inherit issues of the combined methods and require skills and deep understanding to be successfully applied {% cite umber_requirements_2012 %}.

Several researches were conducted to identify the most used in web development requirements techniques and the most relevant ones. In particular, Sajjad and Hanif {% cite sajjad_issues_2010 %} concluded in their thesis, that for large web systems, requirement elicitation commonly uses conversational methods, primarely interviews and brainstorming, and synthetic methods, with a focus on JAD sessions and prototyping. Later, Oliveros et al. {% cite oliveros_requirements_2016 %} conducted questionnaire on the frequency of various requirements elicitation techniques use in web applications development, that supported the popularity of both, individual and group, interviews and brainstorming, as well as highlighted frequent exploitation of the use cases and focus groups. The results also shows recognition of prototyping as the most promising requirements validation resource. 

In 2004, Escalona and Koch {% cite escalona_requirements_2003 %} also explored elicitation techniques, used for web applications, in a comparative study, however, focused precisely on elictation phase in complex requirements engineering frameworks, developed specifically for the web domain, such as Web Site Design Method (WSDM), Scenario-based Object-Oriented Hypermedia Design Methodology (SOHDM), Relationship-Navigational Analysis (RNA), Hypermedia Flexible Process Modeling (HFPM), Object Oriented Hypermedia Design Model (OOHDM), Web Modeling Language (WebML), Navigational Development Techniques (NDT), Design-driven Requirements Elicitation (DDRE), UML-based Web Engineering (UWE), and another UML-based multimedia elements modeling framework — W2000. Notably, most of these methodologies include interviews series, use cases analysis, and prototyping, confirming the high usage frequency of these techniques in web domain. Further, comparison of the requirements types consideration indicated a diverse coverage of the all selected requirement types by NDT and DDDP approaches. Тhough, the results of the comparative analysis of the ready-to-use solutions demonstrated a preponderance of the focus towards design aspects instead of the requirements engineering.

### 2.2 Web Applications Requirements Overview

Despite web applications variability in their purposes and types, most of the analysed in this research papers highlights common features in the final products, as well as in the development process, and corresponding reflection of the domain specifics in the requirements engineering similarities. 

Many insights on the web systems requirements were highlighted by Lowe in his overview {% cite lowe_web_2003 %}. The research explores specific characteristics of web systems and their impact on requirements engineering. Throughout the paper, Lowe emphasize the increased importance of the non-functional requirements in web in terms of such quality attributes, as usability, performance, reliability, and maintainability, caused by increased transparency of such flaws in web application, that are frequently directly accessible to external users and customers. The paper notes the distinguishing for the web domain emphasis on user-interface, its real-time interactivity, engagement and usability, due to the ability of the user quickly and effortless switch between websites. Web applications also depicted to be often developed in short time frames, be maintainable in terms of modifiability and modularity, motivated by rapid evolution of web technologies. Increased modification frequency, powered by the technological evolution pace and high competitiveness of web projects also causes need for application architecture scallability. The paper recommends a design-driven requirements process to manage these challenges effectively​, that is further developed into prototyping-based DDRE methodology {% cite lowe_client_2002 %}, mentioned in the previous section.

Further, the idea of web-specific requirements was developed by Sajjad and Hanif {% cite sajjad_issues_2010 %} in their Master thesis, that studies characteristic issues and challanges of requirement elicitation, inherent to large web projects. The study emphasize the versatility of web requirements and the need to explore structure, navigation, content and access requirements on part with functional and non-functional ones. User-centric design, capability to handle vast number of diverse in geography, culture, age, norms, or values users, and content structuring are highlighted as key common requirements, as well as the need for security {% cite munir_systematic_2023 %}, reliability, and performance for robust complex web systems.

In details, the non-functional concerns (NFC) of web services are explored by Schmeling et al. {% cite schmeling_non-functional_2010 %}. The research identifies indispensable for enterprise web systems quality attributes as security, performance, availability, and reliability. It concludes, that for the web services composition and non-functional requirements successful coverage and satisfaction, both specification and enforcement concerns need to be addressed and inspected, moreover, providing and analysing different approaches to these concerns.

### 2.3 Challenges in Eliciting Web Requirements

#### Requirements Volatility

By their nature, web systems are noted to cause changes and evolution in business models and processes of the client as organisations migrate their operations into automated web solutions {% cite lowe_web_2003 %}, leading to subsequent changes in the requirements, that as well can be caused by developing stakeholders' understanding of the product, its capabilities and their own needs, technological advancements, and high competitiveness. The volatility barriers make it difficult to establish a stable, comprehensive set of requirements early on, resulting in ongoing adjustments as new needs, requirements, and opportunities emerge {% cite sajjad_issues_2010 %}. This also implies that the linkage between the business architecture and the technical design of the system might be much tighter than in other software systems domains. This issue increase the importance of flexible and modifiable processes, both in development and in requirements, followed by the need of reusable, scallable, modular requirements structuring. The challange here arise in the balancing flexibility support and maintaining project requierements consistency, while avoiding scope creep.

#### Rapid Technological Changes

As mentioned previously, web domain is characterized by the variability of technologies, frameworks, libraries, and tools and their continuous evolution {% cite lowe_web_2003 %}. High conpetitiveness of the domain, caused by almost effortless launch and switch between different web solutions, wide adoption by the web applcations of multiple commercial off-the-shelf (COTS) components and integration with third-party APIs brings the neccessity to promptly adapt to such updates. This rapid change create uncertainty for both developers and stakeholders, as systems need to be designed to integrate with new emerging technologies and remain relevant over time. 

#### Short Time-to-Market

Rapid pace of technological advances and increased conpetitiveness of the web services, accompanied by irrelevant perception of the ease of web development, also produced a tendency of web projects to have much shorter delivery schedules than conventional software projects {% cite lowe_web_2003 %}. A common for many customers perceprion that persists to this day about ability of anyone to develop an effective web application with a use of simple Web authoring tools, coupled with numerous small, claiming to be effective WebDev companies in reality offering little more than a combination of HTML and simple graphic design skills, created unrealistic expectations from the customers. As a result, web development projects express a notable interest in light-weight time-effective processes, that is as well valid in terms of requirements elicitation methods.

#### Domain Knowledge Gaps

Uncertainty in domain understanding might be coming from both customers and developers {% cite lowe_web_2003 sajjad_issues_2010 %}. While customers are often missing a comprehensive understanding of what is feasible within the scope of modern web technologies or fail to articulate their needs fully, development team might also lack understanding of the system domain due to the versatility of applications and high integrity of web projects with other domains, from e-commerce to machine learning, and rapid technological evolution. Therefore, it is required for the elicitation technique to be able to gain clear structured domain knowledge, refined by the both sides, and fulfill existing gaps. It is also important to take into account, whether it is an existing or completely new domain, as the elicitation will vary in approaches to them {}.

#### Global Context

Most of web applications are available world-wide, therfore frequently developed to serve a global audience, which introduces additional complexity in eliciting requirements {% cite lowe_web_2003 sajjad_issues_2010 %}. Developers should consider diverse pool of stakeholders, cultural differences, multilingual support, varying user behaviors, compliance with local regulations and norms in the requireents and communication with stakeholders during elicitation process as well. Addressing these diverse needs requires effective strategies to gather requirements from multiple geographic regions, overcome communication barries, such as individual culture limitations, organizational cultures limitations, and national culture limitations {% cite zhang_effective_2007 %}, and ensure inclusive design. 

#### Lack of Attention to Non-Functional Requirements

As was mentioned previously by by Schmeling et al. {% cite schmeling_non-functional_2010 %}, the non-functional requirements (NFRs) are often overlooked or not properly addressed during the requirements elicitation process for web systems, despite their criticality for ensuring the software product quality and clear importance, highlighted by the researches in Section 2.2. Unlike functional requirements, which describe what the system should do, NFRs focus on how the system performs and behaves under various conditions, forming the systems quality, which is highly significant in the context of small attention span of the web user and variety of the quickly accessible alternitives. However, stakeholders frequently fail to articulate these requirements due to a lack of technical understanding or awareness of their importance. As a result, critical in web reqirements left uncaptured, leading to the unsatisfied expectations of the final product. For example, Riveros et al. cautions, that usability requirements are usually forgotten or unconsidered, while being the most important NFRs in web applicationa and determining their acceptability.

<div id="Analysis"></div>

## 3. Comparative Amalysis 🔎

### 3.1 Comparative Analysis Framework

Selection of comparison criteria was based on several researches, standing out in elicitation techniques comparison field, and on the findings, extracted by the literature review. As it was noted by Umber et al., good requirements elicitation process developes specification with the following attributes: unambiguous, complete, verifiable, consistent, modifiable, accountable and convenient during operations and maintenance {% cite umber_requirements_2012 %}. Developed comparison framework aims to depict reflect compliance of the produced by techniques outcomes with these criteria.

To begin with, I compared the general properties of the chosen approaches to requirements: elicitation means type, requirements source, degree of stakeholders involvement, tools usage, and applicability to existing/new domains. Feasibility of usage in the different domains was assessed partially based on the outcomes of the Sajjad and Hanif research {% cite sajjad_issues_2010 %}.

Further, the abilities to avoid issues related to the global geographically-distributed web environment was examined. Global context of web applications causes stakeholders variety in geographical location and time zones, that needed to be handled. Diversity also causes several commmunication obstacles, classified and evaluated by Zhang {% cite zhang_effective_2007%} as national culture, organizational culture, and individual cognitive limitations. Ability to overcome these barriers, as well as necessity of stakeholders' geographical and temporal collocation during elicitation compared across the techniques.

Next, I analysed alliance of the approaches with rapid pace of web appplications development and updates, based on their time costs and efforts in terms of preparation and conduction time, required skills, that could take time to obscure, and user efforts. These metrics and their assessment method was inpired by Wellsandt et al. {% cite wellsandt_qualitative_2014 %} elicitation techniques comparison, while time costs comparison and its results for severall techniques (interviews, prototyping, JAD) was adopted from Rueda et al experiments {% cite rueda_requirements_2020 %}. 

The most complex work was conduct in the following step - completeness evaluation of the produced by elicitation technique requiremnts. Comparison criteria of completeness included ability to extract identified significant components of the web services requirements:

* Functional Requirements;
* Non-functional requiremnts, including usability, performance, reliability, availability, security, and maintainability quality attributes;
* Navigational Requirements;
* Content Requirements;
* Interface Requirements;
* Domain Knowledge;
* Relevant Stakeholders;
* Social Issues.

Last but not least, I assessed the maintainability of the produced requirements formats to reflect their ability to handle requirements change in terms of structure, scallability, and modifiability.

<!-- Final comparison criteria, their description and range of values can be observed in Table 1.

<p style="width: 100%; font-weight:bold; text-align:center;">Table 1: Comparison Criteria.</p>

| Comparison Criteria | Description | Range of Values |
|-|-|-|
| Requirement Sorce |  |  |
| Stakeholder Involvement  | Measures the degree of active involvement from stakeholders. Ensures application meets diverse stakeholder needs and objectives. High involvement indicates comprehensive requirements and stakeholder satisfaction. | None, Low, Medium, High | =
| Adaptability | Evaluates flexibility to incorporate changes. Projects require techniques that adapt to new information. High adaptability shows the technique can handle changes efficiently. | Rigid, Moderate, Flexible | 
| Scalability | Indicates effectiveness across project sizes. Techniques must scale from simple to complex web apps. High scalability suggests efficiency across different scenarios. | None, Low, Medium, High | 
| Time and Cost Efficiency | Evaluates resource efficiency. Critical due to tight deadlines and budget constraints. Resource-efficient techniques meet project constraints effectively. | High Cost/Time, Moderate, Low | 
| Tools and Techniques Support | Assesses availability of supportive tools. Tools enhance efficiency and collaboration in web development. Strong tool support suggests reliable and effective processes. | None, Poor, Adequate, Excellent |  -->

### 3.2 Requirements Elicitation Techniques Analysis

For the comparative analysis, I included 10 common requirements elicitation techniques, based on their usage in the web development domain and overall popularity. As well, I tried to cover all 4 elicitation technique types. Representation of these types in the comparative analysis is the following:

* Conversational techniques: Interview, Brainstorming, Questionnaire, Focus Groups;
* Observational techniques: Ethnography;
* Analytic techniques: Document Analysis, Interface Analysis;
* Synthetic techniques: Prototyping, Use Cases, JAD.

Now let me focus on each of the chosen for comparison requirements elicitation technique and analyse its strong and weak ponts.

#### Interview

The most common and intuitive requirements analysis techniques is group or individual interview with the stakeholders. The analyst conducts meeting with stakeholder, directly asking questions in order to clarify the project, its objectives, problems to be solved and create the common vision. While interviews are a widely used and often essential method, they can lead to misunderstandings due to the conversational format. Differences in background, vocabulary, levels of domain understanding, and overlooked aspects of the discussion often cause further issues. One of the common ambiguity, that could be born in such discussions, is the user-frendly UI/UX web interface. User could meant different things by saying "intuitive interface", therefore if the clear aceptance criteria of usability was not specified during elicitation, such definition can cause the difference in expectations between the frontend developers and the stakeholders. The success of an interview largely depends on the interviewer’s skills, quality of prepared questions, clarified details, interviewee’s understanding of the domain and their needs. Even with existance of various methodologies like the "Mom Test" to guide information extraction, outcomes still hinge on the interviewer’s familiarity with these methodologies and their ability to apply them effectively. 

#### Brainstorming

The next approach to the elicitation process is the brainstorming technique used to generate large number of solution ideas for the project and clarify unclear and unspecified requirements. Brainstorming usually conducted as a conference with six to ten members with diverse background and domain knowledge depth, helping to resolve gaps in domain understanding. It is conducted by the facilitator, who declares the problem, for which the ideas will be generated, prior to the meeting. The final solution is chosen using voting. Therefore, brainstorming is not useful for project with a small group of stakeholders, having disparate needs. 

#### Questionnaire

Questionnaire is a multistage process, that begins with definition of the aspects to be examined and end with interpretation of the result. It is low-effort way to gather data from a large number of stakeholders, presented in a structured and easy to analyze format. Moreover, indirect way of data gathering helps to overcome interaction issues with distributed groups. The result depends upon the quality of designed questions and the honesty of the respondents. Sadly, approach has limited control over the process and environment, which endanger validity of results. The data can be collected in text form, but more frequentle the questionnaires are automated using tools, such as Google Forms or different online polls.

#### Document Analysis

This common method consists of reading and studying available documentation for content, that is relevant to and useful on the requirements elicitation tasks. Document analysis deducts information from experts’ knowledge and experience form another source of requirements, therefore requires skills to understand written by experts documents, such as organizational policies, standards, legislation, market researches and legacy systems specification. Additionally, documents might conatain outdated information and, for the most part, are lacking context about actual state, informal practices and knowledge, social and communicational issues.

#### Focus Groups

Focus groups is a technique aimed on evaluation of stakeholders needs, opinions, and dynamic. Conducted in a form of a facilitated group discussion of current work procedure problems and ideal solutions, it provide insights on group interaction and organizational issues through users spontaneous reactions and ideas. While organized similarly to brainstorming meetings, focus group are used for understanding perspectives and motivations related to specific topics instead of focusing on idea generation, consequently it characterized by more structured guided discussion-focused flow to ensure relevant data is collected. Focus groups might provide valuable rich data, though, it requires careful representative selection of participants to prevent externl validity threats and skewing of discussion by dominant personalities, leading to biased or incomplete ungeneralizable results.

#### Ethnography

Ethnography is the common method used to capture the tacit requirement from the real-world environment. The analyst spends a period of time along with stakeholders in their natural settings (company, country, etc.) by observing what they do without directing the outcomes, thus, getting a detailed information and deep understanding about the workflow, organizational culture in stakeholder own language and terminology. Ethnography is helpful in complex projects enhancing in-depth understanding of the application domain, project routine, complex problems faced by the stakeholders, information flow, social/organizational cultures, work setting (team interaction and collaborative work), and communication obstacles. Knowledge is collected through different sources, such as passive and participant observation. Should be noted, that ethnography is a lengthy process, not suitable for very short timeframes. the observer is also required to be accepted by the people being studied as a kindred spirit and must be sufficiently familiar that they carry on with their normal practices as if he was not there. As most of the observational methods, it requies certain skills to advance further, than workflow observation, and understand stakeholders perception of it.

#### Prototyping

Prototyping is another important for web systems requirement elicitation method, that involves partial visualization of the application to be built, its review with stakeholders and, sometimes, iterative refinement. Is is used to develop a concrete sense of stakeholders about the application, which has not yet been implemented, overcome their domain understanding gaps, identify true feasible requirements and workflow of actual system. Produced results usually contains product features and detailed specifications. Prototyping is the best fit in a situation, when the stakeholders experience difficulties to express their requirements or in a new domain, that stakeholders lack experience about. While the technique provides high level of user satisfaction and reducing development costs and time by errors detection in the early stages, it is highly expensive by itself, requiring development of the simplified system copy (prototype), that most likely will not be used further. The approach can be used as for elicitation, as for requirements validation stage.

#### Interface Analysis

Interface analysis is an analytic method used to identify and describe the interactions among system components, external systems, and users. This approach enhances system integrability by clarifying how various components interact, enabling early detection of potential integration issues. Facilitation of these knowledge in precise system requirements leads to improved usability and system performance. However, the method can be resource-intensive, requiring comprehensive documentation and technical expertise, which may present challenges for teams without sufficient resources or specific skills. 

#### Use Cases

Use case modeling is an interaction session, aimed to describe a sequence of actions and events for a specific case of the generic tasks that the system is intended to accomplish. A use case model consists of actors, use cases, and relationships between them. Actors represent the system environment, while use cases (functional requirements) describe the scope of the system. A use case describes a sequence of interactions between the system and its actors when a concrete function is executed. The main advantage of this technique is that a use case model plays the role of structured and easy-to-be-understood middleware between stakeholders and developers, resolving ambiguities and misunderstandings. However, they might lack details and overly focus on the system functionality, neglecting non-functional requirements and implementation constraints.

#### Requirements Workshop (JAD)

Joint Application Development, or JAD, is a synthetic structured requirements workshop, that systematically involves stakeholders analysts, and developers in facilitated, focused meetings to precisely define product features and requirements. The methodology unfolds is divided into several phases: customization, where sessions are prepared and tailored to the project's specific context; session, where stakeholders engage in focused discussions to extract and generate requirements; and wrap-up, where these requirements are formalized into a detailed document. The advantages of JAD include enhanced precision and alignment in requirement gathering, misinterpretation risk minimization by fostering a shared understanding and concensus among participants. This approach accelerates decision-making and overcomes misunderstandings of the software product and its domain. However, it also demands on significant time and resources costs, require skilled facilitation and active engagement of various stakeholders which may not be suitable for smaller or resource-limited projects. Consequently, while JAD is highly-effective for projects in need of comprehensive requirement synthesis and agreement, it should be chosen with consideration of the project's size and available resources.

### 3.3 Threats to validity.

The research is mostly retrospective and literature-based, therefore poses:

* selection bias in terms of the limited set of chosen papers;
* history bias due to the age of some papers;
* instrumentation bias, caused by usage of the single academic library - Google Scholar.

However, this study successfully avoids maturation biases - due to the short timeframe, in which it is conducted -, any testing and interaction biases, due to the absence of practical experiments and interacting elements.

## 4. Results 📊

### 4.1 Comparative Analysis Results 

The results of the comparative analysis are present in the Tables 1-5. While Table 1 provide general properties comparison  of the techniques, such as their source type, elicitation method, tools usage, etc., each of the following tables focuses on the different web elicitation challanges in details.

<p style="width: 100%; font-weight:bold; text-align:center;">Table 1: General information.</p>

| Comparison Criteria | Interview | Brainstorming | Questionnaire | Focus Groups | Ethnography | Document Analysis | Interface Analysis | Prototyping | Use Cases | JAD |
|:-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|-:|
| Type | Conversational | Conversational | Conversational | Conversational | Observational | Analytical | Analytic | Synthetic | Synthetic | Synthetic |
| Requirement source | Human | Human | Human | Human | Environment | Environment | Environment | Human | Human | Human |
| Stakeholders involvement | High | High | High | High | Low | None | None | Mediocre | Mediocre |  High |
| Suitability for existing domain | 4 | 2 | 2 | 3 | 1 | 3 | 3 | 3 | 3 | 4 |
| Suitability for new domain | 3 | 3 | 1 | 1 | 4 | 1 | 1 | 4 | 2 | 2 |
| Tools-based | No | No | Yes | No | No | No | No | Yes | Yes | No |

Table 2 provides assessment of the techniques on their ability to handle global web environment, consequent geographical distribution and communication barriers of the stakeholders.

<p style="width: 100%; font-weight:bold; text-align:center;">Table 2: Global Context Suitability.</p>
<table>
  <thead>
    <tr>
        <th>Comparison Criteria</th>
        <th>Interview</th>
        <th>Brainstorming</th>
        <th>Questionnaire</th>
        <th>Focus Groups</th>
        <th>Ethnography</th>
        <th>Document Analysis</th>
        <th>Interface Analysis</th>
        <th>Prototyping</th>
        <th>Use Cases</th>
        <th>JAD</th>
    </tr>
  </thead>
    <tr>
        <td>Geographical colocation</td>
        <td>Recommended</td>
        <td>Recommended</td>
        <td>Optional</td>
        <td>Recommended</td>
        <td>Essential</td>
        <td>Unsuitable</td>
        <td>Unsuitable</td>
        <td>Optional</td>
        <td>Recommended</td>
        <td>Essential</td>
    </tr>
    <tr>
        <td>Temporal colocation</td>
        <td>Essential</td>
        <td>Essential</td>
        <td>Optional</td>
        <td>Essential</td>
        <td>Essential</td>
        <td>Unsuitable</td>
        <td>Unsuitable</td>
        <td>Optional</td>
        <td>Essential</td>
        <td>Essential</td>
    </tr>
    <tr>
        <td colspan="11">Ability to overcome communication barriers:</td>
    </tr>
    <tr>
        <td>National culture barriers</td>
        <td>3</td>
        <td>2</td>
        <td>1</td>
        <td>3</td>
        <td>4</td>
        <td>2</td>
        <td>2</td>
        <td>4</td>
        <td>4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Organization culture barriers</td>
        <td>2</td>
        <td>4</td>
        <td>1</td>
        <td>3</td>
        <td>4</td>
        <td>3</td>
        <td>1</td>
        <td>3</td>
        <td>3</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Individual cognitive limitations</td>
        <td>3</td>
        <td>2</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>2</td>
        <td>4</td>
        <td>4</td>
        <td>3</td>
    </tr>
</table>

The comparison of the methods time costs and suitability for short developent timeframes is descrbed in Table 3.

<p style="width: 100%; font-weight:bold; text-align:center;">Table 3: Time-efficiency.</p>

| Comparison Criteria | Interview | Brainstorming | Questionnaire | Focus Groups | Ethnography | Document Analysis | Interface Analysis | Prototyping | Use Cases | JAD |
|:-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|-:|
| Required skills | Low | Mid | Low | Mid | Mid | High | High | High | High | High |
| Effort per user | Mid / Few | Mid / Many | Low / Many | Mid / Many | High / Many | High / Few | High / Few | High / Few | High / Few | High / Many |
| Preparation time | Mid | Mid | Mid | Mid | Low | Low | Low | High | Low | High |
| Elicitation time | Low | Mid | Mid | Mid | High | High | High | High | Mid | High |

Furthermore, summarised by Table 4 completeness comparison analyses coverage of significant for web application aspects by elicitation approach, including navigational, interface, content, functional and non-functional requirements, domain knowledge gaps, relevant stakeholders, etc.

<p style="width: 100%; font-weight:bold; text-align:center;">Table 4: Completeness.</p>

<table>
    <tr>
        <th>Comparison Criteria</th>
        <th>Interview</th>
        <th>Brainstorming</th>
        <th>Questionnaire</th>
        <th>Focus Groups</th>
        <th>Ethnography</th>
        <th>Document Analysis</th>
        <th>Interface Analysis</th>
        <th>Prototyping</th>
        <th>Use Cases</th>
        <th>JAD</th>
    </tr>
    <tr>
        <td>Functional requirements coverage</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>High</td>
        <td>High</td>
        <td>High</td>
    </tr>
    <tr>
        <td>Navigational requirements coverage</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>None</td>
        <td>Low</td>
        <td>Mid</td>
        <td>High</td>
        <td>Mid</td>
        <td>Low</td>
    </tr>
    <tr>
        <td>Content requirements coverage</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>None</td>
        <td>High</td>
        <td>None</td>
        <td>Low</td>
    </tr>
    <tr>
        <td>Interface requirements coverage</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>High</td>
        <td>High</td>
        <td>Low</td>
        <td>Low</td>
    </tr>
    <tr>
        <td>Domain knowledge coverage</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>High</td>
        <td>High</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>High</td>
    </tr>
    <tr>
        <td>Stakeholders identification</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>High</td>
        <td>Mid</td>
        <td>None</td>
        <td>Low</td>
        <td>High</td>
        <td>High</td>
    </tr>
    <tr>
        <td>Social issues coverage</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>High</td>
        <td>High</td>
        <td>Low</td>
        <td>None</td>
        <td>None</td>
        <td>None</td>
        <td>High</td>
    </tr>
    <tr>
        <td colspan="11">Non-functional requirements coverage:</td>
    </tr>
    <tr>
        <td>Usability</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>None</td>
        <td>High</td>
        <td>High</td>
        <td>Mid</td>
        <td>Low</td>
    </tr>
    <tr>
        <td>Performance</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Mid</td>
    </tr>
    <tr>
        <td>Availability</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
    </tr>
    <tr>
        <td>Reliability</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
    </tr>
    <tr>
        <td>Security</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
    </tr>
    <tr>
        <td>Maintainability</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Low</td>
        <td>Mid</td>
        <td>Low</td>
        <td>Mid</td>
    </tr>
</table>

Finally, Table 5 compares output requirements format in terms of its maintainability for further usage and modifications due to the requirements volatility.

<p style="width: 100%; font-weight:bold; text-align:center;">Table 5: Requirements Fromat.</p>

| Comparison Criteria | Interview | Brainstorming | Questionnaire | Focus Groups | Ethnography | Document Analysis | Interface Analysis | Prototyping | Use Cases | JAD |
|:-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|-:|
| Structured | Less | Less | More | Less | Less | Less | More | More | More | More |
| Scalable | More | Less | More | Less | Less | More | Less | More | Less | Less |
| Modifiable | More | Less | More | Less | Less | More | More | More | More | Less |


### 4.2 Limitations

This study is limited by the time and resources constraints, therefore provides only theoretical analysis of a small subset of existing requirements elicitation techniques, focusing on a most used common techniques. The field of requirements elicitation varies in the form and approaches and methodologies, including listed in Section 2.1 web requirements engineering frameworks, that could be further researched according to the provided comparative analysis framework. As well, due to the theoretical, literature-based nature of the research, comparison is limited in terms of quantifiability of the criteria, however, ordinal range of the criteria assessment could be further supplement and validated by quantitative values, gathred from practical experiments. It is also important to mention, that identified primary requirements and issues were collected from the generall literature review, narrowed by the English language and single academic papers source, Google Scholar. The research findings might be complemented and validated by the systematic literature review, inclusion of other academic libraries, such as Scopus, ACDM, IEEE, etc., and complex research queries.

<div id="Discussion"></div>

## 5. Discussion 💬

### 5.1 Key Findings

Analysing result tables, we can highlight techniques more and less effective in the domain barriers overcoming and web requirements capturing. The following conclusions can be withdrawed from the result statistics:

* Noticably, observational and synthetical methods performs good in overcomimg communicational barriers (Table 2) by their in-depth analyis and providing means to nogotiate ambiguities, like prototypes and use case models. However, most of them are unapplicable or hard to be executed in distributed groups, only Prototyping out of them suits good for such environments, offering a solution to be examined on the distance, and possibility to send feedback on it later.
* Questionnaires, Interviews, Brainstorming and Focus Group sessions may provide swift mid-effort solutions in the context of strict time limitations. On part with them, Use Case modeling also shows good use proximity, provided that the corresponding skills are present in the team.
* Best coverage of the relevant in web application development components is presented by JAD and Prototyping, followed by Focus Groups, Ethnography, Use Case Diagrams, and Interface Analysis. While Ethnography and Focus Groups shows good results in covering issues of domain understanding, JAD, Use Cases, and Prototyping are able to effectively identify key functional and nonfunctional requirements of the product to be developed.
* Prototyping and Questionnaires demonstraited effective and flexible maintainability, presenting structured modifiable outcomes, that could be less-effortless adapted to possible changes in requirements. 


### 5.2 Implications for the Web Software Development Management

Performed analysis underscored the importance of selecting appropriate requirement elicitation techniques based on project needs and domain knowledge in web software development. Discovered findings can further guide requirements engineers and project managers in optimizing efficiency of requirement elicitation in web projects. For exapmle, prototyping emerged as a vital tool for distributed teams, facilitating remote collaboration and feedback. On part with techniques, like JAD and use case modeling, it appeared to be crucial for capturing comprehensive functional and non-functional web requirements. For projects with time constraints, utilizing interviews, questionnaires, and brainstorming can offer effective and timely solutions, coupled with the adaptability of prototyping and questionnaires, that ensures seamless integration of evolving requirements and support of agile methodologies.

<div id="Conclusion"></div>

## 6. Conclusions 🏁

This study analyzed requirement elicitation techniques in web application development, focusing on their ability to capture key requirements and address domain-specific challenges. It identified significant obstacles, including requirements volatility, rapid technological changes, and insufficient attention to non-functional requirements. The analysis highlighted techniques like prototyping, JAD, and use case modeling as highly effective for capturing comprehensive functional and non-functional requirements, while methods like interviews and questionnaires - to be efficient for time-constrained projects. 

The findings underscore the importance of selecting techniques suited to project constraints and suggest a framework for further requirement elicitation techniques comparative studies. To enhance elicitation efficiency in the dynamic web development domain, I would suggest to explore the following directions in the future researches:

* Comparison scope expansion to include more diverse requirements elicitation techniques, especially web-specific requirements frameworks and newly emering technologies, like ML and NLP-based tools (IBM Watson AI, NLReq, etc.);
* Systematic literature review conduction across multiple databases (e.g., Scopus, IEEE Xplore) to reduce selection bias and enhance coverage of web domain specifics;
* Real-world validations of the research outcomes to enhance elicitation efficiency in the dynamic web development domain. 

<div id="References"></div>

## 7. References 📚

{% bibliography --cited %}


<div id="AIDisclaimer"></div>

> ---
> ## 8. 🔔 AI-Generated Content Disclaimers 🤖
> 
> **The author affirms that the core ideas presented in the paper are original.**
>
> **AI usage self-declaration:**
> * Translation [no]
> * Spelling correction [yes]
> * Text styling [no]
> * Summarization [no]
> * Content extraction [no]
> * Ideas generation [no]
> * Other [no]
> ---

[jekyll-scholar-citations]: https://github.com/inukshuk/jekyll-scholar#citations
