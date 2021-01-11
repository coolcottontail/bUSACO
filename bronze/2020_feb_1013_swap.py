import copy

fin, fout = open('swap.in'), open('swap.out', 'w')

n, k = list(map(int, fin.readline().split()))

a = list(map(lambda x: int(x) - 1, fin.readline().split()))
b = list(map(lambda x: int(x) - 1, fin.readline().split()))

fCows = list(range(n + 1))

cows =[0] + fCows[1:a[0]+1] + fCows[a[0]+1: a[1] + 2][::-1] + fCows[a[1] + 2:]

cows =[0] + cows[1:b[0]+1] + cows[b[0]+1: b[1] + 2][::-1] + cows[b[1] + 2:]


m = {}
for i in range(1, n+1):
    m[i] = cows[i]

out = cows

for _ in range(k - 1):
    cows = [0] + [cows[m[i]] for i in range(1, n+1)]

for cow in range(1, len(cows)):
    fout.write(str(cows[cow]) + '\n')