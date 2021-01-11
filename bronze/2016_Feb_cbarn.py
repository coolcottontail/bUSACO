import copy

fIn, fOut = open("cbarn.in"), open("cbarn.out", "w")

n = int(fIn.readline())
target = [int(fIn.readline()) for _ in range(n)]

s = 0

tNew = copy.deepcopy(target)


def reverse(x):
    return x[1:] + [x[0]]


mSum = []

for start in target:
    print(tNew)
    ans = 0
    for i in range(n):
        ans += i * tNew[i]
    tNew = reverse(tNew)

    mSum.append(ans)
fOut.write(str(min(mSum)))
