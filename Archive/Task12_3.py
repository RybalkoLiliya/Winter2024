x = '1-2,4-4,3-6,11-15,15'

def res(x):
    lst = []
    for s in x.split(','):
        if '-' in s:
            start, end = map(int, s.split('-'))
            lst.append(start)
            for i in range(start + 1, end + 1):
                lst.append(i)
        else:
            lst.append(int(s))
    return print(lst)

res(x)
