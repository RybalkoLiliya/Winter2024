lst = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
def res(lst):
    lst_min = [i for i in range(len(lst)) if lst[i] == min(lst)]
    lst_max = [i for i in range(len(lst)) if lst[i] == max(lst)]
    return print(f'{lst_min}, {lst_max}')
res(lst)
