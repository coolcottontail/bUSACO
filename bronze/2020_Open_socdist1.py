fin, fout = open('socdist1.in'), open('socdist1.out', 'w')

N = int(fin.readline())
stalls = fin.readline()
DList = [0]
oneList = []
twoList = []
for i in range(len(stalls)):
    if stalls[i] == '1':
        oneList.append(i)
    else:
        twoList.append(i)

for x in range(len(oneList) - 1):
    DList.append(oneList[x + 1] - oneList[x])

for D in range(1 + min(DList),  0, -1):
    working = 0
    for x in DList:
        if D * 2 <= x:
            print(x, D)
            working += 1

    if working >= 2:
        break

fout.write(str(D))