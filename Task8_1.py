str = input()
str = [str[i:i+2] for i in range(0, len(str), 2)]
def swap(str):
    new_str = []
    for i in range(len(str)):
        if str[i] == 'АГ':
            new_str.append('ГА')
        elif str[i] == 'ГА':
            new_str.append('АГ')
        elif str[i] == 'ЦТ':
            new_str.append('ЦАГТ')
        elif str[i] == 'ТЦ':
            new_str.append('ТАГЦ')
    return print(''.join(new_str))

swap(str)




