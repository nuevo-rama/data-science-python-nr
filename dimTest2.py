import numpy as np

#Iterating

d1 = np.array([1,2,3])
for a in d1:
    print(a)


d2 = np.array([[1,2,3],[-1,-2,-3]])
for a in d2:
    for b in a:
        print(b)


d3 = np.array([[[1,2,3],[-1,-2,-3]],[[6,7,8],[-6,-7,-8]]])
for a in d3:
    for b in a:
        for c in b:
            print(c)
