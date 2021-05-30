# Work Ideas
Please create a new H2 heading for each major idea.

## Event scripts
Create a suite of scripts to handle event administration. The scripts should be able to be run from AGOL notebook
to prevent the need to have Pro open to get started.
**Note:** This may not be necessary if we move to a single event GDB implimentation. Perhaps this may be a good model
for feature templates however.
- Event startup (create folders on AGOL, connect data sources, create collections views)
  - Create AGOL groups and assign appropriate members
  - Copy blank eventGDB and add data sources to current map
  - Sync map
  - Run Join an incident tool
- Joining an incident
-   Create feature templates
- Running
  - Update domains in case we need to collect extra data (Domains from Table) **Note:** When fully implimented,
    contingent values are probably the way to go.
  - OSM Networks???
  - Create Survey 123 from feature layer (Event GDB) — Will require updating the URL
- Closing Incident
  - Sync data to AGOL
  
## Custom webapps
- Create custom webapps by functional position

## Print kiosk
- Allow users to output and print maps
  - Pick a size
  - Pick your layers
  - Pick styling
  - Go -> to the printer
  
## Event GDB
- See [here](archive/2018_gdb_changes_nwcg_to_all_hazards.md) for previous attempts at this
- Allow the creation of custom attributes/contingent values
- Create standardized data schemas
- Model off NWCG gdb

### GDB symbology
- See [Canada All Hazards Symbology](http://goccogpubca.canadaeast.cloudapp.azure.com/share/GOC-COG/CAHS-SCTR/Documentation/PS-SP-%231272768-v6A-CAHS_Explained.pdf) for ideas
- May get ESRI involved here
- Will require linking all symbology to attributes in event GDB...may get busy fast

|                                               | Planning                                                  | Execution                                    | Review |
|-----------------------------------------------|-----------------------------------------------------------|----------------------------------------------|--------|
| Infastructure (Things we have)                | Inventory--Serviceability--Response Inventory(Cache--Units)   |                                              |        |
| Hazards (Things that could (or did) go wrong) | Pre-planning--Flood zones--Evacuation routes--Event Planning | Zones--Infrastructure impact                  |        |
| Operations (What are we doing about it)       |                                                           | Unit assignments--Unit locations--Unit history |        |

## Add useful data GDB packaged with template
- Data ideas:
  - Countries
    - world fact database
  - States
    - Simple census data
  - Counties
    - Simple census data
  - Zip codes
  - Fire layer
  - World Vector Labels
  - Water Bodies
  - Terrain
  - UTM Grids (or maybe a tool)
  - Quadranagle index
  - Federal Lands
  - State/county lands?

## Brainstorms
- Move from gdb to geo package to allow use of third party applications/libraries
- IAP creator
- iSuites tools