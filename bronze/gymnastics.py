fin, fout = open('gymnastics.in'), open('gymnastics.out', 'w')

k, n = tuple(map(int, fin.readline().split()))
rankings = [list(map(int, fin.readline().strip().split())) for _ in range(k)]

cows = list(range(1, 1 + n))
ans = 0
for cow1 in cows:
    for cow2 in cows:
        if cow1 != cow2:
            consistent = True
            for ranking in rankings:
                if ranking.index(cow1) < ranking.index(cow2):
                    consistent = False

            if consistent:
                ans += 1

fout.write(str(ans))