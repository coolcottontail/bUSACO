fin, fout = open('shuffle.in'), open('shuffle.out', 'w')

n = int(fin.readline())
o = list(map(int , fin.readline().split()))
order = {}

for x in range(len(o)):
    order[x] = o[x]


cows = fin.readline().split()

for cowindex in range(n):
    curcowindex = cowindex + 1

    for x in range(3):
        curcowindex = order[curscowindex - 1]

    fout.write(cows[curcowindex - 1] + '\n')