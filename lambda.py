a = lambda a : a+5
print(a(10))
b = lambda a,b:a+b
print(b(5,2))
c = lambda a,b:a if  (a>b) else b
print(c(5,10))
d = lambda a :a*a
print(d(5))

lst=[1,2,3,4,5,6]
l1 = list (map(lambda a: a+5,lst))
        print(l1)
lst1=[1,2,3,4,5,6,7,8]
l2 = list(filter(lambda a : a%2 == 0,lst1))
print(l2)
l3 = list(filter(lambda a : a%2 != 0,lst1))
print(l3)

from functools import reduce
lst2 = [7,8,9,4,5,6,1,2,3]
l4 = reduce(lambda a,b:a+b,lst2)
print(l4)
