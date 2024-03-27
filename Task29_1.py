import collections
a=[1,1,1,1,1,1,1,7]
b=collections.Counter(a)
c=[i[0] for i in b.items() if i[1]==1]
print(c[0])


