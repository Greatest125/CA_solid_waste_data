import pandas as pd
import glob
import os
  
# use glob to get all the csv files
# in the folder
path = '/home/leeld/Downloads/files'
csv_files = glob.glob(os.path.join(path, "*.xlsx"))
  
  
# loop over the list of csv files
for f in csv_files:
# Read all three files into pandas dataframes
    test = pd.read_excel(f)

# Create a list of the files in order you want them appended
all_df_list = [test]

# Merge all the dataframes in all_df_list
# Pandas will automatically append based on similar column names
appended_df = pd.concat(all_df_list)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
appended_df.to_excel("DRS_export(all-counties)", index=False)