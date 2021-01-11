fin, fout = open('whereami.in'), open('whereami.out', 'w')
n = int(fin.readline())
S = fin.readline().strip()

k = 1


def count(val, S):
    return val.find(S) == val.rfind(S)


while k <= n:
    b = True
    for x in range(0, n - k):
        val = S[x:x + k]

        if not count(S, val):
            b = False

    if b:
        break

    k += 1

fout.write(str(k))
