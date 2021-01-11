fin, fout = open("reduce.in"), open("reduce.out", "w")

n = int(fin.readline())
cows = []
M = 0
for x in range(n):
    cows.append(tuple(map(int, fin.readline().split())))
    M = max(M, cows[-1][1])

fence = [False] * M + [False]

for cow in cows:
    fence[cow[1]] = cow[0]

print(fence)