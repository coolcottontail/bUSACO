fin, fout = open('blist.in'), open('blist.out', 'w')

N = int(fin.readline())
events = []

for _ in range(N):
    f = fin.readline().split()
    events.append((int(f[0]), 0, int(f[2])))
    events.append((int(f[1]), 1, int(f[2])))

events.sort()
curBuckets = 0
storedBuckets = 0

for event in events:
    if event[1] == 0:
        if event[2] - storedBuckets >= 0:
            curBuckets += event[2]
            storedBuckets = 0

        elif storedBuckets - event[2] > 0:
            curBuckets += event[2]
            storedBuckets -= event[2]

    else:
        curBuckets -= event[2]
        storedBuckets += event[2]

fout.write(str(storedBuckets))