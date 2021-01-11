fin, fout = open('swap.in'), open('swap.out', 'w')

n, m, k = list(map(int, fin.readline().split()))

swapOrder = []

for _ in range(m):
    swapOrder.append(list(map(lambda x: int(x) - 1, fin.readline().split())))

cows = list(range(n + 1))

for s in swapOrder:
    cows = [0] + cows[1:s[0] + 1] + cows[s[0] + 1: s[1] + 2][::-1] + cows[s[1] + 2:]


count = 1
while cows != list(range(n + 1)):
    for s in swapOrder:
        cows = [0] + cows[1:s[0] + 1] + cows[s[0] + 1: s[1] + 2][::-1] + cows[s[1] + 2:]

    count += 1


def swap(x):
    for s in swapOrder:
        x = [0] + x[1:s[0] + 1] + x[s[0] + 1: s[1] + 2][::-1] + x[s[1] + 2:]

    return x


for _ in range(k % count):
    cows = swap(cows)

for cow in cows:
    if cow != 0:
        fout.write(str(cow) + '\n')