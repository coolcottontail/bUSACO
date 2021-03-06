fIn, fOut = open("billboard.in"), open("billboard.out", "w")

x1, y1, x2, y2 = tuple(map(lambda x: int(x), fIn.readline().split()))
x3, y3, x4, y4 = tuple(map(lambda x: int(x), fIn.readline().split()))

tlCorner = False
trCorner = False
brCorner = False
blCorner = False

if y3 <= y1 and x3 <= x1:
    blCorner = True

if y4 >= y2 and x4 >= x2:
    trCorner = True

if x3 <= x1 and y4 >= y2:
    tlCorner = True

if x4 >= x2 and y3 <= y1:
    brCorner = True


cornerCount = len(list(filter(lambda x:x, [blCorner, trCorner, brCorner, tlCorner])))

if blCorner and trCorner:
    fOut.write(str(0))

elif cornerCount == 0 or cornerCount == 1:
    fOut.write(str(abs(x2 - x1) * abs(y2 - y1)))

elif brCorner and trCorner:
    fOut.write(str(abs(y2 - y1) * abs(x2 - x4)))

elif blCorner and tlCorner:
    fOut.write(str(abs(y2 - y1) * abs(x2 - x4)))

elif trCorner and tlCorner:
    fOut.write(str(abs(x2 - x1) * abs(y3 - y1)))

elif brCorner and blCorner:
    fOut.write(str(abs(x2 - x1) * abs(y3 - y1)))

