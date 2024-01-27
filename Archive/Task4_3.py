s1 = sorted(input().lower())
s2 = sorted(input().lower())

dct1 = dict(zip(range(len(s1)), s1))
dct2 = dict(zip(range(len(s2)), s2))

print(dct1 == dct2)
