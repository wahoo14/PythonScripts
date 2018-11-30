#Analyses the 5 most important demographic factors in predicting a county's election outcome in the 2016 election
#using a multiple regression analysis

import pandas as pd
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

#parse election data
electionData = pd.read_csv(r"C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\2016ElectionData.csv",encoding='cp1252')
electionData = electionData[["combined_fips","per_dem"]]

#parse demographic data
data = pd.read_csv(r"C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\ACS_16_5YR_DP02_with_ann.csv",encoding='cp1252', low_memory = False)

#drop columns
demoColumns = data.columns.values

#remove margin of error columns
errorColumns = [a for a in demoColumns if "Margin of Error" in a]
estimateColumns = [c for c in demoColumns if "Estimate;" in c]
demoColumns1 = [b for b in demoColumns if b not in errorColumns]
demoColumns2 = [d for d in demoColumns1 if d not in estimateColumns]
data = data[demoColumns2]

#merge Datasets
electionData["combined_fips"]=electionData["combined_fips"].astype(str)
data["Id2"] = data["Id2"].astype(str)
combinedDf = pd.merge(electionData,data, how='outer', left_on="combined_fips", right_on="Id2")
y = combinedDf["per_dem"]
x = combinedDf.loc[:, combinedDf.columns != "per_dem"]
x = x.drop(["Id","Geography","combined_fips"],axis = 1)
x = x.applymap(str)
x = x.replace("(X)",np.nan)
x = x.replace("*****",np.nan)
x = x.replace("-",np.nan)
x = x.replace("**",np.nan)
x = x.replace("nan",np.nan)
x = x.dropna(axis=1,how='all')
x.fillna(value=0,inplace = True)
x = x.applymap(float)
y = y.apply(lambda z: round(z,2))
y.fillna(value = .5, inplace = True)

#recursive feature elimination
lr = LinearRegression()
rfe= RFE(lr, n_features_to_select=5)
fit = rfe.fit(x,y)

print(x.columns.values[fit.support_])

x = x[x.columns.values[fit.support_]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

regressor = sm.OLS(y_train,x_train).fit()
print(regressor.summary())



