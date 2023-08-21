import pandas as pd
data = pd.DataFrame([[10,11,12,13],[10,11,12,13]],columns=["maths","science","cs","d1"])
print(data)

data = {'name':['purshi','prajju','niranjan'],
        'age':[16,17,18]}
p = pd.DataFrame(data)
print(p)

