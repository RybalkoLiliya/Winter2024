i = int(input())
total = 0
length = 0
while i != 0:
    total += i
    length += 1
    i = int(input())
print(total / len)

#Option 2
su, hm = 0, 0
while True:
    s = int(input())
    if s == 0:
        break
    su += s
    hm += 1
print(su / hm)










