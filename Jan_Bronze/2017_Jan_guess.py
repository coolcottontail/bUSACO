import itertools

fIn, fOut = open('guess.in'), open('guess.out', "w")

N = int(fIn.readline())
animals = {}
char = set()

for _ in range(N):
    f = fIn.readline().split()
    d = f[2:]
    animals[f[0]] = d

    for x in d:
        char.add(x)
ans = 0
stop = False
for permute in itertools.permutations(list(char)):
    avaAni = set()
    for x in animals:
        avaAni.add(x)
    counter = 0
    for thing in permute:
        for ani in animals:
            if thing not in ani:
                avaAni.remove(ani)
            counter += 1
            if len(avaAni) == 1:
                stop = True
                break

        if stop:
            ans = max(ans, counter)
            break

fOut.write(str(ans))