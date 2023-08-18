a = [1,1,1,1]
b = [1,2,3,4]
c = [1,1,1,1]
l1 = list(map(lambda a,b,c:a+b+c,a,b,c))
print (l1)


lst = ["mango","kivi","apple","orange"]
l1 = list(filter(lambda a :'g' in a,lst))
print(l1)
l1 = list(filter(lambda a :'g' not in a,lst))
print(l1)
