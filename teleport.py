fin, fout = open('teleport.in'), open("teleport.out", "w")
a, b, x, y = list(map(int, fin.readline().split()))

if x > y:
    x, y = y, x
if a > b:
    a, b = b, a

pos = [b - a, abs(x - a) + abs(y - b), ]
print(pos)
fout.write(str(min(pos)))