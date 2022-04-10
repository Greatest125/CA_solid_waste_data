# California Solid Waste Data
The python scripts in this repository will allow you to download solid waste data from CalRecycle's [DRS](https://calrecycle.ca.gov/lgcentral/drs/) and [RDRS](https://calrecycle.ca.gov/swfacilities/rdreporting/) databases. While these databases contain a lot of information, it is spread out among many different web pages and requires many downloads (in some cases you need to download a separate excel file for each county!). These scripts simplify that proccess and allow you to parse the data in an efficent manner. 

# The Scripts
## DRS (Disposal Reporting System) - 1995 to 2019

### [Export by County](https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Origin/ExportByCounty) 
* Exported waste by county
* NOT broken up by waste type
* Script to download [here](https://github.com/Greatest125/CA_solid_waste_data/blob/main/RDS_export.py)

### [Facility Reports](https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Origin/FacilitySummary)
* Origin data for each facilities 
* NOT broken up by waste type (but you can extrapolate this w/ waste characterization [studies](https://www2.calrecycle.ca.gov/wastecharacterization/study))
* Script to download [here](https://github.com/Greatest125/CA_solid_waste_data/blob/main/facility_origin.py)

### [Facility IDs ](https://www2.calrecycle.ca.gov/SolidWaste/Site/Search)

# Background information
These scripts were created after consultation with CalRecycle employees. For more information, on all the available datasets for solid waste data and disclaimers about this data, see [this](https://drive.google.com/drive/u/0/folders/14Bdnm6pYQJ6eFdCyBcy0Ez42CSEU0zkg) Google folder.

# About
These scripts are created for a project (funded by the [Energy Justice Network](energyjustice.net)) that seeks to combine available solid waste data (often obtained from state agencies through open records requests) into a single database. More information about the national waste flow database will be updated soon. Be sure to check out a Python script to download GA solid waste [here](https://github.com/Greatest125/GEOS-link-scrape).

For more information, contact leel [at] duck.com
