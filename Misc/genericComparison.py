import pandas as pd

###Generic python script used to join two sheets on user specified-columns and by a user-specified join type.  
###Includes some error handling and outputs the joined spreadsheet.

def getInputs():
	while 1 == 1:
		joinType = raw_input("Join type (left, inner, or outer)?: ").lower()
		if joinType == "left" or joinType == "inner" or joinType == "outer":
			break
		else:
			print("Invalid input.")
	while 1 == 1:
		try:
			leftFilepath = raw_input("Enter filepath for the LEFT sheet: ")
			leftSheet = pd.read_excel(leftFilepath)
		except:
			print("Invalid filepath.")
		else:
			break
	while 1 == 1:
		try:
			rightFilepath = raw_input("Enter filepath for the RIGHT sheet: ")
			rightSheet = pd.read_excel(rightFilepath)
		except:
			print("Invalid filepath.")
		else:
			break
	while 1 == 1:
		leftJoinCol = raw_input("Enter join column name for the LEFT sheet: ")
		if leftJoinCol in list(leftSheet.columns.values):
			break
		else:
			print("Invalid column name.")
	while 1 == 1:
		rightJoinCol = raw_input("Enter join column name for the RIGHT sheet: ")
		if rightJoinCol in list(rightSheet.columns.values):
			break
		else:
			print("Invalid column name.")	
	return leftSheet, rightSheet, leftJoinCol, rightJoinCol, joinType
		
def dataCleanUp(leftSheet, rightSheet, leftJoinCol, rightJoinCol):
	print("Cleaning data...")
	leftSheet[leftJoinCol] = leftSheet[leftJoinCol].str.upper()
	leftSheet[leftJoinCol] = leftSheet[leftJoinCol].str.replace(" ","_")
	rightSheet[rightJoinCol] = rightSheet[rightJoinCol].str.upper()
	rightSheet[rightJoinCol] = rightSheet[rightJoinCol].str.replace(" ","_")
	return leftSheet,rightSheet
	
def merge(cleanedLeft, cleanedRight, leftJoinColumn, rightJoinColumn, joinType):
	print("Merging datasets...")
	mergedDataset = cleanedLeft.merge(cleanedRight, how=joinType, left_on=leftJoinColumn, right_on=rightJoinColumn)
	mergedSheetName = raw_input("Merged dataset name (excluding .csv suffix)? ")
	print("Outputing datafile to CSV...")
	mergedSheetName=mergedSheetName+".csv"
	print(mergedSheetName)
	mergedDataset.to_csv(mergedSheetName, encoding='utf-8')
	
def program():
	print("Auto-Excel Data Joiner")
	leftSheet, rightSheet, leftJoinCol, rightJoinCol, joinType = getInputs()[:]
	cleanedLeft, cleanedRight = dataCleanUp(leftSheet, rightSheet, leftJoinCol, rightJoinCol)[:]
	merge(cleanedLeft, cleanedRight, leftJoinCol, rightJoinCol, joinType)

if __name__ == "__main__":
	program()