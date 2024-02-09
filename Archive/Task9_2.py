s_1 = input().lower()
n = int(input())
s_2 = []
i = 0
while i < n:
    t = input().lower()
    s_2.append(t)
    i += 1

vowels = 'ауоыиэяюёе'
def find(string, vowels):
    for i, c in enumerate(string):
        if c in vowels:
            yield i

string = s_1
indices_1 = list(find(string, vowels))
#print(f'Индекс первого слова: {indices_1}')

all_other = {}
for i in range(len(s_2)):
    string = s_2[i]
    all_other[s_2[i]] = list(find(string, vowels))
#print(f'Индексы для сравнения: {all_other.values()}')

indices_2 = list(all_other.values())
res = []
for j in range(0, len(indices_2)):
    if indices_1 == indices_2[j]:
        res.append(s_2[j])
print(', '.join(res))













