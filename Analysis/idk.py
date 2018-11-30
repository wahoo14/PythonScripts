import pandas as pd

data = pd.read_csv(r'C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Election Analysis Project\DataFiles\ACS_16_5YR_DP02_with_ann.csv', encoding='cp1252')

#drop columns
demoColumns = data.columns.values

#remove margin of error columns
errorColumns = [a for a in demoColumns if "Margin of Error" in a]
estimateColumns = [c for c in demoColumns if "Estimate;" in c]
demoColumns1 = [b for b in demoColumns if b not in errorColumns]
demoColumns2 = [d for d in demoColumns1 if d not in estimateColumns]
data = data[demoColumns2]

print(data.head())