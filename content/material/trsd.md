---
parent: Case Materials
title: TRS Description
nav_order: 1
page_type: case
layout: default
---
# Time Reporting System — System Description

## 1) Overall Context

The **Time Reporting System (TRS)** lets employees report hours worked against customer projects so customers can be billed. Hours are charged to **Pay Codes** (each Pay Code = unique _project + task_). Employees may only charge to Pay Codes for which they have a **charge authorization**.

Because many employees work at customer sites, TRS must support **remote access via web** with no local installs, and run seamlessly on **Chrome, Safari, and Firefox**.

To reduce misuse or tampering, access is **password-protected** and **Pay Code creation is separated from charge authorization**. Worked hours can be approved **only** by the supervisor who **created** the relevant authorization **or their delegate** (delegation is scoped to a specific employee). A supervisor **cannot authorize themself** to charge to a Pay Code.

Approved timesheets are exported to the **Payroll System**, which the organization uses for payroll and **downstream billing**.

---

## 2) System Context

**Purpose & scope.** The diagram shows the **TRS boundary**, the **human actors**, and the **two system-to-system interfaces**.

### 2.1 UML Use Case Diagram

```mermaid
flowchart LR
  classDef actor fill:#fff,stroke:#555,stroke-dasharray:4 2
  classDef main fill:#fde68a,stroke:#b45309,stroke-width:3px,color:#111

  %% Human actors
  emp["👤 Employee"]:::actor
  sup["👤 Supervisor"]:::actor
  adm["👤 Administrator"]:::actor

  %% External systems
  Perso["🗄️ Personnel System"]:::actor
  Payroll["💶 Payroll System"]:::actor

  %% System boundary
  subgraph TRS["Time Reporting System"]
    useOperate(("Operate Time Reporting System")):::main
    ucEmpSync(("Synchronize<br>Employee<br>Data"))
    ucTsExport(("Export<br>Approved<br>Timesheets"))
  end

  %% Associations
  emp --> useOperate
  sup --> useOperate
  adm --> useOperate

  Perso --> ucEmpSync
  ucTsExport --> Payroll

  %% Show they are part of overall operation
  ucEmpSync --- useOperate
  ucTsExport --- useOperate

```

### 2.2 Actors at the boundary

- **Employee** — performs day-to-day time reporting.
    
- **Supervisor** — creates charge authorizations, delegates approval, and approves timesheets.
    
- **Administrator** — manages account access and the Pay Code catalog.
    
- **Personnel System (Perso)** — inbound HR/master data for employees and reporting lines.
    
- **Payroll System** — receives **approved** timesheets for payroll and downstream billing.
    

### 2.3 Information flow & boundary rules

- Direction on arrows indicates who initiates and where data goes (e.g., **Perso → TRS**; **TRS → Payroll**).
    
- Context-level only: internals (DB, screens, services) are out of scope here.
    

---

## 3) Time Reporting Subsystems

- **Access Control** — login and RBAC; **Admin maintains**, **Supervisor/Employee consume**.
    
- **Pay Code** — catalog of chargeable codes (project+task); **Admin maintains**.
    
- **Employee** — employee reference data (incl. supervisor reporting line from Perso).
    
- **Charge Matrix** — the **authorization map** (which employees may charge which Pay Codes); **Supervisors own** it.
    
- **Timesheet** — employees enter/submit; supervisors approve/reject according to the Charge Matrix rules.
    

### 3.1 Operational story

1. **Admins** maintain Access Control and the Pay Code catalog.
    
2. **Supervisors** build the Charge Matrix (authorizations) and approve Timesheets they own (or via valid delegation).
    
3. **Employees** authenticate, see **only authorized** Pay Codes, and create/submit Timesheets.
    

### 3.2 Global UML Class Diagram

