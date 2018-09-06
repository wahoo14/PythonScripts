import logging
import traceback
from datetime import datetime
from joblib import Parallel, delayed
import regressionTest1
import regressionTest2

#set up logging, count variables
today= datetime.today().strftime('%m-%d-%Y')
now= datetime.now()
countSuccessful = 0
testNumber = 1
testList = [regressionTest1.regression1,regressionTest2.regression2]
totalTests = len(testList)

def executionFunction(function):
	global countSuccessful
	global testNumber
	try:
		function()
		countSuccessful = countSuccessful+1
		logging.info("Test "+ str(testNumber)+" Successful")
	except Exception as e:
		logging.error("Test "+ str(testNumber)+" Failed")
		logging.error(e)
	testNumber = testNumber+1

def main():
	logging.basicConfig(filename=str(today)+'_fullRegression.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	logging.info("Execution start time: "+str(now))
	for test in testList:
		executionFunction(test)
	logging.info(str(countSuccessful)+" of "+str(totalTests)+" regression tests successful.")
	logging.info("Execution end time: "+str(datetime.now()))
	logging.info("Run time: "+str(datetime.now()-now))
	print(str(countSuccessful)+" of "+str(totalTests)+" regression tests successful.")

if __name__ =="__main__":
	main()
