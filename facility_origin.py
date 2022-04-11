#Downloads RDS (data <=2019) Facility data (with origin data) which does not track waste type from this website: https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Origin/FacilitySummary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import glob
import os

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/leeld/Downloads/files"}
#change the directory to the whatever you want
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "/usr/bin/chromedriver"
#you need to change the path of the chromedriver depending on your setup (I'm on Lubuntu 20.04)
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
wait = WebDriverWait(driver, 20)

url = "https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Origin/FacilitySummary"

driver.get(url)
dropdown = driver.find_element(By.ID, "ReportType")
dropdown.find_element(By.XPATH, "//option[. = 'Jurisdiction of Origin Waste Disposal']").click()
select_el = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="LandfillName"]')))
facilities = select_el.find_elements(By.TAG_NAME, 'option')
total_facilities = len(facilities)

# len - 1 because the 1st option is blank
print(f"Total facilities: {total_facilities - 1}")
btn = driver.find_element(By.XPATH, '//button[@id="SearchButton"]')

for i in range(1, 70):
    print(f"Clicking Facility - {facilities[i].text}")
    facilities[i].click()
    btn.click()
    time.sleep(2)
driver.close()

driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
wait = WebDriverWait(driver, 20)
driver.get(url)
dropdown = driver.find_element(By.ID, "ReportType")
dropdown.find_element(By.XPATH, "//option[. = 'Jurisdiction of Origin Waste Disposal']").click()
select_el = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="LandfillName"]')))
facilities = select_el.find_elements(By.TAG_NAME, 'option')
total_facilities = len(facilities)

# len - 1 because the 1st option is blank
print(f"Total facilities: {total_facilities - 1}")
btn = driver.find_element(By.XPATH, '//button[@id="SearchButton"]')

for i in range(70, len(facilities)):
    print(f"Clicking Facility - {facilities[i].text}")
    facilities[i].click()
    btn.click()
    time.sleep(2)
driver.close()

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
