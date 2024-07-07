def countWords(fname):
    try:
        f = open(fname, "r")
        cont = f.read()
        return len(cont.split())
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()


print(countWords(r"pgms\lores.txt"))
