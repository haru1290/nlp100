def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    splits = s.split()
    num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    ans = {}

    for i, w in enumerate(splits, 1):
        if i in num_list:
            ans[w[:1]] = i
        else:
            ans[w[:2]] = i

    print(ans)

if __name__ == "__main__":
    main()
