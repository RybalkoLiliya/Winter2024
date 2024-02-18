arg = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
def reqursive(dct, x, res = None):
    if res is None: res = []
    for key, value in dct.items():
        if not isinstance(value, dict):
            if x == key:
                res.append(value)
        else:
            reqursive(value, x, res)
    return res

print(reqursive(arg, x = 2))








