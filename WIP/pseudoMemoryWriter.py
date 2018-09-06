#check to see if memory subfolder exists
#If not, create one, if so, do nothing
#check to see if memory file exists
#if not, create one, if so do nothing

#action to write to memory
#action to delete from memory

import sys
import os
import csv


cwd = os.getcwd()

def createMemory(program):
	markingText= str(program)+"_Memory"
	os.makedirs(markingText)
	open(cwd+"\\"+markingText+"\\"+markingText+".csv",'w')
	
def doesMemoryExist(program):
	markingText= str(program)+"_Memory"
	if os.path.exists(cwd+"\\"+markingText+"\\"+markingText+".csv"):
		return True
	else:
		return False

def writeToMemory():
	try:
		with open('example.csv', newline='') as File:  
			reader = csv.reader(File)
			for row in reader:
				print(row)
	except:
		
#try find memory file
#if successful, write


#def checkMemoryForValue():

#def deleteFromMemory():

#def deleteMemoryFile():

