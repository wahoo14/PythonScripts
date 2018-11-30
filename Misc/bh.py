from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import ctypes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
now = datetime.datetime.now()
nowTime = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
programStartTime = time.time()

def msgBox(header, body, style):
	return ctypes.windll.user32.MessageBoxW(0, body, header, style)
	
def popupBody(listOfMessages):
	deals=[]
	for y in listOfMessages:
		textList = y[0]+'\n'+y[1]+'\n'+y[2]+'\n'+'Time Remaining: '+y[3]+'\n'+'\n'
		deals.append(textList)
	dealBody = ''.join(deals)
	return dealBody

def hitURL(chrome_driver_location):
	#hit URL
	driver = webdriver.Chrome(chrome_driver_location,options=chrome_options)
	url = r'https://www.bhphotovideo.com/find/dealZone.jsp'
	driver.get(url)
	
	#extract get deal html
	soup = BeautifulSoup(driver.page_source, 'lxml')
	allDealsDivs = soup.findAll('div', {'class':'dz-glow dz-hover-glow dz-dealItemGridItem'})
	lastRowItems = soup.findAll('div', {'class':'dz-glow dz-hover-glow dz-dealItemGridItem dz-dealItemGridItem--lastInRow'})
	for x in lastRowItems:
		allDealsDivs.append(x)
	
	#get/print specific information per item
	allMessages =[]
	for i in allDealsDivs:
		item = i.find('div', {'class':'dz-dealItem'})['title']
		tag = i.find('strong').get_text()
		dPrice = i.find('span',{'class':'js-dz-price-region dz-deal-color dz-price-1'}).get_text()
		cPrice = i.find('span',{'class':'dz-smallCents'}).get_text()
		price = dPrice+"."+cPrice
		countDown = i.find('span',{'class':'dz-deal-color dz-clock js-dz-clock'}).get_text()
		#compile message body
		if len(allDealsDivs) > 0:
			message = [item,tag,price,str(countDown)]
			allMessages.append(message)
	#create msgBox
	if len(allDealsDivs) > 0:
		header = 'B&H Photo DEALS!!! MBIR'
		body = popupBody(allMessages)
		msgBox(header, body, 1)
	
	driver.close()
	
if __name__ == '__main__':
	driver_location = input('Enter filepath to Chrome Driver: ')
	checkPeriod = input('How often would you like to check for new deals? (Hours): ')
	checkFloat = float(checkPeriod)*360
	while True:
		hitURL(driver_location)
		time.sleep(checkFloat - ((time.time() - programStartTime) % checkFloat))
		
		
		
		
		
		
		