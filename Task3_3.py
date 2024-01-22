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









#for j in range(i):
#   if len(s[j]) == len(s[ind]): answer.append(s[ind])
#   print(answer)















