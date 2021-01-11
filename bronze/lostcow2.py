import copy

fin, fout = open("lostcow.in"), open("lostcow.out", 'w')

f, b = list(map(int, fin.readline().split()))
d = 0
change = 1
tF = copy.deepcopy(f)
prevF = f

while True:
    f = tF + change
    d += abs(prevF - f)
    change *= -2

    prevF = f
    if tF <= b and f >= b:
        break
    elif tF >= b and f <= b:
        break

fout.write(str(d - abs(f - b)))