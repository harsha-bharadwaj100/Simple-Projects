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


print(FIFO(sequence, fsize))
print(LRU(sequence, fsize))
# print(OPT(sequence, fsize))
