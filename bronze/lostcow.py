fin, fout = open('lostcow.in'), open('lostcow.out', 'w')

x, y = tuple(map( int, fin .readline() .split()))

d = 0.5
z = x


if y > x:
    while z - x < y - x:
        d *= -2
        z = x + d
else:
    while x - z < x - y:
        z *= 2

print(z,  y-z)