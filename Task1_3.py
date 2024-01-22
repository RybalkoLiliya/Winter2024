# Task 1-3
print('Введите число')
x = float(input())
print('Введите еще одно число, кроме нуля')
y = float(input())
n1 = x+y
n2 = x*y
n3 = x/y
n4 = x//y
if n1 > max(n2, n3, n4):
    print(max(n2, n3, n4))
if n2 > max(n1, n3, n4):
    print(max(n1, n3, n4))
if n3 > max(n1, n2, n4):
    print(max(n1, n2, n4))
if n4 > max(n1, n2, n3):
    print(max(n1, n2, n3))


# Task 1-3_version 2
x = float(input())
y = float(input())
n1, n2, n3, n4, n5 = x+y,x-y, x*y, x/y, x//y

if n1 >= n2:
    m1 = n1
    m2 = n2
else:
    m1 = n2
    m2 = n1
if n3 >= m1:
    m1 = n3
    m2 = m1
elif n3 >= m2:
    m2 = n3
if n4 >= m1:
    m1 = m4
    m2 = m1
if n3 >= m: m = n3
if n4 >= m: m = n4
if n5 >= m: m = n5
print(m)











