# **Evaluation of legacy projects to align with current business goals**

_Author: Ravil Nurgaliev, Innopolis University 👤_ _Year: 2024_
# Introduction 📖

## Motivation 
It is necessary to ensure that existing systems and processes align with current business goals, because old systems can, for example, ruin data integrity [1].
## Problem Statement 
Sometimes it can be challenging to align legacy projects functionality with new business objectives - this leading to inefficiencies or increased costs. Evaluation aims to identify opportunities for support growth and innovation. Also, we will focus on discussing provided ways to do so.
# Related Work 🔗

There are some papers for this topic, where various modernization and assessment strategies are discussed.

### 1.“Navigating the Modernization of Legacy Applications and Data: Effective Strategies and Best Practices” by Sivakumar Ponnusamy and Dinesh Eswararaj [2]
    
This work mentions that it is important to modernize legacy systems (these points are common and next papers may somehow mention them too):

- old systems are exposed to modern cyber attacks which were not present at the moment of development
- poor scalability leading to bottlenecks
- old systems mostly are not supported by their vendors, making them hard to maintain and run

Main suggested objective of modernization is to move this system from liability to an asset in driving business

Proposed method for assessment - systematic methodology with 4 steps:

- data collection ( modernization need and drivers)
- data analysis ( modernization, user acceptance, strategy issues and challenges) 
- results and discussion ( best strategies and approaches used )
- conclusion ( modernization options)

Also, authors mentioned possible diagram of actors and actions (use-case), with each person related to various challenges:

- `Developer`
- `User`
- `Trainer/ owner`
- `Security specialist`
- `DevOps engineer` 

This diagram acts as a framework.

### 2. “A Method for Assessing Legacy Systems for Evolution”, by Jane Ransom, Ian Sommerville, and Ian Warren [3]

Vision for legacy systems is similar to the previous paper, so it is a system which was developed in the past and is critical to the business where it operates. 

The assessment method presented in this paper involves measuring the system’s technical quality, its business value, and all organisational characteristics.

The main objective of RENAISSANCE is to develop a systematic method for system evolution and reengineering which is geared to the requirements of commercial systems.

**It has 2 key ideas** :
- `company/product specific re-engineering`
- `constant refinement of re-engineering`

The **following questions** are typical of what can be answered on completion of this method’s assessment exercise: 
- *Is the system critical to the organisation in which the system operates?* 

Assessment might reveal that a system is not essential to the continued operation of the business. If yes, it is not important to update this system.
- *What are the organisation’s business goals?* 

Business goals are used to create evolutionary requirements. 
- *What are the evolution requirements?* 

Evolution requirements are derived from business goals and assessment activities. Requirements need to be anticipated to determine whether the existing system can satisfy the requirements. 
- What is the anticipated lifetime of the system? 

A system’s lifetime is defined by serviceability of software and hardware. 
- *What is the required life of the system?*

If this life is relatively long, we may think about this system’s evolution.
- *What is the technical state of the system?* 

Check state first to later decide whether this system is hard or expensive to maintain.
- *Is the organisation that operates the system amenable to change?*

The organisation’s attitude towards change is a critical success factor for evolution projects. 
- *Does the organisation responsible for evolving the system have sufficient resources?* 

Factors such as the organisation’s technical maturity, skills base and quality of employees, and level of tool support have an impact on evolution projects.

  
After these questions, this method has instanciation method with 2 parameters:
- assessment technique
- assessment level

To assess, we have various metrics, experts and sources:
- we may need application, legacy functional and implementation experts
- metrics must be used carefully, not to create misunderstanding or meaningless results.

Then, some systems characteristics are covered:
- business value
- external environment ( hardware, software, organisational infrastructure)

These characteristics are described in table both on high and low level, with calculated values.

In result, assessment activities produce a collection of characteristic-value pairs for hardware, support software and application software. 

These properties of the legacy system collectively provide a technical perspective of the system. A weighted average assessment value for technical quality can be derived from the technical property values.

