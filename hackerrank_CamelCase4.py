# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys


def split(cse):
    finded = re.findall("[A-Z][a-z]*", string=cse)
    for stuff in finded:
        cse = cse.replace(stuff, "")
    words = [cse] + finded
    words = [w.lower() for w in words]
    return " ".join(words)


def comb(ws, ir):
    wsl = ws.split(" ")
    if ir == "C":
        res = "".join([w.capitalize() for w in wsl])
    elif ir == "M":
        res = wsl[0] + "".join([w.capitalize() for w in wsl[1:]]) + "()"
    elif ir == "V":
        res = wsl[0] + "".join([w.capitalize() for w in wsl[1:]])
    return res


dinl = sys.stdin.readlines()
# dinl = [
#     "S;M;plasticCup()",
#     "C;V;mobile phone",
#     "C;C;coffee machine",
#     "S;C;LargeSoftwareBook",
#     "C;M;white sheet of paper",
#     "S;V;pictureFrame",
#     "C;V;white sheet of paper",
#     "C;M;white sheet of paper",
#     "C;C;white sheet of paper",
# ]
dinl = [din.strip() for din in dinl]
for din in dinl:
    op = din[0]
    ir = din[2]
    st = din[4:]
    st = st.replace("()", "")

    if op == "S":
        print(split(st).strip())

    if op == "C":
        print(comb(st, ir).strip())
