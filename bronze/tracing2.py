fin, fout = open('tracing.in'), open('tracing.out', 'w')
n, t = list(map(int, fin.readline().split()))
cows = [' '] + list(fin.readline())
cows.remove('\n')

meets = [tuple(map(int, fin.readline().strip().split())) for _ in range(t)]
meets.sort()
cowsInMeets = set()
for meet in meets:
    cowsInMeets.add(meet[1])
    cowsInMeets.add(meet[2])

minK = 10e9
maxK = 0

count = set()
for k in range(1, 1 + t):
    yes = False
    for cow0 in list(cowsInMeets):
        tempCows = [' '] + ['0'] * n
        tempCows[cow0] = '1'
        tempD = {}
        for cow in cowsInMeets:
            tempD[cow] = 0

        for meet in meets:
            if tempCows[meet[1]] == '1' and tempD[meet[1]] <= k:
                tempCows[meet[2]] = '1'
                tempD[meet[1]] += 1

            if tempCows[meet[2]] == '1' and tempD[meet[2]] <= k:
                tempCows[meet[1]] = '1'
                tempD[meet[2]] += 1


        if tempCows == cows:
            count.add(cow0)
            yes = True

    if yes:
        minK = min(k, minK)
        maxK = max(k, maxK)

if maxK == t:
    maxK = 'Infinity'


if minK == 10e9:
    minK = 0

fout.write(str(len(count)) + ' ' + str(minK) + ' ' + str(maxK))
