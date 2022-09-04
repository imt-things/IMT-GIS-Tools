# Vision
The event Geodatabase (Event GDB) aims to provide a framework for working with geospatial data during all-hazard IMT assignments. The fixed schema, in conjunction with flexible domains, allows for pre-staged products, data collection of unknown types, and archiving to a common database.

We present the following as a framework for standardizing geospatial data collection during all-hazard IMT assignments.

# Motivation
During assignments, tremendous amounts of time are consumed creating custom schemas that conform to single incidents. This is problematic for a number of reasons (e.g., resources, requirements, and compatibility).
1. Resources:
   1. Creating one-off data schemas is highly time-consuming. Time is a high-demand, low-density resource particularly at the beginning of an incident when personnel are still being assigned or are otherwise heavily engaged. Yet, the beginning of an incident is the precise time when data schemas must be created, tested, deployed, and integrated.
   2. Trained GIS personnel may not be readily available for schema creation even though data collection may be an immediate requirement for safety, incident mitigation, or preservation.
2. Requirements:
   1. Oftentimes, data collection requirements are not known at the beginning of the incident.
   2. Requirements can, and often do, change multiple times during an incident.
3. Compatibility:
   1. Today's GIS implementations, even for relatively small assignments, contain a host of tools that work in conjunction to provide data to decision makers, collaborators, stakeholders, the public, and potentially as evidence.
   2. Changing schemas can break interoperability, sometimes in unpredictable ways. This may result in unusable data collection, analysis, or visualization tools.
   
A fixed schema will allow for pre-staged tools covering the entire spectrum from data collection to visualization while providing the flexibility to collect numerous types of data.

# Status
- Currently, there is no way to update domains/contingent values.
- Event GDB requires table-top exercise testing.

# Changelog
## 2022-09-04
