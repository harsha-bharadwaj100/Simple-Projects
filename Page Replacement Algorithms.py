# ipstring = input("Enter the string: ")
# fsize = int(input("Enter frame size: "))
ipstring = "7 0 1 2 0 3 0 4 2 3 0 3 0 3 2 1 2 0 1 7 0 1"
fsize = 3
sequence = list(map(int, ipstring.split()))


def FIFO(seq, n):
    pagefaults = []
    hits = []
    frame = [None] * n
    pos = 0
    for i in range(len(seq)):
        if seq[i] not in frame:
            frame[pos] = seq[i]
            pos = (pos + 1) % n
            pagefaults.append(i)
        else:
            hits.append(i)
    return pagefaults, hits


def LRU(seq, n):
    pagefaults = []
    hits = []
    frame = [None] * n
    pos = 0
    lru = dict()
    for i in range(len(seq)):
        lru[seq[i]] = i
        if seq[i] not in frame:
            if None in frame:
                frame[pos] = seq[i]
                pos = pos + 1
            else:
                pos = frame.index(min(frame, key=lambda x: lru[x]))
                frame[pos] = seq[i]
            pagefaults.append(i)
            print(frame, lru, seq[i], "pagefault")
        else:
            hits.append(i)
            print(frame, lru, seq[i], "hit")
    return pagefaults, hits


def OPT(seq, n):
    pagefaults = []
    hits = []
    frame = [None] * n
    pos = 0
    opt = dict()
    for i in range(len(seq)):
        if seq[i] in opt:
            opt[seq[i]].append(i)
        else:
            opt[seq[i]] = [i]
    print(opt)
    for i in range(len(seq)):
        if seq[i] not in frame:
            if None in frame:
                frame[pos] = seq[i]
                pos = pos + 1
                # remove the first occurance of the element from opt
            else:
                # framefirstoccurance = [opt[x][0] for x in frame]
                pos = frame.index(
                    max(
                        frame,
                        key=lambda x: opt[x][0] if len(opt[x]) > 0 else len(seq) + 1,
                    )
                )
                frame[pos] = seq[i]
            del opt[seq[i]][0]
            pagefaults.append(i)
            print(frame, seq[i], "pagefault")
            print(opt)
        else:
            hits.append(i)
            del opt[seq[i]][0]
            print(frame, seq[i], "hit")
            print(opt)
    return pagefaults, hits


print(FIFO(sequence, fsize))
print(LRU(sequence, fsize))
print(OPT(sequence, fsize))
