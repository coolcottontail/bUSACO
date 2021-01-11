fin, fout = open('photo.in'), open('photo.out', 'w')

n = int(fin.readline())
b = list(map(int, fin.readline().split()))

a = []
count = 0

for a1 in range(1, n-1):

    off = False

    a = []
    a.append(a1)
    a.append(b[0] - a1)

    cur = b[0] - a1

    for x in range(1, n-1):
        cur = b[x] - cur

        if cur not in a and cur > 0 and cur <= n:
            a += [cur]
        else:
            off = True
            break

    if not off:
        break


fout.write(' '.join(list(map(str, a))))