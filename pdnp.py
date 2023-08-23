import pandas as pd
import numpy as np
dict = {'firstscore':[21,11,np.nan,30],
        'secondscore':[20,np.nan,80,45],
        'thirdscore':[28,36,np.nan,12]}
data = pd.DataFrame(dict)
print(data)
print(data.isnull())
print(data.notnull())
print(data.fillna(1))
print(data.fillna(method='pad'))
print(data.fillna(method='bfill'))
print(data.replace(to_replace=np.nan,value=51))
print(data.dropna())
print(data.dropna(how="all"))
