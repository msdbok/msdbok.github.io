---
parent: Testing
nav_order: 9
title: ALL
layout: default
---

# 3. Testing

## What is testing?

INCOSE

    The verification method of determining performance by exercising or operating the system or item using instrumentation or special test equipment that is not an integral part of the item being verified. Any analysis of the data recorded in the test and that is needed to verify compliance (such as the application of instrument calibration data) does not require interpretation or interpolation/extrapolation of the test data. 

Software practitioner

    The (more or less) thorough execution of the software with the purpose of finding bugs before the software is released for use and to establish that the software performs as expected
Uses

    Verification of functional and performance requirements

Examples

    When provided with the correct user name and password the user is able to login into the system
    The software is capable of handling a load of thousand transactions per minute


> When we test something, our purpose is to make it fail. As a matter of fact  a good test case is one that uncovers a fault. Goal is to falsify the property, it is much easier then to prove correctness. 


## How tests can be classified? Taxonomy

by Level

    Unit
    Integration
    Thread, function, integration, unit, medium
    System

by Purpose or characteristic being tested

    Functional correctness
    Robustness
    Performance
    Regression
    Acceptance

by Source of test cases

    Specification (Black box testing)
    Structure (White box testing)
    Model based
    Experience (Exploratory testing)

by Targeted faults

    Computational
    Domain
    Variable interactions
    Value propagations
    Variable usages

by Test execution mode

    Manual
    Automated

### Unit testing

A “unit” (object, procedure, subprogram) usually created by a single developer
Typical faults: missing/wrong functionality, domain faults, data corruption, error conditions
Defects found are typically kept private and fixed by the same person that developed the code
Can take place before and/or after code review
Runs in a simulated environment (drivers and stubs)
Adequacy measured through statement, branch, basis path, MC/DC coverage or mutation testing

![alt text](image-2.png)

```mermaid
sequenceDiagram
    actor Customer
    participant SC as ShoppingCart
    box "Unit Under Test"
        participant O as Order
    end
    participant I as Item

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```

#### Mocking
```mermaid
sequenceDiagram
    actor Developer
    participant TestFramework
    participant CodeUnderTest
    participant MockService

    Developer->>TestFramework: Write test cases
    TestFramework->>CodeUnderTest: Call functions with inputs
    CodeUnderTest->>MockService: Send mock API call
    MockService-->>CodeUnderTest: Return mock response
    CodeUnderTest-->>TestFramework: Return output
    TestFramework->>Developer: Compare output with expected results
    alt Output matches expected
        TestFramework->>Developer: Test passed
    else Output does not match expected
        TestFramework->>Developer: Test failed
    end
```

### Integration testing

Involves two or more interacting units
Typical faults: Interface misuse and misunderstanding
The focus is on the adjacent interactions
Is performed by the developer of the unit being integrated or by a specialized function  
Defects are usually reported
Runs in a development environment
Adequacy measured through node or edge coverage of immediate neighbors


> Interface Misuse - A calling unit calls another unit and makes an error in its use of interface, probably by calling/passing parameters in the wrong sequence.
Interface Misunderstanding - A calling unit makes some assumption about the other unit’s behavior which is incorrect.

```mermaid
sequenceDiagram
    actor Customer
    participant SC as ShoppingCart
    box "Integration Test"
        participant O as Order
        participant I as Item
    end
    participant I as Item

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```


### Thread, function, integration testing

Involves two or more interacting units
Focus in end to end functionality
Is performed by the developer of the unit being integrated or by a specialized function  
Defects are usually reported
Runs in a development environment


```mermaid
sequenceDiagram
    actor Customer
    box "Function Test"
        participant SC as ShoppingCart
        participant O as Order
        participant I as Item
    end
    participant I as Item

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```

### System testing

Encompass end-to-end functionality and other system-level characteristics. 
Typical faults: Undesirable interactions, negative test cases
Is not performed by the developer
Defects are reported
Runs in a real environment
Adequacy measured by combinatorial coverage or  mutation testing


```mermaid
sequenceDiagram
    box "System Test"
        actor Customer
        participant SC as ShoppingCart
        participant O as Order
        participant I as Item
    end
    participant I as Item

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```


### Purpose-based testing

What things do we want to test? A non-exhaustive list of the software characteristic being tested

Functions. See that each function does what it’s supposed to do and not what it isn’t supposed to do
Look for any data processed by the product. Look at outputs as well as inputs
Decide which particular data to test with. Consider things like boundary values, typical values, convenient values, and invalid values
Consider combinations of data worth testing together

Regression - Re-testing of something that was already working, usually with existing test cases, to provide confidence that the system under test (SUT) still functions correctly following modification or extension of the system (such as user enhancements or upgrades or following new builds or releases of the software)


