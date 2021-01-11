fin, fout = open('nocow.in'), open('nocow.out', "w")

N, K = tuple(map(int, fin.readline().strip().split()))

noCow = []

for _ in range(N):
    f = fin.readline().split()
    l = f[4:len(f) - 1]
    noCow.append(l)


numCol = len(noCow[0])
columns = [set() for _ in range(numCol)]

for x in noCow:
    for i in range(numCol):
        columns[i].add(x[i])

for i in range(numCol):
    columns[i] = sorted(list(columns[i]))



counters = [len(x) for x in columns]
def find_x(x):
    pTimes = [1]

    for i in range(len(columns) - 1, 0, -1):
        pTimes.append(pTimes[-1] * counters[i])

    pTimes.reverse()

    kIs = [0] * len(pTimes)
    curI = x

    for i in range(len(pTimes)):
        if curI == 0:
            break

        kIs[i] = (curI // pTimes[i])
        curI %= pTimes[i]

    kXs = []
    for i in range(len(kIs)):
        kXs.append(columns[i][kIs[i]])

    return kXs


switch = 0
found = find_x(K)

if not found in noCow:
    noCow.append(find_x(K))
else:
    switch = 1

noCow.sort()

fout.write(" ".join(find_x(noCow.index(find_x(K)) + K + switch - 1)))
