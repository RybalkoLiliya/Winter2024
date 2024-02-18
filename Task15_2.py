import re
def search_number(num):
    regex = (r'[A, B, E, K, M, H, O, P, C, T, X, Y, А, В, Е, К, М, Н, О, Р, С, Т, Х, У]\d{3}[A, B, E, K, M, H, O, P, C, T, X, Y, А, В, Е, К, М, Н, О, Р, С, Т, Х, У]{2}\d{2,3}')
    res = re.findall(regex, num)
    if res == []:
        return None
    else:
        return res
data = 'A123BC78M676ХХ178jyyyyyyjjhh77'
result = search_number(data)
print(result)
