print('Введите числа через пробел')
s = [float(i) for i in input().split()]
m = s[0]
for i in range(len(s)):
    if s[i] < m: m = s[i]
print(m)