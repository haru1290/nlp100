import re

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
splits = re.sub("[.]", "", str).split()
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}
for i, w in enumerate(splits):
    if i+1 in num_list:
        ans[w[:1]] = i+1
    else:
        ans[w[:2]] = i+1
print(ans)
