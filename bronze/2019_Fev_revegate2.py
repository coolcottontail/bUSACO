import itertools
fin, fout = open("revegetate.in"), open("revegetate.out", "w")

n, m = tuple(map(int, fin.readline().split()))

cows = []
for x in range(m):
    cows.append(tuple(map(int, fin.readline().strip().split())))
count = 0

print(cows)