fin, fout = open('crossroad.in'), open('crossroad.out', 'w')

n = int(fin.readline())

sightings = []

dic = {}
for x in range(n):
    sightings.append( fin.readline().split())


for cow, val in sightings:
    try:
        dic[cow] += val
    except:
        dic[cow] = val


def find(x):
    count = 0
    for f in range(len(x) - 1):
        if x[f] + x[f + 1] == '01' or x[f] + x[f + 1] == '10':
            count += 1

    return count


count = 0
for k in dic:
    val = dic[k]
    count += find(val)


fout.write(str(count))