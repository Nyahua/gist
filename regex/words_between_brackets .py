import re
cl, cr = "[]"
pat = re.compile(rf'(?<=\{cl}).+?(?=\{cr})')
s = "my string contains [word] in [brackets]. "
re.findall(pat, s)
