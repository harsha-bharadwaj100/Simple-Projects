import re

pl = ["fox", "dog", "horse", "A"]
for p in pl:
    match = re.search(p, "A quick brown fox jumps over the lazy dog")
    # print(match.string, match.span())
    print(match)