After all, results are interpreted in a table ( figure 1):

![image1.png](image1.png)

Figure 1 - assessment of business and technical values

Important, that we obtain the ability to analyze – whether this system is critical, evolution requirements, current state, etc.

Risk of producing an inaccurate assessment can be reduced by further iterations of the method, performed at more detailed levels.

### 3. “A Decisional Framework for Legacy System Management”, by Andrea De Lucia, Anna Rita Fasolino, Eugenio Pompella [4]
  
The main idea of this work is that a decision about how to evolve a legacy system must be made with focus on several factors: software’s value, risks and costs. 

Authors proposed an assessment model with division to business and technical values of a legacy system. These values have variables and metrics for them, containing a sequence of steps required to measure all the attributes.

The business value depends on how effectively the software asset is used in the organization and determines benefits to its stakeholders.

The technical value depends on the characteristics of the software components, and on the external technical environment of the system, including hardware, support software and organizational infrastructure

This method provides later usage of the decision model - basically, a set of rules with structured approach.

#### Decisional model has these steps: 
- Goal definition

  `Several business goals were specified that took into account the points of view of the system vendors, users and maintainers`

- Gap Analysis

	`Actual quality profile of each system unit was assessed and compared with the expected Quality Profile`

- Portfolio Analysis
    
	`Determining the maintenance needs for each software unit and for prioritizing the work`

- Alternative definition

	`Define alternative actions to be taken to improve the different attributes`

- Conversion strategy definition
    
	`Decisions for each unit, based on time and costs constraints`

  
In general, this method gives the opportunity to have a systematic decision-making process with proposed rules. 

### 4. “A Framework to Assess Legacy Software Systems”, by Basem Y. Alkazemi [5]


This topic’s main goal is also to propose an assessment framework to create flexibility in systems with legacy software, with focus on architectural aspects.

So, the framework has **4 main strategies** to identify appropriate system evolution:

- replacing system with new enterprise solution
- maintain legacy system with limited evolution
- create whole new architecture for such systems with same functionality
- expand legacy system, adding  interaction with new systems

For proper assessment, author provides its dimensions:

- Support (hardware and software)
- Business (keep, replace or shut down the system)
- Architecture (style and integration patterns)
- Technology (type of technologies adopted by the system)

  
Later, a case study conducted in real organisation (UQU in Saudi Arabia) is presented. Legacy systems in this company were assessed using the proposed framework. Results were placed in the table divided by 4 dimensions and various factors with statuses.

Usage of this framework helped to understand strong points and weaknesses of the company’s processes, and results were also placed in a weighted table for decision-making. In this particular example, advantages of the existing system overweighted disadvantages.

 The key outcomes of this study should be useful to help the CEO of the university to make an informed decision about the ability of the current systems to serve its mission and subsequent objectives.

  
### 5. “Managing legacy system costs: A case study of a meta-assessment model to identify solutions in a large financial services company”, by James Crotty, Ivan Horrocks [6]

This paper relates to the previous three with some analysis. Authors assume that assessment would require more comprehensiveness, so they proposed a new meta-model derived from the three existing models combining business and technical factors with architecture attributes and some considerations.

The created approach will be more unified and extensive, and this may help dealing with real legacy systems.

Output results may be placed on decisional matrix, the same as in some previous methods. But, this metamodel combines existing attributes, so their mix really could be more descriptive (figure 2).
![image2.png](image2.png)

Figure 2 - attributes of meta-model

The decision matrix may be the same as in Sommerville’s paper [3] - business values and technical quality.

  
These parameters were used in a case study, which was conducted in a large UK financial services company - FinCo. 

This organisation has a huge system, CSS (which supports the majority of the firm’s business operations, accounts for 75–80% of the annual IT budget). 

Main method for data collection was questionnaire, which was focused on:

