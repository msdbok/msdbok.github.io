---
parent: Testing
nav_order: 5
title: Purpose-based
layout: default
---


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

