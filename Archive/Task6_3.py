n = input()
# n = input().lower()
ab = []
num = []
punc = []
for i in n:
    if i.isalpha():
        ab.append(i)
    elif i.isalnum():
        num.append(i)
    else:
        punc.append(i)
print(f'{set(ab)}\n{set(num)}\n{set(punc)}')

