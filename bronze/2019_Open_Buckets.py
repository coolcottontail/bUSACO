fin, fout = open("buckets.in"), open("buckets.out", "w")
matrix = []

for i in range(10):
    x = fin.readline().strip()
    matrix.append(x)

    if 'B' in x:
        bx = i
        by = x.index('B')

    if 'R' in x:
        rx = i
        ry = x.index('R')

    if 'L' in x:
        lx = i
        ly = x.index('L')

if lx == bx == rx and (ly > by > ry or ly < by < ry or by < ly < ry):
    fout.write(str(abs(by - ly) + abs(bx - lx) - 1))

elif lx == bx == rx:
    fout.write(str(abs(by - ly) - 1 + 2))

elif ly == by == ry and (lx > bx > rx or lx < bx < rx):
    fout.write(str(abs(by - ly) + abs(bx - lx) - 1))
elif ly == by == ry:
    fout.write(str(abs(by - ly) + abs(bx - lx) - 1 + 2))

elif bx == lx:
    fout.write(str(abs(by - ly) - 1))

elif by == ly:
    fout.write(str(abs(bx - lx) - 1))
else:

    fout.write(str(abs(by - ly) + abs(bx - lx) - 1))
