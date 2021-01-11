fin, fout = open('milktemp.in'), open('milktemp.out', 'w')

N, X, Y, Z = list(map(int, fin.readline().split()))
cows = []
MAX = 0

for _ in range(N):
    f = tuple(map(int, fin.readline().split()))
    cows.append((f[0], 0))
    cows.append((f[1], 1))
cows.sort()

M = N * X
for cow in cows:
    if cow[1] == 0:
        M += (Y - X)
    else:
        M += (Z - Y)

    MAX = max(M, MAX)

fout.write(str(MAX))