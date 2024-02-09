def res(lst):
    for sub_lst in lst:
        sub_lst.sort(reverse = True)
    return sorted(lst, key = lambda x: len((''.join(map(str, x)))))

print(res([[1,3,4,5,6], [26,39,46],[556778,34567]]))
