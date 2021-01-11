fin, fout = open('speeding.in'), open('speeding.out', 'w')

N, M = tuple(map(int, fin.readline().split()))

road = []
for _ in range(N):
    f = list(map(int, fin.readline().strip().split()))
    for _ in range(f[0]):
        road.append(f[1])

bessie = []
for i in range(M):
    f = list(map(int, fin.readline().strip().split()))
    for _ in range(f[0]):
        bessie.append(f[1])

ans = 0
for i in range(100):
    r = road[i]
    b = bessie[i]
    ans = max(b - r, ans)

fout.write(str(ans))