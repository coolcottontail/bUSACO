fIn, fOut = open('blocks.in'), open('blocks.out', 'w')
n = int(fIn.readline())
boards = [fIn.readline().split() for _ in range(n)]

ans = []
for board in boards:
    front = board[0]
    back = board[1]

ans.sort()

d = {}

for x in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
    d[x] = 0

# d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
# 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for x in ans:
    d[x] += 1


for v in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
    fOut.write(str(d[v]) + '\n')
