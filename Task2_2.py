#Version_1
print('Введите числа через пробел')
s = [float(i) for i in input().split()]
m = s[0]
for i in range(len(s)):
    if s[i] < m: m = s[i]
print(m)

#Version_2
lst = [1,2,4,5]
for i in lst:
    m += abs(i)
m += 1
print(m)

#Version_3
lst = []
m = float('inf')#Бесконечность
print(m)

