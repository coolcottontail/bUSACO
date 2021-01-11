import copy

fIn, fOut = open("marathon.in"), open("marathon.out", "w")

def dis(o, t):
    return abs(o[0] - t[0]) + abs(t[1] - o[1])

N = int(fIn.readline())
coors = []

for x in range(N):
    coors.append(list(map(int, fIn.readline().split())))


m = 10e9
for i in range(1, N):
    temp = copy.deepcopy(coors)
    temp.pop(i)

    d = 0
    for pointI in range(N - 2):
        d += dis(temp[pointI], temp[pointI + 1])
    m = min(d, m)


fOut.write(str(m) + '\n')
