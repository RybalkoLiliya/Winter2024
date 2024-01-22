i = int(input())
s = []
total = 0
while i != 0:
    total += i
    s.append(i)
    i = int(input())
print(total / len(s))