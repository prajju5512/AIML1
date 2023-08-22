import pandas as pd
data = {'days':[1,2,3,4,5,6,7,8,9,10],
        'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
df=pd.DataFrame(data)

df['steps'] = df['steps']+1000

print(df)

d = pd.DataFrame(data)
print(d)
print(d.loc[d['steps']>7000])