- The applicability of the proposed definition of legacy systems to FinCo’s CSS system.  
- The applicability of the proposed meta-model’s business and technical attributes to FinCo.  
- An estimated measure of each business and technical attribute for FinCo’s core system. 
-  The applicability of the proposed meta-model’s organisational attributes to legacy system solution selection for FinCo.  
- An estimated measure of each organisational attribute for FinCo

Also, CSS system was assessed in order to check, is it legacy or not. 10 respondents answered 11 questions each. In result, the system was considered as legacy ( 75/110 points for ‘yes’). Questions were about documentation, prior changes, management quality, and support quality.

There was a second calculation for usage of business value attributes in legacy systems. 

It was more complex, having 10 business attributes and in-depth analysis of responses with value index derived from re-coded attribute values.

The third study was about  23 technical value attributes. When asked whether these are used in assessing the legacy systems in FinCo, 60% of the 230 responses were positive. 


All results later were used in decisional matrix ( with business and technical attribute values, figure 3):

![image3.png](image3.png)

Figure 3 - decision matrix

Later, business and technical values were calculated for the input of each of the ten respondents and plotted together with the aggregated value for FinCo in the decisional matrix.

These actions and calculations provided proposed actions for this particular company - a complete reengineering with addressing architectural style and consumption constraints, source code translation, operating system and hardware replacement and outsourcing of data centre management.

In conclusion, this paper provided a different approach for the legacy systems improvement - a construct meta-model.
# Discussion 💬 and  Conclusions 🏁

Basically, there is some discussion in papers’ analysis, so main idea is that there no universal solution, and:

- you must know what the legacy system is
- you must know why you need to assess systems
- you need to use existing assessment methods carefully, adjusting when it is needed and possible
- you may create a whole new framework for the legacy system, which can combine existing methodologies

In general, legacy systems in one way or another will continue to appear (methodologies for the system creation, technologies themselves and business goals are changing), so organizations must be prepared to do something related to the work discussed in this topic. It is always better when these measurements and assessments are meaningful and useful in actual work, so system evolution will be relatively easy.

# References 📚

