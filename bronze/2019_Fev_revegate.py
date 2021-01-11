fin, fout = open("revegetate.in"), open("revegetate.out", "w")

n, m = tuple(map(int, fin.readline().split()))

cows = []
for x in range(m):
    cows.append(tuple(map(int, fin.readline().strip().split())))
count = 0

for order in range(int('1' * n), int('4' * n) + 1):
    success = True
    order = str(order)


    if '0' in order:
        continue

    for cow in cows:
        if order[cow[0] - 1] == order[cow[1] - 1]:
            success = False

    if success:
        fout.write(order)
        break