from anom_detect import anom_detect
import pandas as pd


#df = pd.read_csv(r'C:\Users\dyu\Documents\Python_Scripts\anomaly_detection\sunspots.txt',sep='\t',header=None)
#df.index.name = 'time'
#df.drop(df.columns[0],axis=1,inplace=True)
#df.columns = ['sunspots']

df = pd.read_csv(r'C:\Users\dyu\Documents\Python_Scripts\anomaly_detection\exampleQA.csv',encoding='cp1252', header = None,)
df.columns = ['idk']

an = anom_detect()

an.evaluate(df)

print(an.anoma_points)

an.plot(from_console=True)

