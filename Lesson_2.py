#Task_1
for i in range(1, 0):
    if i % 15 == 0: break #Вылет из цикла, переход на следующую строку
    if i % 2 != 0: continue # Идти вначало цикла, не выполняя оператора
    print(i, end = " ")
else:
    print("Нормальное завершение")

#Task_2
for i in "Hello, world":
    if i == "o": continue
    print(i*2, end = "")
else:
    print("\tagain") #\n либо \t

#Task_3
for i in "Hello, world":
    if i == "o": break
    print(i*2, end = "")
else:
    print("\tagain")

#Task_4
for i in "Hello, world":
    if i == 'a':
        break

else:
    print(" В строке нет буквы а")

#Task_5
n = int(input())
for i in range(n):
    print(i, end = ",")
    if i > 10: break
    elif i % 2 == 0: continue
else:
    print("ИТОГ", i)

#n = int(input())
#for i in range(n):
#   print(i, end = ":")
    #if i > 10: break
    #elif i % 2 == 0: continue
    #else:
        #print(" ", i)