Scenarios. Test to a compelling story. Do one thing after another
Define test procedures or high level cases that incorporate multiple activities connected end-to-end 
Don’t reset the system between tests. 
Vary timing and ordering of events

Efficiency. Does the system provide appropriate performance, relative to the amount of resources used, under stated conditions


Performance testing
Testing done to evaluate system’s response time, throughput and resource utilization
Performed under “normal” operating conditions

Load testing
Process of exercising the system by feeding it the largest  specified task or workload

Stress testing
Trying to break the system  with the purpose of assuring  that the system fails and recovers gracefully. This testing is performed by overwhelming the system’s resources or by taking them away from it beyond the specified conditions

Robustness Testing. Imagine calamities. The possibilities are endless. How will the system react to them?

### White or black box testing?

#### White box testing

    Tests what is written, not what was intended
    Knowledge of the implementation helps to  include test cases that may not be identified from specifications alone
    Good for discovering additional, perhaps unwanted, functionality, e.g., intrusive or unreachable code
    Can be used to assess precisely what code features remain untested
    On its own, gives no indication of how thoroughly the stated requirements have been tested

![wb](image-3.png)

```mermaid
flowchart LR
    subgraph WhiteBox["White Box"]
        direction TB
        Code["If A then<br>   S1<br>Else<br>   S2<br>Endif  <br>If B then<br>   S3<br>Else<br>   S4<br>Endif"]

        A{Decision: A?} -->|True| S1[Statement S1]
        A -->|False| S2[Statement S2]
        S2 -->B
        S1-->B
        B{Decision: B?} -->|True| S3[Statement S3]
        B -->|False| S4[Statement S4]
    end

    Input1["Input A"] --> WhiteBox
    Input2["Input B"] --> WhiteBox

    WhiteBox --> Output1["Output X"]
    WhiteBox --> Output2["Output Y"]
```



##### More about WB
White Box Testing: Looking at the Code

Design test cases such as
    All the code statements have been executed
    Both branches of each condition have been executed
    All linearly independent paths have been traversed

> To stimulate the program we need inputs, how do we choose them? If we base our selection we might miss unspecified behaviors implemented in the program. If we select values based on the structure we might miss required behaviors that were not implemented. If the condition is not satisfied we will analyze the code to see what values must be provided as input to force the execution along the desired path

```mermaid

---
config:
  layout: fixed
---
flowchart TB
 subgraph Legend["Legend"]
        Passed["Passed by tests = green"]
        NotPassed["Not passed by tests = red"]
  end
    Start(["Start"]) --> D1{"Decision 1?"}
    D1 -- True --> S1["Statement S1"]
    D1 -- False --> S2["Statement S2"]
    S1 --> D2{"Decision 2?"}
    S2 --> D3{"Decision 3?"}
    D2 -- True --> S3["Statement S3"]
    D2 -- False --> S4["Statement S4"]
    D3 -- True --> S5["Statement S5"]
    D3 -- False --> S6["Statement S6"]
    S3 --> End(["End"])
    S4 --> End
    S5 --> S1
    S6 --> End
    style Passed fill:#d9fcd9,stroke:#008000,stroke-width:2px
    style NotPassed fill:#fcd9d9,stroke:#ff0000,stroke-width:2px
    style Start fill:#f9f9f9,stroke:#000,stroke-width:2px
    style D1 fill:#f9f9f9,stroke:#000,stroke-width:2px
    style S1 fill:#d9fcd9,stroke:#008000,stroke-width:2px
    style S2 fill:#d9fcd9,stroke:#008000,stroke-width:2px
    style D2 fill:#f9f9f9,stroke:#000,stroke-width:2px
    style D3 fill:#f9f9f9,stroke:#000,stroke-width:2px
    style S3 fill:#d9fcd9,stroke:#008000,stroke-width:2px
    style S4 fill:#fcd9d9,stroke:#ff0000,stroke-width:2px
    style S5 fill:#d9fcd9,stroke:#008000,stroke-width:2px
    style S6 fill:#fcd9d9,stroke:#ff0000,stroke-width:2px
    style End fill:#f9f9f9,stroke:#000,stroke-width:2px
    linkStyle 0 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 1 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 2 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 3 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 4 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 5 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 6 stroke:#ff0000,stroke-width:2px,fill:none
    linkStyle 7 stroke:#008000,stroke-width:2px,fill:none
    linkStyle 8 stroke:#ff0000,stroke-width:2px,fill:none
    linkStyle 11 stroke:#008000,stroke-width:2px,fill:none

```


#### Black box testing

    Good for identifying incorrect or missing implementation of stated requirements 
    Test cases can be written by users and technologist alike
    On its own, gives no indication of how thoroughly the program code has been tested
    Can be used to assess whether any features in the requirements remain untested

