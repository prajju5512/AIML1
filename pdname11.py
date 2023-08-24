import pandas as pd
df={'id':[1,2,3,4],
      'name':['prajju','dhanush','purshi','abhi'],
      'gender':['male','male','female','male'],
      'age':[18,19,60,25],
      'dept':['cse','ec','cse','mech'],
      'sal':[250000,300000,2500,50000]}
data = pd.DataFrame(df)
print(data)
print((data[data['gender']=='male']['dept']=='cse').value_counts())
print((data[data['gender']=='female']['dept']=='cse').value_counts())
print(data.groupby('dept')['sal'].sum())


