Author: Saveliy Chertkov, Innopolis University
Year: 2024
### Abstract 📝
This paper explores how to manage a software team without traditional management roles with an emphasis on the self-organazing team model, inspired by the practices at Valve Corporation. Valve's flat structure allows employees to choose projects and make decisions about them, which fosters creativity and innovation within the company. However, this model creates unique issues in identifying, assessing, and mitigating risks. Using Valve as an example, we examine risk management mechanisms and methods.
## 1. Introduction 📖
Self-organizing teams are teams characterised by their flexibility and adaptability [1]. In most cases Self-organizing teams consist of 10-15 people [1]. These teams are characterised by the following features [1] :
1. Informal and temporary.
   These teams are formed on an ad hoc basis to work on a specific project.
2. Formed spontaneously.
   Such teams appear around the task at hand on their own, not by assignment from a central authority.
3. Absence of formal hierarchy.
   In such teams there is no traditional organisational structure and decision-making is shared.
### 1.1 Motivation💡
With the current economic changes, such as salary cuts and layoffs of junior developers, with more than 191,000 employees laid off in the US according to Crunchbase [2], companies are faced with the need to optimize resources and retain key employees. These changes are forcing companies to rethink their approaches to organizing work in order to minimize costs and retain talented employees.
Self-organizing teams offer a promising solution to this problem, with its structure, Self-organizing teams helps to minimize management costs while maintaining high team productivity [3].
By eliminating complex hierarchies, they minimize bureaucracy by distributing responsibility among employees [1]. Self-organizing teams also help to increase employee motivation by involving them in decision-making and working on what they consider important [4]. 
Valve is a prime example of a company that has successfully operated without a traditional hierarchy using a self-organizing team approach [5] for 28 years, with many companies also using elements of self-organizing teams (Example: Spotify, Gore-Tex (W.L. Gore & Associates)).
However, although self-organizing teams have many advantages (reduced bureaucracy and increased employee engagement), they are not without problems. One such issue is the lack of established approaches to risk management in such structures. 
### 1.2 Problem Statement❓
Traditional risk management methodologies typically rely on hierarchical supervision [5]. Due to the lack of traditional hierarchy, as well as decentralized responsibility for decision-making [1], traditional risk management approaches may prove ineffective.
Valve successfully operates without a hierarchy, offering insights into decentralized management. An analysis of Valve's team structure highlights the following specific challenges in risk management:
* How does the company prevent project failures?
* What mechanisms allow to avoid wasting resources and time?
An analysis of Valve's command structure reveals the following key issues:
1. Uncertainty in the distribution of responsibilities.
   In the absence of formal roles [3], responsibility for risk management is shared among all team members. This approach can result in important risks being overlooked.
2. Limited applicability of traditional methods.
   Classic risk management tools are difficult to adapt to Valve's flat and decentralized structure. This requires the development of unique approaches that take into account the specifics of self-organizing teams.
## 2. Related Work 🔗
This section reviews several key articles that address aspects of self-organization, risk management, and team structure in software development. Particular attention is paid to the unique organizational model of Valve Corporation.
### 2.1 “Self-organizing roles on agile software development teams” [1]
This paper analyses the dynamic roles that arise in self-organising agile teams. This study provides insight into how self-organising teams operate without formal hierarchy. Particular attention is paid to the changing roles of employees.

**Key findings**:
* The study identifies several roles that emerge in self-organising teams such as: "Mentor", “Coordinator,” “Translator,” “Champion,” “Promoter,” and "Terminator".
* Unlike traditional teams, self-organising teams allow participants to change roles depending on the team situation, project needs or personal experience.
**Limitatoins**: The paper does not directly address risk management
### 2.2 “Employee self-management without formally designated teams: An alternative road to empowerment” [6]
This paper discusses empowering employees without relying on formal command structures through the introduction of self-management. It provides a deep understanding of the principles of autonomy and shared responsibility that underlie self-organizing teams.

**Key findings**:
* This paper emphasises that by empowering employees to take responsibility for their work can increase motivation, creativity and productivity in a team.
* By reducing reliance on formal hierarchies (not by removing them altogether, but by reducing their multi-level nature), organisations can encourage employees to co-manage their tasks and make decisions.
* This study notes that the lack of formal structures can lead to uncertainty in roles and responsibilities, potentially affecting co-ordination.

**Limitation**: The paper does not focus on software development, it indirectly discusses the risk management process.
### 2.3 “Managing innovation without managers: Valve corp.” [7]
This studi examines the Valve case, how employees work without traditional management roles, focusing on innovation and managing complex projects in a self-organizing environment.

**Key findings**:
* Valve's lack of formal management allows employees to choose projects and allocate their time, which increases motivation and encourages innovation.
* Valve has a "freedom to fail" philosophy whereby employees are not penalised for failures and mistakes. Mistakes are treated as learning opportunities that foster self-development.
* Valve conduct post-mortems on failed projects or decisions to analyse what went wrong and avoid similar mistakes in the future. Valve also conducts an annual employee evaluation process where each employee evaluates their peers. This review evaluates individual contributions to the company.
**Limitation**: The paper discusses innovation management and does not look in detail at operational aspects such as risk management.
### 2.4 “Valve’s way” [8]
This paper presents an analysis of Valve corporation's flat organisational structure, focusing on its cultural and operational aspects. 

**Key findings**:
* Without formal management roles, employees are accountable for their decisions to their colleagues. This can be achieved through the following mechanisms:
	1. Autonomy in selecting projects.
	2. Peer assessment of effectiveness.
