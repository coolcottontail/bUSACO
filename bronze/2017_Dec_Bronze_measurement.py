fIn, fOut = open("measurement.in"), open("measurement.out", "w")
n = int(fIn.readline())
days = []
for _ in range(n):
    d, c, i = fIn.readline().split()
    days.append((int(d), c, int(i)))

days.sort(key=lambda x: x[0])
newDays = [(7, 7, 7)]

for day in days:
    prev = newDays[-1]
    if day[1] == 'Bessie':
        newDays.append((prev[0] + day[2], prev[1], prev[2]))

    elif day[1] == 'Elsie':
        newDays.append((prev[0], prev[1]+ day[2], prev[2]))

    elif day[1] == 'Mildred':
        newDays.append((prev[0], prev[1], prev[2] + day[2]))

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