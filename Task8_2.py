def res(lst):
    for sub_lst in lst:
        sub_lst.sort(reverse = True)
    return sorted(lst, key = len)

print(res([[1,3,4,5,6,7], [2,3,4],[5,6,7,1]]))

