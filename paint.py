import copy
fin, fout = open('paint.in'), open("paint.out", "w")

N = int(fin.readline())
bessie = []
mMin = 10e9
mMax = 0

for x in range(N):
    f = fin.readline().split()
    bessie.append([int(f[0]), f[1]])
    mMin = min(int(f[0]), mMin)
    mMax = max(int(f[0]), mMax)

start = mMin
fence = {}

for turn in bessie:
    prevStart = copy.deepcopy(start)

    if turn[1] == 'L':
        start -= turn[0]
    else:
        start += turn[0]
    sorted = [prevStart, start]
    sorted.sort()

    for i in range(sorted[0], sorted[1]):
        try:
            fence[i] += 1

        except:
            fence[i] = 1
ans = 0
for part in fence:
    if fence[part] >= 2:
        ans += 1

fout.write(str(ans))