* Although Valve's structures are flat, informal social hierarchies and leaders can emerge that affect decision making and team dynamics.
**Limitation**: This paper highlights the problems that can arise in a company when an informal hierarchy emerges, but does not consider how this affects the organisation's ability to manage risk, nor does it offer specific solutions to mitigate such problems.
### 2.5 "Handbook for New Employees" [4]
It is an internal document that provides a detailed view of the company's organisational philosophy. 
**Key findings**:
* Employees have complete freedom to choose the projects they are interested in.
* The handbook emphasises the absence of a formal hierarchy, where decisions are made jointly and responsibilities are shared among team members. 

**Limitation**: This article does not describe specific mechanisms to address operational tasks such as risk assessment and mitigation.
## 3. Discussion 💬
This section highlights the main approaches, described in the literature and using Valve corporation as an example, for managing risk in self-organising teams and analyses the strategies found.
### 3.1 "Freedom to fail" philosophy
Valve's philosophy of viewing employee mistakes as opportunities for growth [7] stands out as a new approach to risk management. 
This method differs significantly from traditional approaches as the focus shifts to learning. This insight can be useful for organisations looking to innovate. 
However, this approach can both benefit and severely harm a company. Therefore, to avoid employees repeating mistakes, you can add the tool of annual peer evaluation of employees to your company's operations.
### 3.2 Freedom to choose a project
According to the analysed articles [4]  [7]  [8], Valve corporation employees independently choose the project that inspires them. This approach helps to increase employee motivation and responsibility for their work. 
In addition, this approach automatically removes unsuccessful projects. It naturally eliminates those ideas that seem unfeasible.
### 3.3 Roles and their dynamics in self-organising teams
Self-organising teams often adapt roles depending on the needs of the project. Team members often take responsibility for certain aspects of the project (roles) and can be replaced by a colleague at any time if needed. In some cases, as in the Valve corporation example [7]  [8], one person on the team can take on multiple roles at once.
Roles in self-organising teams for risk management [1] :
1. Coordinator
	Tracks the assignment of tasks to team members. Allows you to quickly identify resource gaps, delays and inconsistencies in tasks.
2. Champion (master)
	Takes responsibility for key aspects of the project, solves critical problems. Helps minimise performance risks.
3. Mentor
	Helps less experienced team members adapt and enhance their skills. Also helps minimise risks associated with poor performance and eliminates risks associated with errors due to lack of knowledge in new employees.
### 3.4 Application of the self-organising team approach in software development
The model of self-organising teams can be effectively used in the following types of projects and companies:
1. Innovative projects
   Companies developing new innovative products can use self-organising teams to stimulate creativity and quickly test ideas and hypotheses, by "Freedom to fail" philosophy.
2. Creative industries
   In projects requiring a high level of creativity (gamedev). This structure favours the free exchange of ideas due to the flat hierarchy structure.
### 3.5 Key issue
All the approaches described above will only be able to demonstrate their effectiveness in conditions of a strong corporate culture and a high level of trust between employees [3]  [7]. However, in companies that are just beginning the transition to self-organising models, the main problem may be the lack of a cultural base.
To make the transition to such a model more seamless, companies need to:
1. You can't instantly jump to a flat hierarchical model. An immediate rejection of the traditional hierarchy can lead to confusion in the distribution of duties and responsibilities.
   Instead of a complete transition, it is recommended to gradually reduce the hierarchy levels. For better functioning, it is sufficient to reduce the number of management levels while maintaining the strategic role of senior managers.
2. Implement hybrid tools that combine both freedom of action for employees but also control.
## 4. Conclusions 🏁
This paper analysed approaches to risk management in self-organising teams using Valve Corporation as an example. 
Self-organising teams use the following approaches for risk management:
 1. "Freedom to fail" philosophy
 2. Freedom to choose a project
 3. Roles and their dynamics in self-organising teams
 However, although this model looks successful in theory, it has a number of drawbacks that can be very damaging to companies. When moving to this model, you need to clearly understand that your company has a strong corporate culture and level of trust among employees. 
 The results of the study highlight the potential of self-organising teams in a dynamically changing market, especially for innovative and creative projects.
Valve Corporation's experience can serve as a reference point for companies that seek to reduce bureaucracy and increase employee motivation. 
## References 📚
[1] R. Hoda, J. Noble, and S. Marshall, “Self-organizing roles on agile software development teams,” IEEE Transactions on Software Engineering, vol. 39, no. 3, pp. 422–444, 2012.

[2] “Tech Layoffs: US Companies With Job Cuts In 2023 and 2024,” Crunchbase News, [Online]. Available: https://news.crunchbase.com/startups/tech-layoffs/. [Accessed: 2-Dec-2024]

[3] Moe N. B., Dingsøyr T., Dybå T. Understanding self-organizing teams in agile software development //19th australian conference on software engineering (aswec 2008). – IEEE, 2008. – pp. 76-85.

[4] Valve Corporation, "Handbook for New Employees," 2012.

[5] Pressman R. S. Software Engineering: a practitioner’s approach //Pressman and Associates. – 2005.

[6] F. Shipper and C. C. Manz, “Employee self-management without formally designated teams: An alternative road to empowerment,” Organizational Dynamics, vol. 20, no. 3, pp. 48–61, 1992.

[7] D. Thornblad, “Managing innovation without managers: Valve corp.,” Journal of Case Studies, vol. 36, no. 2, pp. 92–107, 2018.

[8] P. Puranam and D. D. H˚akonsson, “Valve’s way,” Journal of Organization Design, vol. 4, no. 2, pp. 2–4, 2015.

> ### 🔔 AI-Generated Content Disclaimer 🤖

> The author declares that his original ideas are the core of this article’s content. The content is verified for factual accuracy.
> **AI Usage Self-Declaration**:
> - Spelling correction: [yes]
> - Text styling: [yes]
> - Translation [yes]


