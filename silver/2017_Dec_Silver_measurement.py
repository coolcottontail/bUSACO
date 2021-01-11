import copy

fIn, fOut = open("measurement.in"), open("measurement.out", "w")

n, g = tuple(map(int, fIn.readline().split()))

days = []
maxC = 0

for _ in range(n):
    d, c, i = fIn.readline().split()
    maxC = max(maxC, int(c))
    days.append((int(d), int(c), int(i)))

days.sort(key=lambda x: x[0])

newDays = [[g] + [g] * maxC]


for day in days:
    prev = newDays[-1]

    cur = copy.deepcopy(prev)

    print(day, cur)
    cur[day[1]] += day[2]

    newDays.append(cur)

maxList = []

for day in newDays:
    m = max(day)
    maxList.append([i for i, j in enumerate(day) if j == m])

count = 0
prev = maxList[0]

for x in maxList:
    if x != prev:
        count += 1

    prev = x

fOut.write(str(count))
