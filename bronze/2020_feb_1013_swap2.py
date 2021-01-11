fin, fout = open('swap.in'), open('swap.out', 'w')

n, k = list(map(int, fin.readline().split()))

a = list(map(lambda x: int(x) - 1, fin.readline().split()))
b = list(map(lambda x: int(x) - 1, fin.readline().split()))

fCows = list(range(n + 1))

cows = [0] + fCows[1:a[0] + 1] + fCows[a[0] + 1: a[1] + 2][::-1] + fCows[a[1] + 2:]

cows = [0] + cows[1:b[0] + 1] + cows[b[0] + 1: b[1] + 2][::-1] + cows[b[1] + 2:]

count = 1
while cows != list(range(n + 1)):
    cows = [0] + cows[1:a[0] + 1] + cows[a[0] + 1: a[1] + 2][::-1] + cows[a[1] + 2:]

    cows = [0] + cows[1:b[0] + 1] + cows[b[0] + 1: b[1] + 2][::-1] + cows[b[1] + 2:]

    count += 1


def swap(x):
    x = [0] + x[1:a[0] + 1] + x[a[0] + 1: a[1] + 2][::-1] + x[a[1] + 2:]
    x = [0] + x[1:b[0] + 1] + x[b[0] + 1: b[1] + 2][::-1] + x[b[1] + 2:]

    return x

for _ in range(k % count):
    cows = swap(cows)

for cow in cows:
    if cow != 0:
        fout.write(str(cow) + '\n')