s = input()
for m in range(0,10):
    n = s.count(str(m))
    print(m, n)

#Option_2
s = input()
for k in '0123456789':
    print(k, "-", s.count(k))

#Option_3
hm = [0] * 10
s = input()
for k in s:
    i = int(k)
    hm[i] += 1
for k, v in enumerate(hm):
    print(k, "-", v)


