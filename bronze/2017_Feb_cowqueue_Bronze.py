fIn, fOut = open("cowqueue.in"), open("cowqueue.out", "w")

n = int(fIn.readline())
cows = []

for cow in range(n):
    cows.append(tuple(map(int, fIn.readline().strip().split())))

cows.sort(key=lambda x: (x[0], x[1]))
cowsinline = []

time = 0

for cow in cows:
    if cow[0] > time:
        time = cow[0]
    time += cow[1]

fOut.write(str(time))