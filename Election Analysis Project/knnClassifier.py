import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def voteOutcome(gop, dem):
	if gop > dem:
		return 1
	else:
		return 0

def main():
	countyData = pd.read_csv(r"C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\CountyData.csv",encoding='cp1252')
	electionData = pd.read_csv(r"C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\2016ElectionData.csv",encoding='cp1252')
	#Drop alaska (incomplete county election data)
	countyData = countyData[countyData['State']!='AK']
	electionData = electionData[electionData['state_abbr']!='AK']

	#merge dataframes
	merged = pd.merge(left=countyData, right=electionData, left_on='Geography', right_on='county_name', how='outer')
	#create Boolean column, 1 for majority GOP vote, 0 for majority Democrat vote
	merged['Voted Republican?'] = merged.apply(lambda x: voteOutcome(x['per_gop'],x['per_dem']), axis=1)
	merged.to_csv("test10.csv")
	#drop Nans
	merged = merged.dropna(axis = 0, how ='any')
	#set x and y datasets
	y=merged['Voted Republican?']
	x=merged[['Civilian_labor_force_2017','Unemployment_rate_2017','Median_Household_Income_2016']]
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
	#scale features
	scaler = StandardScaler()
	scaler.fit(x_train)
	x_train = scaler.transform(x_train)
	x_test = scaler.transform(x_test)
	
	#START KNN
	classifier = KNeighborsClassifier(n_neighbors = 2)
	classifier.fit(x_train, y_train)
	y_pred = classifier.predict(x_test)
	
	print(confusion_matrix(y_test, y_pred))  
	print(classification_report(y_test, y_pred))  
	
	
	
if __name__ == "__main__":
	main()
