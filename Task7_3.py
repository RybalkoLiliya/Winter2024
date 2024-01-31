def max_num(lst):
    result = sorted(sum(lst, []), reverse=True)
    print(sorted(result[0:3]))


max_num([[2, 3, 4], [4, 5, 6], [45, 3, -5]])
