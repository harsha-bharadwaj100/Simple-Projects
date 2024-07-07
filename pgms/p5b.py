with open("pgms\lores.txt", "r") as f:
    txt = f.read()
    print(txt)
    for i in txt:
        if i == i.upper() and i.isalpha():
            print(i)
            txt = txt.replace(i, "")
with open("pgms\loresCopy.txt", "w+") as f:
    f.write(txt)
    f.seek(0)
    print(f"Modified Content:\n{f.read()}")
    f.seek(0)
    lines = len(f.readlines())
    print(f"Lines = {lines}")
