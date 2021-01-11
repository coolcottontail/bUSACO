fin, fout = open('cowsignal.in'), open('cowsignal.out', 'w')

m, n, k = tuple(map(int, fin.readline().split()))
s = []
for x in range(m):
    s.append(fin.readline().strip())

for line in s:
    out = ''
    for letter in line:
        out += letter * k
    fout.write((out + '\n') * k)