import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
splits = re.sub("[,|.]", "", str).split()
ans = [len(i) for i in splits]
print(ans)
