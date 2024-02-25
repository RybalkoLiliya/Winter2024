import re

s = input()
n = int(input())
nums = re.findall(r'[+-]?\d+', s)
nums = [int(i) for i in nums if int(i) < n and int(i) >= 0]
print(nums)
