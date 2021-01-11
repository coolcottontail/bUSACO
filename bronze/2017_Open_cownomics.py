fIn, fOut = open("cownomics.in"), open("cownomics.out", "w")

n, m = tuple(map(int, fIn.readline().split()))
spotcow = [fIn.readline().strip() for cow in range(n)]
clearcow = [fIn.readline().strip() for cow in range(n)]
count = 0

for row in range(m):
    data1 = set()
    data2 = set()
    for x in spotcow:
        data1.add(x[row])

    for x in clearcow:
        data2.add(x[row])

    if data1 != data2 and len(data1.intersection(data2)) == 0:
        count += 1

fOut.write(str(count))