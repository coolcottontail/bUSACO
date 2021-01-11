fin, fout = open('tracing.in'), open('tracing.out', 'w')
n, t = list(map(int, fin.readline().split()))
cows = [' '] + list(fin.readline())
cows.remove('\n')

meets = [tuple(map(int, fin.readline().strip().split())) for _ in range(t)]
meets.sort()
cowsInMeets = set()
for meet in meets:
    cowsInMeets.add(meet[0])
    cowsInMeets.add(meet[1])

notInfected = set()

for meet in meets:
    if meet[1] not in notInfected:
        try:
            notInfected.remove(meet[1])
        except:
            pass

        try:
            notInfected.remove(meet[2])
        except:
            pass

    if cows[meet[1]] == '0' or cows[meet[2]] == '0':
        notInfected.add(meet[1])
        notInfected.add(meet[2])

    print(notInfected)
print(notInfected)