#.py file called on user created code. Reads code into a list of strings,
#manipulates the created code and writes other code in its place without the 
#user needing to be aware


#user writes code
#Code is saved into a .txt file
#manipulate text file into separating print statements into another file to be printed& convert .txt to .py
#in SEMOSS R call reticulate
#call source_python("newly created .py file")

import os
#import sys
#import re
content=[]
moddedContent=[]
#regex = re.compile(r'print')

def main(helperFunctionFilePath, filepath, content):
	#open retiPrint function, prepend content with it
	with open(helperFunctionFilePath,"r") as e:
		for line in e:
			content.append(line)

	#read file into a list
	with open(filepath,"r") as f:
		for line in f:
			content.append(line)
	#TODO: Remove- was originally for regex matching a new print function
	for string in content:
		#string = re.sub(regex,r"retiPrint",string)
		moddedContent.append(string)
	#create and add in new log file path 
	logFilePath = "r'"+filepath.split(".")[0]+'_log.txt'+"'"
	moddedContent[3] = logFilePath
	#append file to close output
	moddedContent.append('\nsys.stdout.close()')

	#write into existing file
	with open(filepath,"w") as g:
		for string in moddedContent:
			g.write(string)
	g.close()
	#convert to .py file 
	base = os.path.splitext(filepath)[0]
	os.rename(filepath,base+".py")
	newFilePath = "'"+filepath.split(".")[0]+'.py'+"'"
	newFilePath = newFilePath.replace("\\","/")

	return newFilePath, logFilePath


if __name__ == "__main__":
	main(r"C:\Users\davidayu\Misc\Python Scripts\reticulate\helperFunction.txt",r"C:\Users\davidayu\Misc\Python Scripts\reticulate\textToManipulate.txt", content)
