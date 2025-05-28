---
parent: Testing
nav_order: 2
title: Levels
layout: default
---


# ✅ Testing Techniques Structured by Levels

Software testing can be classified based on the *scope* or *level* of the system being tested. The goal is to verify software components in increasing scale and complexity—from individual functions to the entire system.

---

### 📋 Summary Table

| **Level**                     | **Description**                                                          |
| ----------------------------- | ------------------------------------------------------------------------ |
| **Unit Testing**              | Tests a single unit (e.g., function, method, object) in isolation.       |
| **Integration Testing**       | Tests interactions between multiple units or components.                 |
| **Thread / Function Testing** | Tests workflows or execution paths involving multiple interacting units. |
| **System Testing**            | Tests the complete and integrated system as a whole.                     |
| **Medium Testing**            | An intermediate testing level between unit and system testing.           |

---

## 🧪 Unit Testing

* A **unit** is typically a function, method, or class written by a developer.
* Unit testing focuses on **internal correctness** of that unit.
* It’s usually done **early** in development, before or after code reviews.
* **Simulated environment**: Uses *stubs* (dummy functions) and *drivers* (test harnesses).
* **Common faults**: Incorrect logic, boundary issues, data corruption, etc.
* **Test adequacy**: Measured using:

  * **Statement/branch coverage**
  * **Path coverage**
  * **MC/DC** (Modified Condition/Decision Coverage)
  * **Mutation testing**

### 🛒 Example: Unit Test of `Order` Object

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

### 🧪 Mocking in Unit Testing

Mocking simulates dependencies (like APIs or databases) to isolate the unit being tested.

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

---

## 🔗 Integration Testing

* Combines two or more **interacting units** and tests their interaction.
* **Typical faults**:

  * *Interface misuse*: Incorrect parameter usage or function calls.
  * *Interface misunderstanding*: Incorrect assumptions about a function’s behavior.
* Usually performed by developers or a dedicated testing team.
* **Test environment**: Development or staging.
* **Adequacy**: Measured via **node/edge coverage** of immediate connections.

### 🧪 Integration Test Example

```mermaid
sequenceDiagram
    actor Customer
    participant SC as ShoppingCart
    box "Integration Test"
        participant O as Order
        participant I as Item
    end

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```

---

## 🔁 Thread / Function Testing

* Tests **end-to-end workflows** or **execution paths** that span multiple components.
* Focuses on *functional correctness* of operations from input to output.
* Runs in a development or pre-production environment.
* Faults and defects are logged and reported for triaging.

### 🧪 Function Test Example

```mermaid
sequenceDiagram
    actor Customer
    box "Function Test"
        participant SC as ShoppingCart
        participant O as Order
        participant I as Item
    end

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```

---

## 🖥️ System Testing

* Involves testing the **entire application**, including all subsystems and integrations.
* **Goal**: Validate that the system meets all **functional and non-functional** requirements.
* **Environment**: As close as possible to production.
* Performed by **independent QA** teams, not the developers.
* **Common issues** found:

  * Faulty interactions between components
  * Negative test cases (e.g., incorrect user input)
* **Adequacy** measured using:

  * **Combinatorial coverage**
  * **Mutation testing**

### 🧪 System Test Example

```mermaid
sequenceDiagram
    box "System Test"
        actor Customer
        participant SC as ShoppingCart
        participant O as Order
        participant I as Item
    end

    Customer->>SC: Add items and get total
    SC->>O: Create order
    O->>I: Get item prices
    I-->>O: Return item prices
    O-->>SC: Return total price
    SC-->>Customer: Display total price
```