[1] IBM, ”Data Integrity Issues: Examples, Impact, and 5 Preventive Measures”, 2023. URL : [https://www.ibm.com/think/insights/data-integrity-strategy](https://www.ibm.com/think/insights/data-integrity-strategy)

[2] Sivakumar Ponnusamy and Dinesh Eswararaj, “Navigating the Modernization of Legacy Applications and Data:Effective Strategies and Best Practices”, Cognizant Technology Solutions, Richmond, VA, 2023. URL: [http://archive.sdpublishers.com/id/eprint/2053/1/Ponnusamy1642023AJRCOS108612.pdf](http://archive.sdpublishers.com/id/eprint/2053/1/Ponnusamy1642023AJRCOS108612.pdf)

[3] Jane Ransom, Ian Sommerville, and Ian Warren, “A Method for Assessing Legacy Systems for Evolution”, Computing Dept., Lancaster University, 2002. URL : [https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=9ada9f5a72f7bb52a4cef494b69766f5518d7826](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=9ada9f5a72f7bb52a4cef494b69766f5518d7826)

[4] Andrea De Lucia, Anna Rita Fasolino, Eugenio Pompella, “A Decisional Framework for Legacy System Management”, Faculty of Engineering - University of Sannio, 2002.  URL : [https://dl.acm.org/doi/pdf/10.1109/ICSM.2001.972781](https://dl.acm.org/doi/pdf/10.1109/ICSM.2001.972781)

[5] Basem Y. Alkazemi “A Framework to Assess Legacy Software Systems”, Department of Computer Science, Umm Al-Qura University, 2014. URL : [https://www.jsoftware.us/vol9/jsw0901-15.pdf](https://www.jsoftware.us/vol9/jsw0901-15.pdf)

[6] James Crotty, Ivan Horrocks, “Managing legacy system costs: A case study of a meta-assessment model to identify solutions in a large financial services company”, School of Engineering and Innovation, Faculty of Science, Technology, Engineering and Maths, The Open University, 2016. URL : [link](https://pdf.sciencedirectassets.com/280412/1-s2.0-S2210832717X00033/1-s2.0-S2210832716301260/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCT8FfmRrKakPVg0XESgWRlNUua5%2BGv%2F8vajA9Tt%2FKMewIgVzvvdGjgzN2JGDloZp08Rr3RN0EGEeQc%2BG1uosnPEBYqvAUIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAFGgwwNTkwMDM1NDY4NjUiDBXa6Ssnm%2B81d1lTkyqQBbt5iFkLC6GJLtDgGQDWlfcDi0MXivKrmy0mWUs3spCKgPqfAI2WY6LXOj4M%2BNC0zQIz2XKT6dlulDjMhRFop%2FvMry3HPnNCjIBiqyfso1tQdqu7YgM4b2Bw5zoPsnxVnca5SWLastohKdWYWzvzVHI%2Fz%2BYypBhKTJawa5Uk9O%2F5pPiG00GR3aoV7PWe%2Fd%2FxV%2Bcsw%2ByvMJlwzk%2Bzk%2B4Mr5Uc%2BCAaM63ShAgKNlchKbgSoJsieCBATEB2vBx2EJXg%2Fj5I9%2B0DoMsHOa67JHLLEP9hPfqAEBFQ8gRrYsVVFLvsvpKHWqSNbworlDaHeP%2F4O%2BcDEwn0gqlnvaUh9qyu291U0YICmitSKUAzxjf1%2FLUB9sDGedhv5hKZqvOTk9YRT%2Fu%2FthMgp%2FzCltV7bjNrCDwjAjQbBjPRxibq0zHlEfgc9pVMEfvLgl7%2FujzdRveKyobFpc9liEMi1LcOxDv8p0w4jD0rCZgNvQGrYrw7y8hpVGH5D%2B1NF9QnaKb11w%2FGVJKa1keQSjIhjdpPmB6uK1AXf7yG7iGZdCMbXSX5jHXQbMR9LOBsszABNSokEZg%2FSeQFVPygdVoUr4U97e8nH7Y02eubTm93Xseen5okkynIyiKxmOWxl9XtzDgnge9so3yFR6bM9Yaa%2BAa03Igb4M4vyGK8AQrAse4ICpIK0oojZ9ldtYZrPEXsj73i%2BNTspMOq4HBW3ayhT6tvtIs9OXez%2Fn%2B1jGlcK3KqMlHsbwmZc0fypETwyL%2FKMrBzMnZl3UOZ2A6Axeud%2FLRGQRcl2Yb68jf%2BWXdwDRD9p7kR7VcszKTYgRp%2Fp%2BPU%2BmhxPnLMUWK9iMqFaR%2BGXrdNxFEzWug4%2FfhI55NPvMdpp9ZSMTEMMMnZ6LoGOrEB%2FiMfAUOOQsmBN7FSkKFd5QZeyrYrQThYYnmdNYipspCRwthcwVyPJn4xMWDzIVB1hZ0QgZFMq%2FF%2Fij66pUapfajwid88zkmfAumU1GHedYF7Ww%2FJ9PNoYHNgYDMb0X2cjU%2BdvYkSm2DRMKTzPr1w0zB%2BNk7qHUEsf2qwlQgmCRSuUUSeAkiG6g8YVYj%2BtD8WI8IvxL%2Fr0w%2BH72ANhPAVflb%2FG4TUFtur7NsYW%2BogVLra&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241212T011156Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY4YSFX3S7%2F20241212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e71762288b33d5f86c059a6c0305b6ee652b2832a3afa894949643f1541b337b&hash=3546ab832178d691183a54d9e4b78b407351cbcdad9d566230c7497d9a741f57&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2210832716301260&tid=spdf-4eccb40b-3d16-4197-85cc-59322de77d86&sid=30ba88962e913844bd3979099a2c4d435c41gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=14155e02565b0b520700&rr=8f09d7dcafde5f92&cc=ru)

# 6.🔔 AI-Generated Content Disclaimers 🤖

no AI usage 