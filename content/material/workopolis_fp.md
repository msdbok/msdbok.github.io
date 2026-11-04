---
parent: Case Materials
title: "Workopolis: a function-point count, worked"
nav_order: 5
page_type: case
layout: default
---

# Workopolis: a function-point count, worked

A rated **function-point count** turns a backlog into a size anyone can check: classify each file
and transaction, count its fields, subgroups and referenced files, rate it with the IFPUG tables and
add the weights. This page counts **Workopolis**, a job board of fifteen user stories
{% cite miranda2009sizing %}, from start to finish, then turns the count into hours. The stories give
no fields, so the data model below is **constructed** for the example. The rules and tables are on
[FPA explained](../scope/estimates/fpa_explained).

## 1. The files

Workopolis keeps three groups of data and reads one that another system maintains. No story creates
or changes a recruiter account, so for this application it is an external interface file. A resume
is part of a job seeker's profile, so it is a **subgroup** (a record element type) of that file, not a
file of its own. A career alert is a saved search the user manages as a list, so it is counted as a
file. Both are judgements about how the user sees the data; the other choices are counted in
section 3.

| File | Type | Fields | DET | RET | Rating | FP |
|---|---|---|--:|--:|---|--:|
| Job seeker | ILF | profile: name, e-mail, password, phone, city, desired job title, registered on · resume: document, document name, uploaded on | 10 | 2 | Low | 7 |
| Career alert | ILF | keywords, city, category, minimum salary, frequency, status, created on, owner (which job seeker) | 8 | 1 | Low | 7 |
| Job announcement | ILF | title, company, city, category, salary, description, contract type, posted on, status, posted by (which recruiter) | 10 | 1 | Low | 7 |
| Recruiter account | EIF | name, company, e-mail, password | 4 | 1 | Low | 5 |

All four are small: fewer than 20 fields and at most five subgroups put each in the Low cell.

## 2. The transactions

A transaction counts the fields that cross the boundary, plus one for its button and one for its
message; an inquiry or output counts each field once even if it appears on both sides
{% cite longstreet2002fpa %}. Fields the system sets itself, such as *registered on* or *posted on*,
are stored but do not cross the boundary, so they are not DETs of the transaction.

| Transaction | Type | DET | FTR | Rating | FP |
|---|---|--:|--:|---|--:|
| Register: 6 entered fields, button, message | EI | 8 | 1 | Low | 3 |
| Upload resume · Delete resume: the document, button, message | EI | 3 | 1 | Low | 3 + 3 |
| Create alert: 5 fields; references alert and job seeker | EI | 7 | 2 | Average | 4 |
| Suspend alert · Delete alert · Delete job: the item picked, button, message; checks the owner | EI | 3 | 2 | Low | 3 × 3 |
| Post job · Edit job: 7 fields; references announcement and recruiter account | EI | 9 | 2 | Average | 4 + 4 |
| Log in, job seeker · Log in, recruiter: e-mail, password, button, message | EQ | 4 | 1 | Low | 3 + 3 |
| Search jobs: 3 criteria in, 5 fields out, city once, button, message | EQ | 9 | 1 | Low | 3 |
| Notify job seekers of matching posts: 7 fields in the e-mail, including the count of matches | EO | 7 | 3 | Average | 5 |

Notify is an output because its e-mail carries a count the system calculates; selecting or matching stored records alone is not derived data, which is why Search jobs and the log-ins are inquiries. Log-outs move no data
the user would recognise, so they are not counted. Only the transactions that reference two or more
files and more than four fields leave the Low cell: the deletes touch two files but carry only three
fields.

## 3. The total, and what the rating did

| | Every item Average | Rated |
|---|--:|--:|
| Files: 3 ILF + 1 EIF | 37 | 26 |
| Inputs: 9 EI | 36 | 30 |
| Inquiries: 3 EQ | 12 | 9 |
| Output: 1 EO | 5 | 5 |
| **Unadjusted function points (UFP)** | **90** | **70** |

Rating every item Average is the honest default when the stories carry no fields
{% cite longstreet2002fpa %}. Once the fields are known, Workopolis rates mostly Low and the count
falls by 22%. The open classification choices move it much less: career alerts treated as part of the job seeker (a subgroup) give 62, the resume as a file of its own 77, *Notify* without the count, an inquiry, gives 69,
recruiter accounts as an internal file 72, log-ins left out 64. After the boundary, the rating is the
biggest lever, so a count should record every rating and the fields behind it.

## 4. From count to hours

**With productivity.** At a company's past productivity of 8 to 12 FP per person-month, recorded in
UFP, 70 UFP is 5.8 to 8.8 person-months, or **930 to 1,400 hours** at its 160-hour person-month. Quote
the range, and say what the productivity covers.

**With COCOMO II**, every scale factor and multiplier at nominal {% cite usc2000cocomo %}:

| Step | Formula | Workopolis |
|---|---|---|
| Size | UFP × 53 lines per FP (Java) | 3.71 KSLOC |
| Exponent | E = 0.91 + 0.01 × 18.97 (the five scale factors at nominal) | 1.10 |
| Effort | PM = 2.94 × KSLOC<sup>E</sup> | 12.4 person-months; at COCOMO's 152-hour person-month, about 1,890 hours |
| Schedule | TDEV = 3.67 × PM<sup>0.28 + 0.2 (E − 0.91)</sup> | 8.2 months |
| Team | PM ÷ TDEV | about 1.5 people |

COCOMO takes unadjusted function points. Uncalibrated, it applies other organisations' productivity,
which is why it sits above the estimate from the team's own rate; recalibrate its constant on your
own finished projects before quoting it.

## 5. What the count does not see

A function-point count sizes the software the user touches. Data migration, training material,
deployment and support after launch are not in it, so estimate them bottom-up over the work
breakdown structure and add them. A bottom-up estimate that comes out higher than the count is
information about that missing work, not an error to average away.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David
Root** {% cite root2014lectures %} on software project management. Workopolis and the
function-point material are Miranda's {% cite miranda_managing_2014 %}.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
