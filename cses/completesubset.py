def subsets(l):
    le = len(l)
    out = 0
    for x in range(0, 2**le):
        binary = bin(x)[2::]
        while len(binary) != le:
            binary += '0'

        thel = []
        for f in range(le):
            if binary[f] == '1':
                thel += [l[f]]
                print(f)
        print(thel, x)

myList = [x for x in range(1, 4)]
subsets(myList)