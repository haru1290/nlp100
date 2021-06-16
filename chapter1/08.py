def cipher(str):
    return "".join([chr(219-ord(i)) if i.islower() else i for i in str])

str = "I am an NLPer"
cr_str = cipher(str)
de_str = cipher(cr_str)

print("平文　：", str)
print("暗号文：", cr_str)
print("復号文：", de_str)
