# Link
# http://www.usaco.org/index.php?page=viewproblem2&cpid=591

fin, fout = open('promote.in'), open('promote.out', 'w')


b = list(map(int, fin.readline().split()))
s = list(map(int, fin.readline().split()))
g = list(map(int, fin.readline().split()))
p = list(map(int, fin.readline().split()))

goldToPlatinum = p[1] - p[0]
silverToGold = g[1] - g[0] + goldToPlatinum
bronzeToSilver = s[1] - s[0] + silverToGold

fout.write(str(bronzeToSilver) + '\n')
fout.write(str(silverToGold) + '\n')
fout.write(str(goldToPlatinum) + '\n')