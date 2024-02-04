n = input()
conv_dict={
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'
}

def conv(n):
    for l in n:
        rna_string = ''
        rna_string = rna_string + conv_dict[l.upper()]
        print(rna_string, end = '')

conv(n)