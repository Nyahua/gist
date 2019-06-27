import re

s = "RMB1,234.56 万元"
pat = "[^0-9.]+"
print(re.sub(pat, "", s))
