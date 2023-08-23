import pandas as pd
data = {'name':['purshi','prajju','niranjan'],
        'age':[16,17,18]}
p = pd.DataFrame(data)
p1 = p['age'][0]=p['age'][0]+10
print(p)

