def uppercase_deco(func):
    def wrapper(*args, **kwargs):
        res = []
        for i in args:
            if type(i) == str:
                res.append(i.upper())
        for j in kwargs:
            v = kwargs[j]
            if type(v) == str:
                res.append(v.upper())
        return res
    return wrapper

@uppercase_deco
def abc(*args, **kwargs):
    return
print(abc(5, 'Try', a = 'Go', b = 7))


