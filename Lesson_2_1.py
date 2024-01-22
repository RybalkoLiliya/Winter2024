#Task1
s = "Hello world"
for i in range(1):
    print(s[1:i])
#Task2
s = "Hello world"
print(s[1:15:2])

#Task3
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("+", end = "")
    print()
#Task4
a = [4, "f"] #строка
s = []
print(s, type(s))

s = list("Hello")
print(s, type(s))

s = list("Hello")
for i in range(5):
    print(s[i])

s = list("Hello")
print(s)
s[0] = 123
for i in range(5):
    print(s[i])
#1
s = list("Hello")
print(s)
print(len(s))

#2
s = list("Hello")
for i in s:
    print(i)
for j in range(len(s)):
    print(s[j])