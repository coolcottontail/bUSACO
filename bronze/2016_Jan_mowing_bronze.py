fin, fout = open('mowing.in'), open('mowing.out', 'w')
n = int(fin.readline())

x = 1
y = 1
time = 0
ans = 1e9

matrix = {}


for _ in range(n):
    f = fin.readline().split()


    for _ in range(int(f[1])):
        try:
            ans = min(ans, time - matrix[(x,y)])
            matrix[(x, y)] = time

        except:
            matrix[(x, y)] = time
        time += 1


        if f[0] == 'N':
            y += 1
        elif f[0] == 'S':
            y -= 1
        elif f[0] == 'W':
            x -= 1
        else:
            x += 1

fout.write(str(ans))
