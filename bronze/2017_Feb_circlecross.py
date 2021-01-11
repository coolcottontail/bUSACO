fin, fout = open('circlecross.in'), open('circlecross.out', 'w')
s = fin.readline()
cowD = {}
for i in range(52):
    try:
        cowD[s[i]].append(i)

    except:
        cowD[s[i]] = [i]

count = 0
for a in cowD:
    for b in cowD:
        if a != b and (cowD[a][0] < cowD[b][0] < cowD[a][1] and cowD[a][1] < cowD[b][1]):
            count += 1

fout.write(str(count))
