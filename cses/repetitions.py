n = input()

if len(n) == 1:
    print(1)

else:
    newN = ''

    prev = ''

    for x in range(0, len(n) - 1,2 ):
        if prev != n[x]:
            newN += ' '
        newN += n[x]
        if n[x] != n[x + 1]:
            newN += ' '
        newN += n[x + 1]
        prev = n[x + 1]
    newN = newN.split()

    m = 0

    for x in newN:
        m = max(len(x), m)

    print(m)