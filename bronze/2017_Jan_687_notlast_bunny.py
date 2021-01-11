fin, fout = open('notlast.in'), open('notlast.out', 'w')

cows = {}

cows['Bessie'] = 0
cows['Elsie'] = 0
cows['Daisy'] = 0
cows['Gertie'] = 0
cows['Annabelle'] = 0
cows['Maggie'] = 0
cows['Henrietta'] = 0

n = int(fin.readline())
for x in range(n):
    read = fin.readline().split()
    try:
        cows[read[0]] += int(read[1])
    except:
        cows[read[0]] = int(read[1])

cowTLst = [(cows[x],x) for x in cows]
cowTLst.sort()

min = cowTLst[0][0]

min2count = 0
min2 = 101

first = 0
for cow in cowTLst:
    if cow[0] != min:
        if first == 0:
            min2count += 1
            first = 1
            min2 = cow
        elif min2[0] == cow[0]:
            min2count += 1
            min2 = cow

if min2count == 1:
    fout.write(min2[1])
else:
    fout.write('Tie')