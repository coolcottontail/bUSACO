fin, fout = open('notlast.in'), open('notlast.out', 'w')

cows = {'Bessie': 0}
n = int(fin.readline())
for x in range(n):
    read = fin.readline().split()
    try:
        cows[read[0]] += int(read[1])
    except:
        cows[read[0]] = int(read[1])



min1 = [('Bessie', 103)]
min2 = [('Bessie', 103)]
for cow in cows:
    cowVal = cows[cow]
    if cowVal < min1[0][1]:
        min2 = min1
        min1 = [(cow, cowVal)]
    elif cowVal == min1[0][1]:
        min1.append((cow, cowVal))
    elif cowVal < min2[0][1]:
        min2 = [(cow, cowVal)]
    elif cowVal == min2[0][1]:
        min2.append((cow, cowVal))

if len(min2) == 1:
    fout.write(min2[0][0])
else:
    fout.write('Tie')


