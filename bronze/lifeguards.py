fin, fout = open('lifeguards.in'), open('lifeguards.out', 'w')

n = int(fin.readline())
events = []
for i in range(n):
    s, e = list(map(int, fin.readline().split()))
    events.append((s, 0, i + 1))
    events.append((e, 1, i + 1))

events.sort()
events.append((3, 2, 0))

guardD = {}
totalTime = 0
curLifeguards = set()

for i in range(len(events) - 1):
    val, event, ID = events[i]
    valN, eventN, idN = events[i + 1]

    if event == 0:
        curLifeguards.add(ID)
    elif event == 1:
        curLifeguards.remove(ID)

    if len(curLifeguards) == 1:
        try:
            guardD[list(curLifeguards)[0]] += valN - val
        except:
            guardD[list(curLifeguards)[0]] = valN - val

    if len(curLifeguards) > 0:
        totalTime += valN - val

fout.write(str(totalTime - min(guardD.values())))


























