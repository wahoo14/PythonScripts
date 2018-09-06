import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import statsmodels.api as sm

def main():
	###Clean, merge data
	popData = pd.read_csv(r"C:\Users\davidayu\Misc\Python Scripts\PopulationOverTime.csv", encoding='cp1252')
	saleData = pd.read_csv(r"C:\Users\davidayu\Misc\Python Scripts\HomesForSale_byCounty.csv", encoding='cp1252')
	saleData['CountyName'] = saleData['CountyName'].map(lambda x: x+' County')
	HHIncome = pd.read_csv(r"C:\Users\davidayu\Misc\Python Scripts\CountyData.csv", encoding='cp1252')
	HHIncome = HHIncome[['Geography','Median_Household_Income_2016','Unemployment_rate_2017']]
	
	popReduced = popData[['Geography','Population Estimate (as of July 1) - 2017']]
	saleData['Geography'] = saleData['CountyName']+', '+saleData['StateFullName']
	saleReduced = saleData[['Geography', '2017']]

	mergedDf1 = pd.merge(left = saleReduced, right = popReduced, on ="Geography", how="outer")
	mergedDf2 = pd.merge(left =HHIncome, right = mergedDf1, on = "Geography", how="outer" )
	mergedDf2 = mergedDf2.dropna(axis = 0, how ='any')

	###Create scatterplot visualization
	#plt.scatter(mergedDf1['Population Estimate (as of July 1) - 2017'], mergedDf1['2017'])

	#for index, row in mergedDf1.iterrows():
	#	plt.annotate(row[0],(row[2],row[1]))
#uncomment to show plot
#plt.show()

#Run linear regression, test against actual results
	y=mergedDf2['2017']
	x=mergedDf2[['Population Estimate (as of July 1) - 2017','Median_Household_Income_2016','Unemployment_rate_2017']]
	x=sm.add_constant(x)
	
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

	regressor = sm.OLS(y_train,x_train).fit()
	print(regressor.summary())
	
	print("----------------------")
	
	predictions = regressor.predict(x_test))
#	results = pd.DataFrame({"Actual":Y_testFlat,"Predicted":Y_predFlat})

#	print("----------------------")
#	print("Intercept: "+str(regressor.intercept_))
#	print("Coefficients: "+str(regressor.coef_))
#	print('Mean Absolute Error:', metrics.mean_absolute_error(Y_testFlat, Y_predFlat))  
#	print('Mean Squared Error:', metrics.mean_squared_error(Y_testFlat, Y_predFlat))  
#	print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_testFlat, Y_predFlat))) 
#	print("RSquared:", metrics.r2_score(Y_testFlat, Y_predFlat))
	
if __name__ == "__main__":
	main()
