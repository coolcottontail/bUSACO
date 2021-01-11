fin, fout = open('lifeguards.in'), open('lifeguards.out', 'w')

n = int(fin.readline())
events = []
for i in range(n):
    s, e = list(map(int, fin.readline().split()))
    events.append((s, i + 1))
    events.append((e, i + 1))

events.sort()

guardD = [0] + [0] * n
totalTime = 0
curLifeguards = set()


for i in range(0, len(events)):
    val, ID = events[i]
    if i > 0:
        valP, idP = events[i - 1]
    else:
        valP, idP = val,  ID

    if len(curLifeguards) == 1:
        guardD[list(curLifeguards)[0]] += val - valP


    if len(curLifeguards) > 0:
        totalTime += val - valP

    if ID in curLifeguards:
        curLifeguards.remove(ID)
    else:
        curLifeguards.add(ID)

guardD.pop(0)

try:
    fout.write(str(totalTime - min(guardD)))
except:
    fout.write(str(totalTime))
    print('Bunny')