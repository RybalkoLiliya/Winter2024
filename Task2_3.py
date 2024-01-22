#Version_1
n = int(input())
f = n
if n == 0: print(1)
else:
    for i in range(1, n):
        f = f*i
    print(f)

#Version_2
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)
