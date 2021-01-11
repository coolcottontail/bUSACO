fin, fout = open("socdist2.in"), open("socdist2.out", "w")

n = int(fin.readline())
cows = [list(map(int, fin.readline().split())) for _ in range(n)]
cows.sort()

r = 10e9
for cow in range(1, n):
    if cows[cow][1] == 0 and cows[cow - 1][1] == 1:
        r = min(r, cows[cow][0] - cows[cow - 1][0])
    if cows[cow][1] == 1 and cows[cow - 1][1] == 0:
        r = min(r, cows[cow][0] - cows[cow - 1][0])
r -= 1

ans = 1

newCows = []
for cow in cows:
    if cow[1] == 1:
        newCows.append(cow[0])


count = 0
print("radius: ", r)
for cow in newCows:
    count += 1
    if count % 10 == 0:
        print()
    print(cow, end=' ')

print("\n")

p1 = 0
p2 = 0
group = newCows[p1] + r

while len(newCows) > p2 and len(newCows) > p1:
    if newCows[p2] <= group:
        group = newCows[p2] + r
    else:
        print('dbg', newCows[p2] - newCows[p1], p1)
        p1 = p2
        ans += 1
        group = newCows[p2] + r

    p2 += 1



fout.write(str(ans))
