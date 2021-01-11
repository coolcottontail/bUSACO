import itertools

fin, fout = open('lineup.in'), open('lineup.out', 'w')

n = int(fin.readline())
restrictions = []

for _ in range(n):
    restrictions.append(fin.readline().strip().split(' must be milked beside '))

cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
cows.sort()
count = 0

for cowOrdering in itertools.permutations(cows):
    passed = True
    for cow1, cow2 in restrictions:
        if abs(cowOrdering.index(cow1) - cowOrdering.index(cow2)) != 1:
            passed = False

    if passed:
        break

for cow in cowOrdering:
    fout.write(cow + '\n')