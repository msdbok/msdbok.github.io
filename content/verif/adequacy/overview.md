---
title: Overview
parent: Adequacy
nav_order: 1
layout: default
---

# Adequacy criteria & coverage

Coverage measures the thoroughness of the testing. The quality of the application is measured indirectly under the assumption that a more thorough testing will uncover more faults than a less thorough one
Adequacy criteria: A measurable condition of what needs to be achieved by a test suite 
White box criteria - Structural
All statements are executed
All branches of all control statements are executed
All basis paths are executed
All definition – uses of a variable are tested
All mutants of a given program are killed
Black box criteria - Requirements / Specification based criteria
All unique combinations of n parameters are used as testing inputs
N-Switch coverage

Coverage is a measure of the extent to which a the condition has been satisfied

Selecting a large number of tests that always test the same portion of the code is not very helpful. What we need to know is the extent to which test planning and execution ensure thorough execution of the system. What criteria can be used to ensure the thorough testing? 

To do this testers typically use the coverage criteria, although there are other, e.g. we exhausted the test cases or the budget. As a minimum testers will strive to cover all statements (executing each source line at least once) and covering inputs (applying each externally generated event). But if code and input coverage were sufficient, released products would have very few bugs. 

Concerning the code, it isn’t individual code statements that interest testers but execution paths: sequences of code statements representing an execution of the software. Unfortunately, there are an infinite number of paths. Concerning the input domain, it isn’t the individual inputs that interest testers but input sequences that, taken as a whole, represent scenarios to which the software must respond. There are an infinite number of these, too.

To further complicate things these criteria are used not only as a measurement instrument but as test case generator and sometimes as an stopping rule.

Coverage criteria are traditionally used in one of two ways. One method is to
directly generate test case values to satisfy a given criterion. This method is often
assumed by the research community and is the most obvious way to use criteria. It is
also very hard in some cases, particularly if we do not have enough automated tools
to support test case value generation. 

The other method is to generate test case
values externally (by hand or using a pseudo-random tool, for example) and then
measure the tests against the criteria in terms of their coverage. This method is
usually favored by industry practitioners, because generating tests to directly satisfy
the criteria is too hard.

## Coverage measures can be applied to almost any verification activity

Coverage measures can be applied to any verification activity, although they are most frequently applied to testing activities. Appropriate coverage measures give the people doing, managing, and auditing verification activities a sense of the adequacy of the verification accomplished

We can measure coverage on any artifact produced during software development, e.g., structural coverage of source code, coverage of input space, coverage of complex inputs - e.g., grammar based, coverage of specification, coverage of test
models, coverage of requirements, coverage of GUI elements, ...

Exception exploratory testing


## Non-exhaustive list of adequacy criteria

![alt text](image.png)

LCSAJ – Linear Code Sequence and Jump
MC/DC – Modified Condition/Decision Coverage
DU – Definition Use pairs


Only in the case where we keep other things unchanged adequacy/coverage will measure test effectiveness. In general adequacy/coverage are a measure of the thoroughness of the testing.

A criterion C1 includes (or subsumes) the criterion C2 if for every program P and its specification S, any set of test cases that satisfy C1 also satisfy C2. This relation is represented as C1=> C2, and is a transitive  relation. 

One may think that if C1 => C2, testing based on C1 will always be better than testing based on C2. This is not the case because the fault-detection capability of a set of test cases T that satisfy a criterion C depends on the actual test cases in T and not just C (i.e., the criterion is not valid). In other words, if Ti and T2 both  satisfy C for a program does not imply that T1 and T2 will execute the same paths of P and detect the same faults in P. Because the actual test cases also play a role in whether or not an error in a program is detected, in general, it is possible to have a situation where Ci => C2, Ti satisfies Ci, T2 satisfies C2, but T2 detects an error that Ti does not. However, if similar methods are used for test case generation then, generally speaking, Ci will be better for testing than C2 if Ci =^ C2.

## Adequacy criteria selection

Purpose of the testing activity
Source code availability and relevance
Targeted faults (underlying fault model)
Compliance requirements


## Criteria hierarchy

In general, the higher in the hierarchy the criteria, the more thorough the testing. 
It is possible however, to have a situation where Ci subsumes Cj, Ti satisfies Ci, Tj satisfies Cj, but Tj detects an error that Ti does not


### Example
![alt text](image-1.png)
Criteriai : Branch coverage
Test suitei : a = 0; a = 2

Criteriaj : Statement coverage
Test suitej : a = 1


## Terminology

### Decisions, conditions & branches

![alt text](image-2.png)

*(Adapted from A. Hass, Guide to Advanced Software Testing, 2008)*

The first concept is that of a statement. An executable statement is defined as a non-comment or nonwhite space entity in a programming language, typically the smallest indivisible unit of execution.

A group of statements always executed together—or not at all—is called a basic block. A basic block can consist of only one statement or it can consist of many. There is no theoretical upper limit for the number of statements in a basic block.

The last statement in a basic block will always be a statement that leads to another building block, or stops the execution of the component we are working with (e.g., return) or the entire software system (end).

The most interesting is, however, when a basic block ends in a decision, that is a statement where the further flow depends on the outcome of the decision.
Decision statements are for example IF … THEN …ELSE, FOR …, DO WHILE…, and CASE OF…. A decision statement is also called a branch point. A branch is a (virtual) connection between basic blocks. One or more branches will lead into a basic block (except to the first), and likewise there will be one or more branches leading out of a basic block (except the last).
The branches out of a basic block are connected to the outcomes of the decision, also called decision outcome or branch outcome. Most decisions have two outcomes (True or False), but some have more, for example Case statements.
The last concept is that of a condition. A condition is a logical expression that can be evaluated to either True or False. A decision may consist of one simple condition, or a number of combined conditions.

### Control flow graphs

Nodes correspond to statements or a block of statements
Edges model transfer of control (i.e. what is the next statement to be executed) within the program
Nodes with two or more output edges are decisions

A path through the software is a sequence of instructions or statements that starts at an entry, junction, or decision and ends at another, or possibly the same, junction, decision, or exit. A path may go through several junctions, processes, or decisions, one or more times. 

Often the first step in understanding the control flow of a program under test is to derive its control-flow graph (CFG). A control-flow graph is a connected directed graph composed of a set of nodes N and a set of edges E. The set of nodes will be regarded as containing two special nodes: a unique start-node and a unique end-node. Each node represents an individual statement in the program and each edge Z(ni, nj) represents a transfer of control flow from node ni to node nj. However, a more compact CFG can be constructed, without loss of relevant information, by partitioning the statements into basic blocks. A basic block is simply a sequence of one or more contiguous, executable statements such that the sequence has only one entry point (the first statement in the block), only one exit point (the last statement in the block), and no statement other than the last can give rise to branching of control flow. In this equivalent, but more compact CFG, each node represents a basic block rather than an individual statement and the edges are the possible control flow connections between the basic blocks.


#### Example


### Data flow criteria and data flow testing

Intuition:  Statements interact through data flow

The assumption behind data flow testing is that to test a program adequately, we should focus on the flows of data values:
A value computed in one statement is used in another
The computation of a bad value is only revealed when it is used
Data flow testing consists of the identification of relevant Definition Use pairs and the design of test cases that force the execution of the program thru them
As an adequacy criteria the number of paths satisfying the criteria (All DUs, All DEFs, All USEs) is counted and compared to the number of paths actually traversed as result of executing the test suite
Data flow testing should not be confused with data flow analysis which concerns itself with the avoidance of data anomalies, e.g. using an undefined variable, but not with the correctness of the computations

