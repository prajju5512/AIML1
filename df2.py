import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-01/Desktop/p/Iris.csv")
print(data)
df = data.head(5)
s1 = pd.Series(data['SepalLengthCm'])
print(s1)
print(s1.value_counts())
d = pd.DataFrame(df['SepalLengthCm'].values,index=df['PetalWidthCm'])
print(d) 
