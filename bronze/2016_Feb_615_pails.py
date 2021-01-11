fin, fout = open('pails.in'), open('pails.out', 'w')
x, y, m = tuple(map(int, fin.readline().split()))
ma = m
for ycount in range(m//y+1):
    ma = min(ma, (m - ycount * y) % x)
fout.write(str(m - ma))