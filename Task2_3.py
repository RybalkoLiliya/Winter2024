n = int(input())
f = n
if n == 0: print(1)
else:
    for i in range(1, n):
        f = f*i
    print(f)
