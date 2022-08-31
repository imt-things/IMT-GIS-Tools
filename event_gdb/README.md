# Vision
The event Geodatabase (Event GDB) aims to provide a framework for working with geospatial data during all-hazard IMT assignments. The fixed schema, in conjunction with flexible domains allow pre-staged products while allowing for data collection of unknown types. Additionally, archiving to a common database and utilizing pre-made tools is possible due to the known schema.

We present the following as a framework for standardizing geospatial data collection during all-hazard IMT assignments.

# Motivation
Tremendous amounts of time are consumed during assignments creating custom schemas that conform to single incidents. This is problematic in a number of ways but generally fall into resources , requirements, and compatibility.
1. Resources:
   1. Creating one-off data schemas takes a tremendous amount of resources. Time is a high-demand, low-density resource particularly at the beginning of an incident when personnel are still being assigned or are otherwise heavily engaged. Yet, the beginning of an incident is the precise time when data schemas must be created, tested, deployed, and integrated
   2. Trained GIS personnel may not be readily available while data collection may be an immediate requirement for safety, incident mitigation, or preservation.
2. Requirements:
   1. Oftentimes, data collection requirements are not known at the beginning of the incident.
   2. Requirements can, and often do, change multiple times during an incident.
3. Compatibility:
   1. Todays GIS implementations, even for relatively small assignments, contain a host of tools that work in conjunction to provide data to decision makers, collaborators, stakeholders, the public, and potentially as evidence.
   2. Changing schemas can break interoperability, sometimes in unpredictable ways. This may result in unusable data collection, analysis, or visualization tools.
   
A fixed schema will allow for pre-staged tools covering the entire spectrum of data collection to visualization while providing the flexibility to collect numerous types of data.

# Status
- Currently no way to update domains/contingent values
- Event GDB requires table-top exercise testing

# Changelog
## 2022-08-31