import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

###Clean, merge data
popData = pd.read_csv("C:\Users\davidayu\Misc\Python Scripts\Data Science\PopulationOverTime.csv")
saleData = pd.read_csv("C:\Users\davidayu\Misc\Python Scripts\Data Science\HomesForSale_byCounty.csv")
saleData['CountyName'] = saleData['CountyName'].map(lambda x: x+' County')

popReduced = popData[['Geography','Population Estimate (as of July 1) - 2017']]
saleData['Geography'] = saleData['CountyName']+', '+saleData['StateFullName']
saleReduced = saleData[['Geography', '2017']]

mergedDf = pd.merge(left = saleReduced, right = popReduced, on ="Geography", how="outer")
mergedDf = mergedDf.dropna(axis = 0, how ='any')

###Create scatterplot visualization
plt.scatter(mergedDf['Population Estimate (as of July 1) - 2017'], mergedDf['2017'])

for index, row in mergedDf.iterrows():
	plt.annotate(row[0],(row[2],row[1]))
#uncomment to show plot
#plt.show()

#Run linear regression, test against actual results
yHousesSold = mergedDf['2017'].reshape(-1,1)
xPop = mergedDf['Population Estimate (as of July 1) - 2017'].reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(xPop, yHousesSold, test_size = 0.2, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)

#unravel list of lists
Y_testFlat = [val for sublist in Y_test for val in sublist]
Y_predFlat = [val for sublist in Y_pred for val in sublist]
results = pd.DataFrame({"Actual":Y_testFlat,"Predicted":Y_predFlat})

print(results)

print('Mean Absolute Error:', metrics.mean_absolute_error(Y_testFlat, Y_predFlat))  
print('Mean Squared Error:', metrics.mean_squared_error(Y_testFlat, Y_predFlat))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_testFlat, Y_predFlat))) 
