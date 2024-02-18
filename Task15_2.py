import re
def search_number(num):
    regex = (r'[ABEKMHOPCTXYАВЕКМНОРСТХУ]\d{3}[ABEKMHOPCTXYАВЕКМНОРСТХУ]{2}\d{2,3}')
    res = re.findall(regex, num)
    if res == []:
        return None
    else:
        return res
data = 'A123BC78M676ХХ178jyyyyyyjjhh77'
result = search_number(data)
print(result)
