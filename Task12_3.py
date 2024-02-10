x = '1-2,4-4,3-6,11-15,15'
res = []
for s in x.split(','):
    if '-' in s:
        start, end = map(int, s.split('-'))
        res.append(start)
        for i in range(start + 1, end + 1):
            res.append(i)
    else:
        res.append(int(s))
print(res)

# res = [[i for i in range(int(n[j][0]), int(n[j][2])+1)] for j in range(len(n))]
# print(res)
