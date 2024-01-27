s = [3, "l", True, [5]]
for i in s:
    if type(i) == str: print(i*2)
    elif type(i) == int: print(i**2)
    else:print(i)


s = [3, "l", True, [5]]
print(s)
s.append('Hello world')
print(s)
print(len(s))

s = []
for i in range(5):
    s.append(i)
print(s)


lst = []
for i in range(5):
    a = int(input())
    lst.append(a)
else:
    print(lst)


