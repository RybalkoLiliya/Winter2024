n = input()
dct = {}
def f_ten(n):
  for symb in n:
    symb = symb.lower()
    dct[symb] = dct.get(symb,0)+1
    n_dct = dict(sorted(dct.items()))
    res_array = sorted(n_dct.items(), key = lambda item: item[1],reverse = True)
  return print(dict(res_array[0:10]))

f_ten(n)


