fIn, fOut = open('blocks.in'), open('blocks.out', 'w')
n = int(fIn.readline())
boardsFront = []
boardsBack = []
for _ in range(n):
    f = fIn.readline().split()
    boardsFront += f[0]
    boardsBack += f[1]

coun