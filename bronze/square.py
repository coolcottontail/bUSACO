fin, fout = open('square.in'), open('square.out', 'w')


x1, y1, x2, y2 = tuple(map(int, fin.readline().split()))
x3, y3, x4, y4 = tuple(map(int, fin.readline().split()))

xmin = min(x1, x2, x3, x4)
xmax = max(x1, x2, x3, x4)

ymin = min(y1, y2, y3, y4)
ymax = max(y1, y2, y3, y4)

fout.write(str(max(xmax - xmin, ymax - ymin) ** 2))