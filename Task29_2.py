from itertools import zip_longest
def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip_longest(str1, str2))

print(hamming_distance('abc', 'xyz'))