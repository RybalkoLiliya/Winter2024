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
        return print(res)
    return wrapper

@uppercase_deco
def abc(*args, **kwargs):
    return
abc(5, 'Try', a = 'Go', b = 7)