```mermaid
classDiagram
class AdminService
class SupervisorService
class EmployeeService

class AccessControl
class AccountAccess {
  +accessId
  +role        %% EMP / SUP / ADM
  +status      %% Active / Blocked
}
class PayCode {
  +payCodeId
  +projectId
  +taskId
  +description
  +active
}
class Employee {
  +employeeId
  +name
  +orgUnit
}
class Supervisor {
  +supervisorId
}
class Authorization {
  +authorizationId
  +createdBySupervisorId
  +validFrom
  +validTo
}
class ChargeMatrix {
  +matrixId
  +name
  +effectiveFrom
  +effectiveTo
}
class Timesheet {
  +timesheetId
  +periodStart
  +periodEnd
  +status
}
class TimesheetRow {
  +rowId
  +workDate
  +hours
  +notes
}

note for AdminService "Administrator Functions"
note for SupervisorService "Supervisor Functions"
note for EmployeeService "Employee Functions"
note for ChargeMatrix "Charge Matrix<br>(authorization map)"
note for AccountAccess "TRS account access record<br>(roles / status)<br>Not a charge authorization."

%% Inheritance
Employee <|-- Supervisor : inherits

%% Domain relationships
Authorization "1" --> "1" Employee : employee
Authorization "1" --> "1" PayCode  : payCode
Authorization "1" --> "1" Supervisor : createdBy
ChargeMatrix "1" --> "0..*" Authorization : entries
Employee "0..*" --> "0..1" Supervisor : reportsTo
Timesheet "1" --> "1" Employee : for
Timesheet "1" --> "1..*" TimesheetRow : contains
TimesheetRow "1" --> "1" PayCode : chargedTo
AccountAccess "1" --> "1" Employee : for employee

%% AccessControl usage verbs (standardized)
AdminService ..> AccessControl : manage (roles,resets)
SupervisorService ..> AccessControl : check RBAC
EmployeeService ..> AccessControl : authenticate

%% Services' main dependencies
AdminService ..> PayCode : maintain catalog
AdminService ..> AccountAccess : grant/revoke/block
SupervisorService ..> ChargeMatrix : manage
SupervisorService ..> Authorization : create/maintain
SupervisorService ..> Timesheet : approve/reject
EmployeeService ..> ChargeMatrix : lookup eligible codes
EmployeeService ..> Authorization : check eligibility
EmployeeService ..> Timesheet : create/submit/recall

```

---

## 4) Supervisor Functions

- **Login → Access Control** — RBAC is checked for supervisor capabilities.
    
- **Create/Delete Charge Authorization** — grants/removes an employee’s ability to charge a Pay Code (project+task). The record is stored in the **Charge Matrix** and marked with **createdBy** (the owning supervisor).
    
- **Delegate Approval / Revoke Delegation** — a supervisor may delegate **approval authority for a specific employee** to another supervisor for a validity window.
    
- **Approve Timesheet** — approves/rejects employee Timesheets. Approval is allowed when the approver is **the Authorization.createdBy** **or** has a **valid Delegation** for that **employee**.
    
- **Supervisor Report** — reports over authorizations and Timesheet status/activity.
    

### 4.1 Supervisor UML Class Diagram

```mermaid
classDiagram
class SupervisorService

class AccessControl
class PayCode
class Employee
class Supervisor {
  +supervisorId
  +name
}
class Authorization {
  +authorizationId
  +createdBySupervisorId
  +validFrom
  +validTo
}
class ChargeMatrix {
  +matrixId
  +name
  +effectiveFrom
  +effectiveTo
}
class Delegation {
  +delegationId
  +delegatorSupervisorId
  +delegateSupervisorId
  +employeeId
  +validFrom
  +validTo
}
class Timesheet
class TimesheetRow
class SupervisorReport

note for SupervisorService "Supervisor Functions"
note for ChargeMatrix "Charge Matrix<br>(authorization map)"
note for Delegation "Delegation of approval authority<br>scoped to a specific Employee"
note for SupervisorReport "Reporting/queries<br>for supervisors"

%% Inheritance (kept across all diagrams)
Employee <|-- Supervisor : inherits

%% Domain relationships
Authorization "1" --> "1" Employee : employee
Authorization "1" --> "1" PayCode  : payCode
Authorization "1" --> "1" Supervisor : createdBy
ChargeMatrix "1" --> "0..*" Authorization : entries
Employee "0..*" --> "0..1" Supervisor : reportsTo
Timesheet "1" --> "1" Employee : for
Timesheet "1" --> "1..*" TimesheetRow : contains
TimesheetRow "1" --> "1" PayCode : chargedTo

%% Delegation scope & parties
Delegation "1" --> "1" Supervisor : delegator
Delegation "1" --> "1" Supervisor : delegate
Delegation "1" --> "1" Employee   : for

%% Service dependencies
SupervisorService ..> AccessControl : check RBAC
SupervisorService ..> ChargeMatrix : manage
SupervisorService ..> Authorization : create/maintain
SupervisorService ..> Delegation : delegate/revoke
SupervisorService ..> Timesheet : approve/reject
SupervisorService ..> SupervisorReport : generate

SupervisorReport ..> Timesheet : read
SupervisorReport ..> ChargeMatrix : read
SupervisorReport ..> Employee : read
SupervisorReport ..> PayCode : read

```

