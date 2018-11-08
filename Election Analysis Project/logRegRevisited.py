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
		
def percentChecker(value):
	if value>=100:
		return np.nan
	else:
		return value

def main():
	countyData = pd.read_csv(r"C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\ACS_16_5YR_DP02_with_ann.csv",encoding='cp1252')
	electionData = pd.read_csv(r"C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\2016ElectionData.csv",encoding='cp1252')

	#pare county data to percentage columns
	allColumns = countyData.columns.values
	errorColumns = [a for a in allColumns if "Margin of Error" in a]
	estimateColumns = [c for c in allColumns if "Estimate;" in c]
	noErrorColumns = [b for b in allColumns if b not in errorColumns]
	filteredColumns = [d for d in noErrorColumns if d not in estimateColumns]
	countyData = countyData[filteredColumns]
	
	#pare election data to outcome/join keys
	electionData['Voted Republican?'] = electionData.apply(lambda x: voteOutcome(x['per_gop'],x['per_dem']), axis=1)
	electionData.drop(labels=['Unnamed: 0','votes_dem','votes_gop','total_votes','per_dem','per_gop','diff','per_point_diff','state_abbr','combined_fips'], inplace=True, axis=1)
	
	#merge dataframes
	merged = pd.merge(left=countyData, right= electionData, left_on='Geography', right_on='county_name', how='inner')
	#clean dataset
	merged.drop(labels=['Id','Id2','county_name'],inplace=True, axis=1)
	merged.replace(to_replace=['(X)','-'], value = np.nan, inplace=True)
	merged = merged.dropna(axis = 1, how ='any')
	
	#set x and y
	x = merged.iloc[:,1:-1]
	x = x.applymap(percentChecker)
	x = x.dropna(axis = 1, how='any')
	y = merged.iloc[:,-1:]
	
	#recursive feature elimniation
	logreg = LogisticRegression(max_iter=1000)
	rfe = RFE(logreg, 3)
	rfe = rfe.fit(x,np.ravel(y, order='C'))
	x=x.loc[:,rfe.support_]
	
	#logistic regression, train set
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
	logreg.fit(x_train, y_train)
	regressor=sm.Logit(y_train,x_train).fit()
	print(regressor.summary())
	
	#logistic regression, test set
	y_pred = logreg.predict(x_test)
	print("---------------------")	
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(x_test, y_test)))
	print("---------------------")
	confusionMatrix = confusion_matrix(y_test, y_pred)
	print(confusionMatrix)
	
if __name__ == "__main__":	
	main()
