def n_gram(n, lst):
    return list(zip(*[lst[i:] for i in range(n)]))

str1 = "paraparaparadise"
str2 = "paragraph"
X = set(n_gram(2, str1))
Y = set(n_gram(2, str2))
s_union = X | Y
s_intersection = X & Y
s_difference = X - Y

print("X=", X)
print("Y=", Y)
print("和集合", s_union)
print("積集合", s_intersection)
print("差集合", s_difference)
print("Xにseが含まれるか？", {('s', 'e')} <= X)
print("Yにseが含まれるか？", {('s', 'e')} <= Y)
