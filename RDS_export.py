#Downloads RDS (data <=2019) EXPORT (import not tracked) data which does not track waste type from this website: https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Origin/ExportByCounty
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/leeld/Downloads/files"}
#change the directory to the whatever you want
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "/usr/bin/chromedriver"
#you need to change the path of the chromedriver depending on your setup (I'm on Lubuntu 20.04)
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

wait = WebDriverWait(driver, 20)

url = "https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Origin/ExportByCounty"


driver.get(url)

select_el = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="CountyID"]')))
counties = select_el.find_elements(By.TAG_NAME, 'option')
total_counties = len(counties)

# len - 1 because the 1st option is blank
print(f"Total counties: {total_counties - 1}")
btn = driver.find_element(By.XPATH, '//button[@id="SearchButton"]')

for i in range(1, len(counties)):
    print(f"Clicking County - {counties[i].text}")
    counties[i].click()
    btn.click()
    time.sleep(2)
