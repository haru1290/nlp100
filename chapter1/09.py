import random

str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = [i if len(i) <= 4 else i[:1] + "".join(random.sample(i[1:-1], len(i)-2)) + i[-1:] for i in str.split()]
print(ans)
