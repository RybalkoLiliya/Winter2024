lst = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
lst_res = ([i for i in range(len(lst)) if lst[i] == min(lst)],
           [i for i in range(len(lst)) if lst[i] == max(lst)])
print(lst_res)



