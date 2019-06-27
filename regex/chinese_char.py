import re

pat = r'[\u4e00-\u9fff]+'

text = "abc汉字123"

print(re.findall(pat, text))
