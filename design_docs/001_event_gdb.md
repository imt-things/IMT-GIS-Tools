## [date, short title of solved problem, and solution]
***
  * Status: proposed
  * Deciders: Pound
  * Date: 2022-02-27

***
## Context and Problem Statement

How do we collect data that allows for pre-built tools to create, read, update, delete (CRUD) with little to no configuration?

The nature of IMT assignments require numerous pre-built tools to enable personnel to begin performing CRUD operations immediately. Additionally, pre-built tools for specific functions/tasks necessitates a pre-defined schema to perform operations on.

This ADR attempts to layout the underlying data schema.

## Decision Drivers <!-- optional -->

* [driver 1, e.g., a force, facing concern, …]
* [driver 2, e.g., a force, facing concern, …]
* … <!-- numbers of drivers can vary -->

## Considered Options

1. Standardized data schema acting as a framework for all assignments.
2. Different data schemas for different assignment types.
3. Creation of schema at time of incident assignment.

## Decision Outcome

Chosen option: Framework schema due to flexibility, ability to pre-develop/deploy tools, and drastic reduction of resources required to deploy.

### Positive Consequences <!-- optional -->

* Enable immediate data collection following notification of assignment. 
* Framework allows creating domains to limit feature types based on assignment requirements (requires completion of [#14](https://github.com/fdny-imt/IMT-GIS-Tools/issues/14) to be completed).
* In conjunction with ready-state deployment, will require no work from technical specialists to begin collection (technical specialist will be required for above point).
* Allows for pre-developed and deployed tools (surveys, webapps, etc.) to be ready for immediate use.
* Common schema allows for simple archiving by appending to a master feature service.

### Negative Consequences <!-- optional -->

* Will require numerous SQL queries on downstream products to ensure viewing of relevant data (consider use of feature service views to perform the queries and serve as layers).
* Will require a technical specialist to update domains. See [#14](https://github.com/fdny-imt/IMT-GIS-Tools/issues/14).
* May require unknown sacrifices on what data can be collected or methods in which it can be collected.
## Pros and Cons of the Options <!-- optional -->

### Framework Schema

Create frame work that contains can accept numerous pre-loaded feature types and provide the ability to update domains from a template. ([#14](https://github.com/fdny-imt/IMT-GIS-Tools/issues/14).

* Pros:
  * Allows for same schema for all potential incident types
  * Allows for hasty deployment for immediate use
  * Allows for starting from standalone database for disconnected incidents
  * Allows for pre-developed/deployed tools

* Cons:
  * May require technical specialist to update domains
  * Potential to limit the data that can be collected and the methods of collection.

### Incident-Type Specific Schemas

Create numerous pre-defined schemas for pre-determined incident types.

* Pros:
  * More specific schemas specific to certain incident types
  * Would not require updating of domains for feature types

* Cons:
  * Limited to pre-determined incident types. Incidents outside those previously built require falling back to option 3 (manual creation)
  * If data to be collected falls outside the pre-determined feature types would require updating of domains/fields
  * Severely limits ability to maintain pre-deployed tools
  * Requires maintaining multiple schemas/deployments

**Note:** Some of the cons may be able to be negated by scripting but largely remain significant hurdles. 

### Custom Schema Per Incident

Manual creation of database at time of assignment.

* Pros:
  * Custom schema provides results most likely to meet needs of incident

* Cons:
  * Requires extensive time and technical knowledge to create
  * Can be very difficult to change mid-incident, potentially resulting in data loss
  * No ability to create/deploy pre-developed tools
  * Has ability to create very difficult to understand/maintain data structures

## Links <!-- optional -->

* [Link type] [Link to ADR] <!-- example: Refined by [ADR-0005](0005-example.md) -->
* … <!-- numbers of links can vary -->


# Low-level 

**Evaluation criteria**:

  * Summary: Determine method to quickly spin-up database to allow near-immediate data collection following notification of assignment.

  * Specifics

**Candidates to consider**:

  * Summary: explain briefly how we discovered candidates, and draw attention to any outliers.

  * List all candidates and related options; what are we evaluating as potential solutions?

  * Specifics

**Research and analysis of each candidate**:

  * Summary: explain briefly the research methods, and draw attention to patterns, clusters, and outliers.
    
  * Does/doesn't meet criteria and why

    * Summary

    * Specifics

  * Cost analysis

    * Summary

    * Examples

      * Licensing, such as contract agreements and legal commitments

      * Training, such as upskilling and change management

      * Operating, such as support and maintenance

      * Metering, such as bandwidth and CPU usage

  * SWOT analysis

    * Summary

    * Strengths

    * Weaknesses

    * Opportunites

    * Threats

  * Internal opinions and feedback

    * Summary

    * Examples

      * By the team, ideally written by the actual person

      * From other stakeholders

      * Quality attributes a.k.a. cross-functional requirements 

  * External opinions and feedback

    * Summary

    * Who is providing the opinion?

    * What are other candidates you considered?

    * What are you creating? 

      * Examples

        * B2B or B2C

        * external-facing or employee-only

        * desktop or mobile

        * pilot or production

        * monolith or microservices

    * How did you evaluate the candidates?

    * Why did you choose the winner?

    * What is happening since then?

      * Examples

        * How is the winner performing?

        * What % of real-world production user traffic is flowing through the winner?

        * What kinds of integrations are involved, such as with continuous delivery pipelines, content management systems, analytics and metrics, etc.?

        * Knowing what you know now, what would you advise people to do differently?

  * Anecdotes

**Recommendation**:

  * Summary

  * Specifics

