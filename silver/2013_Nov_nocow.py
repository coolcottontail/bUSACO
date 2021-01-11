fin, fout = open('nocow.in'), open('nocow.out', "w")

N, K = tuple(map(int, fin.readline().strip().split()))
a = {}

noCow = []

for _ in range(N):
    f = fin.readline().split()
    l = []
    for i in range(4, len(f) - 1):
        try:
            a[i].append(f[i])
        except:
            a[i] = [f[i]]

        l.append(f[i])

    noCow.append(l)

aL = list(map(lambda x: sorted(list(set(x))), a.values()))

stop = False
aC = []
for cow in aL:
    aC.append(len(cow) - 1)

counts = [0] * len(aL)
print(aC)
for c in range(K):
    cow = []
    up = 0

    for i in range(len(aC)):
            cow.append(aL[i][counts[i]])

    for i in range(len(aC)):
        if i == aC[i]:
            print(i)
            up += 1


    counts[up] += 1
    print(cow)