![bb](image-4.png)

```mermaid
flowchart LR
    subgraph BlackBox["Black Box"]
        direction TB
        Spec["Specification f(x, y, ...)"]
    end

    Input1["Input 1"] --> BlackBox
    Input2["Input 2"] --> BlackBox
    Input3["Input 3"] --> BlackBox

    BlackBox --> Output1["Output 1"]
    BlackBox --> Output2["Output 2"]
    BlackBox --> Output3["Output 3"]
```

##### More about BB

Black box testing: looking at the specification

    Identify the software under test
    Things that the product can do (functions and sub functions).
    Identify relevant test aspects
    Values and other attributes of the data
    Execution conditions
    Design test cases
    Decide which particular data to test with. Consider things like boundary values, typical values, convenient values, invalid values, or best representatives
    Consider combinations of data worth testing together
    Determine how would you’d know a function is working (expected test result) 
    Test each function, one at a time. See that each function:
    Does what it should do AND
    Does not do what it shouldn’t do


### White or black box testing? 

| **White Box Testing**                                                                 | **Black Box Testing**                                                          |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Tests what is written, not what was intended                                         | Good for identifying incorrect or missing implementation of stated requirements |
| Knowledge of the implementation helps include test cases that may not be identified from specifications alone | Test cases can be written by users and technologists alike                     |
| Good for discovering additional, perhaps unwanted, functionality (e.g., intrusive or unreachable code) | On its own, gives no indication of how thoroughly the program code has been tested |
| Can be used to assess precisely what code features remain untested                   | Can be used to assess whether any features in the requirements remain untested |
| On its own, gives no indication of how thoroughly the stated requirements have been tested |                                                                               |

## More BB techniques

### Exploratory testing: Based on the skill and experience of the testers

Useful…

    If few system specifications are available, but knowledge of the application and the anticipated goal are
    As a supplement to the “scripted” test design techniques

Limitations

    Poor exploration may result in a false sense of coverage and effectiveness
    Lack of repeatability. There is no guarantee that a particular function will be tested in the same way by a different tester

Two approaches

    Ad-hoc
    Session based

### Target fault model

Partition based testing. 

Assumptions about where the faults are most likely located or systematic exploration of the software. Points belonging to a partition are assumed to be “revealing” or equivalents

    Boundary value analysis
    Combinatorial
    Data flow
    States
    Negative testing

Random testing. 

All input points are unique. Effort is put into finding a suitable random distribution

    Random testing
    Fuzz testing

#### Partition testing

A partition is the division of the input domain of the software under test into a number of subsets (called equivalence classes) for which the behavior is assumed to be the same for all values belonging to the each of them

The partition criteria utilized is what differentiates one test design technique from another

> To keep down our testing costs, we don’t want to write several test cases that test the same aspect of our program. A good test case uncovers a different class of errors (e.g., incorrect processing of all character data). Equivalence partitioning is a strategy that can be used to reduce the number of test cases that need to be developed. Equivalence partitioning divides the input domain of a program into classes. For each of these equivalence classes, it is hypothesized that the set of data must be treated the same by the module under test and should then produce likely answers, if it does not then the test fails.

![alt text](image-5.png)

#### Random testing

The systematic variation of values through the input space with the purpose of identifying abnormal output patterns. 
When such patterns are identified a root cause analysis is conducted to identify the source of the problem. In this case the “state 3” outputs seem to be missing

(from. When Only Random Testing Will Do Dick Hamlet, 2006)

> Random testing is a technique which systematically explores the input space of the software under testing. This use of the term random is very different from other disciplines where random testing means selecting a few cases just by “chance”. To be effective and efficient random testing relies on the automatic generation of test inputs. The problem with random testing is how to verify that the results are those expected. This is known as the “oracle problem”.

> The solutions to the oracle problem fall into three categories: the use of a proxy to produce the correct results against the values produced by the new application will be checked. The proxy could be an existing system or a simple computational form. The second category is based on the recognition of patterns. Pattern recognition can take the form of curve fitting algorithms followed by a study of discontinuities in the output of the application or it can be in the form of assertions where a relation between variables is a specified and a violation of the assertion denotes a failure of the software. The breaking of a pattern can also be detected by visual inspection of a summary input like in the example shown. A third category consist in analyzing the states which result after the execution of the software with a certain data. A common example for this is fuzz testing in which the expected output from the test are that after processing the data the software exits normally. The software raises an exception indication an abnormal condition or the software crashes revealing an abnormal situation that it was not programmed to handle.

### Test execution

Manual execution

Automatic execution

    Capture/replay 
    Scripting
    Frameworks (Junit, TestNG)
    Continuous Integration (GitHub Actions, GitLab CI, …)

