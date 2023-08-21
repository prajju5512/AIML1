import pandas as pd
import numpy as np
s1 = pd.Series([10,11,1,3])
s2 = pd.Series([1,12,3,5])
u = pd.Series(np.union1d(s1,s2))
print("union\n",u)
i = pd.Series(np.intersect1d(s1,s2))
print("intersect \n",i)
notcommon = u[~u.isin (i)]
print("not common in :\n",notcommon)
