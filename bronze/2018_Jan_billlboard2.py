fIn, fOut = open("billboard.in"), open("billboard.out", "w")

x1, y1, x2, y2 = tuple(map(lambda x: int(x), fIn.readline().split()))
x3, y3, x4, y4 = tuple(map(lambda x: int(x), fIn.readline().split()))

if y3 == y1 and y4 == y2 and x3 != x1 and x4 != x2:
    fOut.write(str(()))
# Case 1: The cow feed poster covers up the other poster
if x3 >= x1 and y3 >= y1 and x4 <= x2 and y4 <= y2:
    fOut.write(str(0))
elif x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2:
    fOut.write(str(0))
else:
    # Case 2: Case 1 doesn't work
    fOut.write(str((abs(x2 - x1) * abs(y2 - y1))))


