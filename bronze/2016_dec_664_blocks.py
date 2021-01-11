fIn, fOut = open('blocks.in'), open('blocks.out', 'w')
n = int(fIn.readline())
boards = [fIn.readline().split() for _ in range(n)]
binLst = [x for x in range(2 ** n)]

l = [0] * 26
for mNum in binLst:
    print(mNum)

    bitmask = mNum
    for i in range(n):
        mNum >>= 1
        bit = mNum & 1

        tempL = [0] * 26
        for i in range(len(boards)):
            for letter in boards[i][bit]:
                try:
                    tempL[ord(letter) - ord('a')] += 1
                except:
                    tempL[ord(letter) - ord('a')] = 1

    for i in range(26):
        if l[i] < tempL[i]:
            l[i] = tempL[i]

for letter in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
    try:
        fOut.write(str(l[ord(letter) - ord('a')]) + '\n')
    except:
        fOut.write(str(0))
