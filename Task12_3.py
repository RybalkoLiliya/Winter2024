x = '1-2,4-4,3-6,11-15,15'

def res(x):
    res = []
    for s in x.split(','):
        if '-' in s:
            start, end = map(int, s.split('-'))
            res.append(start)
            for i in range(start + 1, end + 1):
                res.append(i)
        else:
            res.append(int(s))
    return print(res)

res(x)
