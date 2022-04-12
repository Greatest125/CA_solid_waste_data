import os, pandas as pd, glob
#Merge all of the spreadsheets (one for each facility) into one master spreadsheet 
os.chdir("/home/leeld/Downloads/files")
extensions = ("*xlsx")
filenames = []  # made 'filename' plural to indicate it's a list

# building list of filenames moved to separate loop
for files in extensions: 
    filenames.extend(glob.glob(files)) 
# getting excel files to be merged
print('File names:', filenames)

# empty data frame for the new output excel file with the merged excel files
outputxlsx = pd.DataFrame()

# for loop to iterate all excel files
for file in filenames:
   # using concat for excel files
   # after reading them with read_excel()
   df = pd.concat(pd.read_excel( file, sheet_name=None), ignore_index=True, sort=False)
   #Clean up unwanted text from spreadsheet
   df = df[~df['Unnamed: 0'].isin(['Jurisdiction or Origin Waste Disposal By Facility'])]
   # appending data of excel files
   outputxlsx = outputxlsx.append( df, ignore_index=True)
print('All spreadsheets merged into one file ("RDS_FacilityReports(origin data).xlsx"')
outputxlsx.to_excel("/home/leeld/Downloads/files/RDS_FacilityReports(origin data).xlsx", index=False)
#Delete data files for each county
for filename in glob.glob("/home/leeld/Downloads/files/FacilitySummary*"):
    os.remove(filename) 
print('Deleting data spreadsheets')