**Approval policy for mixed Pay Codes.** Approvals are **per TimesheetRow** (per charged Pay Code). A Timesheet becomes **Approved** when **all** rows are approved; otherwise it remains **Partially Approved** or **Submitted** (policy name up to the team).

---

## 5) Employee Functions

- **Login → Access Control** — the employee authenticates.
    
- **Report Time** — create time entries (date, Pay Code, hours, notes).
    
- **Modify Timesheet** — edit Draft entries.
    
- **Submit Timesheet** — move to **Submitted** for supervisor action (usually locks edits).
    
- **Recall Timesheet** — move back to **Draft** (allowed **until any row is approved**).
    
- **Employee Report** — personal summaries (hours by period/Pay Code, statuses).
    

### 5.1 Operational story

1. Employee authenticates.
    
2. Employee records time, with available Pay Codes filtered by the **Charge Matrix** (must be authorized).
    
3. Employee can modify until submission; after submission, they can **recall** (unless any row was already approved).
    
4. Employee may view reports at any time.
    

### 5.2 Timesheet lifecycle (policy)

```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Submitted : submit()
  Submitted --> Draft : recall()<br>(allowed until<br>any row approved)
  Submitted --> Approved : all rows approved
  Submitted --> Rejected : any row rejected<br>and returned
  Rejected --> Draft : amend()
  Rejected --> [*]
  Approved --> [*]

```



### 5.3 Employee UML Class Diagram

```mermaid
classDiagram
class EmployeeService

class AccessControl
class PayCode
class Employee {
  +employeeId
}
class Supervisor {
  +supervisorId
}
class Authorization {
  +authorizationId
  +validFrom
  +validTo
}
class ChargeMatrix {
  +matrixId
}
class Timesheet {
  +timesheetId
  +status
}
class TimesheetRow {
  +workDate
  +hours
}
class EmployeeReport

note for EmployeeService "Employee Functions"
note for ChargeMatrix "Charge Matrix<br>(authorization map)"
note for EmployeeReport "Employee self-service reports"
note for Timesheet "Lifecycle:<br>Draft <-> Submitted (Recall).<br>Approved when all rows approved."

%% Inheritance (kept across all diagrams)
Employee <|-- Supervisor : inherits

%% Domain relationships
Authorization "1" --> "1" Employee : employee
Authorization "1" --> "1" PayCode  : payCode
ChargeMatrix "1" --> "0..*" Authorization : entries
Timesheet "1" --> "1" Employee : for
Timesheet "1" --> "1..*" TimesheetRow : contains
TimesheetRow "1" --> "1" PayCode : chargedTo

%% Service dependencies
EmployeeService ..> AccessControl : authenticate
EmployeeService ..> ChargeMatrix : filter pay codes
EmployeeService ..> Authorization : check eligibility
EmployeeService ..> Timesheet : report / modify / submit / recall
EmployeeService ..> EmployeeReport : generate

EmployeeReport ..> Timesheet : read
EmployeeReport ..> PayCode : read
EmployeeReport ..> Authorization : read
EmployeeReport ..> ChargeMatrix : read

```

---

## 6) Administrator Functions

Two areas, both gated by Login/Access Control:

1. **Employee account & access management**
    
    - **Grant TRS Account Access** (provision/activate account with role).
        
    - **Revoke TRS Account Access** (permanently remove access).
        
    - **Block Account** (temporary disable).
        
    - **Reset Password**.
        
2. **Pay Code catalog lifecycle**
    
    - **Create / Update / Delete Pay Code** entries used by other subsystems.
        

> Terminology: These are **account access** operations (not charge authorizations). Charge authorizations are in the Supervisor area via the **Charge Matrix**.

### 6.1 Admin UML Class Diagram

