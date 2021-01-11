fin, fout = open('cow.in'), open('cow.out', 'w')

n = int(fin.readline())
s = fin.readline()

cCount = 0
coCount = 0
cowCount = 0

for i in range(n):
    if s[i] == 'C':
        cCount += 1

    elif s[i] == 'O':
        coCount += cCount

    elif s[i] == 'W':
        cowCount += coCount

fout.write(str(cowCount))