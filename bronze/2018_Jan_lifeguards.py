import copy

# Deal Input and Output
fIn, fOut = open("lifeguards.in"), open("lifeguards.out", "w")

n = int(fIn.readline())
lg = []

for _ in range(n):
    f = tuple(map(int, fIn.readline().split()))
    lg.append(f)

lg.sort(key=lambda x: (x[0], x[1]))

maxDis = 0
for firedLG in lg:
    tempLG = copy.deepcopy(lg)
    tempLG.remove(firedLG)
    print(tempLG)
    temp = []
    for f in tempLG:
        temp.append((f[0], 0))
        temp.append((f[1], 1))
    temp.sort(key=lambda x: (x[0], x[1]))

    dis = 0
    for timeI in range(len(temp) - 1):
        time, key = temp[timeI]
        time1, key1 = temp[timeI + 1]

        if key == 0 and key1 == 0:
            dis += time1 - time
        elif key == 0 and key1 == 1:
            dis += time1 - time
        elif key == 1 and key1 == 1:
            dis += time1 - time
    maxDis = max(maxDis, dis)
fOut.write(str(maxDis))
