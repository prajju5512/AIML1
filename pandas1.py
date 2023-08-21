import pandas as pd
import numpy as np
info = pd.array([1,2,3,4,5,8,10])
print (info)
p = pd.Series([2,1,3,4,5,6])
print(p)
i = pd.Index([1,3,1,np.nan,1])
print(i.value_counts())
