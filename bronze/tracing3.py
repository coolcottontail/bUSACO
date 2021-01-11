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

minK = 1000000000
maxK = 0

count = set()
for k in range(1, 1 + t):
    for cow0 in list(cowsInMeets):
        tempCows = [' '] + ['0'] * n
        tempCows[cow0] = '1'
        tempD = {}
        for cow in cowsInMeets:
            tempD[cow] = 0

        for meet in meets:
            if tempCows[meet[1]] == '1':
                tempD[meet[1]] += 1
            if tempCows[meet[2]] == '1':
                tempD[meet[2]] += 1

            if tempD[meet[1]] <= k:
                tempCows[meet[2]] = max(tempCows[meet[2]], tempCows[meet[1]])

            if tempD[meet[2]] <= k:
                tempCows[meet[1]] = max(tempCows[meet[2]], tempCows[meet[1]])

        if tempCows == cows:
            count.add(cow0)
            minK = min(k, minK)
            maxK = max(k, maxK)

if maxK == t:
    maxK = 'Infinity'


if minK == 1000000000:
    minK = 0


counter = 0
for cow in cows:
    if cow == '1':
        counter += 1

if counter == 1:
    minK, maxK, count = 0, 0, ['yummy']


fout.write(str(len(count)) + ' ' + str(minK) + ' ' + str(maxK))
