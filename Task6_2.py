a = input().split(',')
b = input().split(',')
res = []
for i in range(len(a)):
    if a[i] in b:
        res.append(a[i])
print(len(res))
