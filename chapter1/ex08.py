def cipher(s):
    return "".join([chr(219-ord(c)) if c.islower() else c for c in s])

def main():
    s = "I am an NLPer"

    print("平文　：", s)
    print("暗号文：", cipher(s))
    print("復号文：", cipher(cipher(s)))

if __name__ == "__main__":
    main()
