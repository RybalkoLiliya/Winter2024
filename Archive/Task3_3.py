s = input().split()
id_longest = 0
answer = []
for i in range(len(s)):
    if len(s[i]) > len(s[id_longest]):
        id_longest = i
for j in range(len(s)):
    if len(s[j]) == len(s[id_longest]):
        answer.append(s[j])
print(answer)

#Option_2
s = input().split()
ma = ''
for w in s:
    if len(w) >= len(ma):
        ma = w

#Option_3
s = input().split()
ma = ''
for w in s:
    if len(w) >= len(ma):
        ma = w
for w in s:
    if len(w) == len(ma):
        print(w)

#Option_4
s = input().split()
res = ['']
for w in s:
    if len(w) == len(res[0]):
        res.append(w)
    elif len(w) < len(res[0]):
        continue
    elif len(w) > len(res[0]):
        res = [w]
print(*res)






