```mermaid
classDiagram
class AdminService

class AccessControl
class Employee {
  +employeeId
}
class Supervisor {
  +supervisorId
}
class AccountAccess {
  +accessId
  +role
  +status
}
class PayCode {
  +payCodeId
}

note for AdminService "Administrator Functions"
note for AccountAccess "TRS account access<br>(grant/revoke/block/reset).<br>Not a charge authorization."
note for PayCode "Project+Task catalog entry<br>(created/updated/deleted by Admin)."

%% Inheritance (kept across all diagrams)
Employee <|-- Supervisor : inherits

%% Relationships
AccountAccess "1" --> "1" Employee : for employee

%% Service dependencies
AdminService ..> AccessControl : manage (roles,resets)
AdminService ..> AccountAccess : grant / revoke / block
AdminService ..> Employee : manage profile (optional)
AdminService ..> PayCode : create / update / delete

```

---

## 7) The contract

Your company bids for a **turnkey** contract: it builds TRS, deploys it, and supports it after
launch. The client is a large consulting firm with **four offices** across the country. TRS
replaces the firm's existing **mainframe** time reporting application.

The contract obliges your company to deliver:

- a **specification** with wireframes and navigation diagrams, approved by the client;
- the software, in **three increments**, each one demonstrated to the client;
- the **data migration**: the client's IT department sends the old data as CSV files **one week
  before launch**, and your company loads them;
- the **training material**: the client's HR department runs the training, and needs the material
  **two weeks before** the training session;
- the **acceptance test procedure**: the client's IT department runs acceptance, and needs the
  procedure **at least one week before** the test;
- **30 days of support** after deployment.

### 7.1 Payment schedule

| # | Milestone | Payment |
|---|---|---|
| 1 | Specification approved, including wireframes and navigation diagrams | 5% |
| 2 | Data migrated from the old system to the new one | 5% |
| 3 | Each increment demonstrated (three in total) | 20% each |
| 4 | User training completed | 10% |
| 5 | System accepted | 10% |
| 6 | 30-day post-deployment support period completed | 10% |

---

## 8) Function list

The names used in C4, C5 and C6. Twenty-two functions: nineteen the client ranks in C6, plus
two system interfaces and the data load.

| # | Function | Actor | Section |
|---|---|---|---|
| 1 | Login | all users | §3, §5 |
| 2 | Grant Account Access | Administrator | §6 |
| 3 | Revoke Account Access | Administrator | §6 |
| 4 | Block Account | Administrator | §6 |
| 5 | Reset Password | Administrator | §6 |
| 6 | Create Pay Code | Administrator | §6 |
| 7 | Update Pay Code | Administrator | §6 |
| 8 | Delete Pay Code | Administrator | §6 |
| 9 | Create Charge Authorization | Supervisor | §4 |
| 10 | Delete Charge Authorization | Supervisor | §4 |
| 11 | Delegate Approval | Supervisor | §4 |
| 12 | Revoke Delegation | Supervisor | §4 |
| 13 | Approve Time Sheet | Supervisor | §4 |
| 14 | Supervisor Report | Supervisor | §4 |
| 15 | Report Time | Employee | §5 |
| 16 | Modify Time Sheet | Employee | §5 |
| 17 | Submit Time Sheet | Employee | §5 |
| 18 | Recall Time Sheet | Employee | §5 |
| 19 | Employee Report | Employee | §5 |
| 20 | Synchronize Employee Data | Personnel System | §2 |
| 21 | Export Approved Time Sheets | Payroll System | §2 |
| 22 | Import Legacy Data | client IT (CSV) | §7 |

*Grant / Revoke Account Access* and *Block Account* are account operations. They are **not**
charge authorizations (see the note in §6).

---

## 9) After the contract is won (C5, C6)

- **Team:** two developers and one tester, 40 hours a week each. A working day is 8 hours,
  Monday to Friday. Ignore public holidays. You are the project manager; your hours are not in
  the team's.
- **Kick-off:** Monday 11 January 2027.
- **Development starts:** Monday 1 February 2027, after the specification is approved.
- **Operational deadline:** TRS is live no later than Tuesday 1 June 2027.

---

## Acknowledgments

The Time Reporting System, its description and the three assignments are adapted from
**Eduardo Miranda**'s course material on estimating and planning software projects (TRS
description 2009; critical-path and milestone assignments 2013), taught with **David Root**.

## Sources

- Miranda, Eduardo. *Time Reporting System — System Description.* Course material, 2009.
- Miranda, Eduardo. *Critical Path* and *Developing a Milestone Plan.* Assignments, 2013.
- Miranda, Eduardo. "Time-boxing planning: Buffered MoSCoW rules." *ACM SIGSOFT Software
  Engineering Notes* 36(6), 2011, 1–5.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
