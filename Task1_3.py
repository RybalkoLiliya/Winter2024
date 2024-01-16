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











