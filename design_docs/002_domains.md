## [date, short title of solved problem, and solution]
***
  * Status: proposed
  * Deciders: Pound, Mahon
  * Date: 2022-02-12

***
## Context and Problem Statement

How do we capture the almost infinite feature types that all-hazards IMTs (AHIMT) may be asked to capture? AHIMTs may be asked to capture features that vary greatly in both mission and scale. For the sake of data cleanliness, databases should be capable of limiting the inputs for fields such as 'feature type'.

## Decision Drivers <!-- optional -->

* Should include numerous pre-determined domains and/or ability to create domains as required.

## Considered Options

1. Pre determine and build domains.
2. Manual creation of domains.
3. Programmatically create domains from external template.
4. Manual entry of feature type.

## Decision Outcome

Chosen option: Programmatically create domains from external template.

### Positive Consequences <!-- optional -->

* Allows for use of domains for data cleanliness.
* Enables flexibility to edit domains to meet mission requirements.

### Negative Consequences <!-- optional -->

* Limits feature types that can be collected prior to domain editing.
* May require personnel with technical ability to edit domains prior to collecting new feature types (somewhat negated by utilizing script against template).


# Low-level 

**Evaluation criteria**:

  * Summary: explain briefly what we seek to discover and why.

  * Specifics

**Candidates to consider**:

  * Summary: explain briefly how we discovered candidates, and draw attention to any outliers.

  * List all candidates and related options; what are we evaluating as potential solutions?

  * Specifics

**Recommendation**:

  * Create template pre-populated with common feature types.
  * Implement tool to parse external template.