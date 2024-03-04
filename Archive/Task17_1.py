import re

n = input()
output = re.sub(r'\b(\w+)(?:\W+\1\b)+', r'\1', n, flags=re.IGNORECASE)
print(output)
