def res(lst):
    res = sorted(lst, key = lambda x: (-len(set(x)), x))
    print(res)

res(['abab', 'xx', 'aaaaaaa', 'abcbab'])




