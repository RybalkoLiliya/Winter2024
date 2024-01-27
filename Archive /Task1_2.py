# Task 1-2_version 1
x = float(input())
y = float(input())
result = max(x+y,x-y, x*y, x/y, x//y)
print(f'Максимальное число: {result}')

# Task 1-2_version 2
x = float(input())
y = float(input())
n1, n2, n3, n4, n5 = x+y,x-y, x*y, x/y, x//y
m = n1
if n2 >= m: m = n2
if n3 >= m: m = n3
if n4 >= m: m = n4
if n5 >= m: m = n5
print(m)
