import re
def search_number(num):
    regex = (r'(?:\+7)(?:\(\d{3}\))\d{3}-\d{2}-\d{2}|(?:\+7)(?:\(\d{3}\))\d{3}-\d{4}')
    res = re.findall(regex, num)
    if res == []:
        return None
    else:
        return res

data = '+78121112222, -7(812)222-83-44 +7(921)678-98-78+7(921)777-4433'
result = search_number(data)
print(result)
