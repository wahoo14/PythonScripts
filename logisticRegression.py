import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import statsmodels.api as sm

def voteOutcome(gop, dem):
	if gop > dem:
		return 1
	else:
		return 0

def main():
	countyData = pd.read_csv(r"C:\Users\davidayu\Misc\Python Scripts\CountyData.csv",encoding='cp1252')
	electionData = pd.read_csv(r"C:\Users\davidayu\Misc\Python Scripts\2016ElectionData.csv",encoding='cp1252')
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
	#recursive feature elimination/selection
	logreg = LogisticRegression()
	rfe = RFE(logreg, len(x))
	rfe = rfe.fit(x,y)
	print(rfe.support_)
	print(rfe.ranking_)
	print("---------------------")
	regressor=sm.Logit(y,x).fit()
	print(regressor.summary())
	print("---------------------")
	#split dataset into test and train
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
	logreg.fit(x_train, y_train)
	y_pred = logreg.predict(x_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(x_test, y_test)))
	print("---------------------")	
	confusionMatrix = confusion_matrix(y_test, y_pred)
	print(confusionMatrix)
	
	
if __name__ == "__main__":
	main()