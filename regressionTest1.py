from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commonValues import download_folder
from commonValues import chrome_driver_location
from commonValues import url
import time

##regression test function
def regression1():
	##set options, webdriver, etc
	chrome_options = webdriver.ChromeOptions()
	setDLfolder = {"download.default_directory": download_folder}
	chrome_options.add_experimental_option("prefs",setDLfolder)
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_driver_location,chrome_options=chrome_options)
	wait = WebDriverWait(driver, 10)
	##execute test
	driver.get(url)
	searchField = wait.until(EC.presence_of_element_located((By.CLSS_NAME,'landing-search-input')))
	searchField.clear()
	searchField.send_keys('test')
	driver.close()

if __name__ == "__main__":
	regression1()