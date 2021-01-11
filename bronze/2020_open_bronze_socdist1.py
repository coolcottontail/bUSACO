fin = open('socdist1.in', 'r')
fout = open('socdist1.out', 'w')

n = int(fin.readline())
d = list(fin.readline())

maxd = []


def lenofzeros(x):


for cow1 in range(len(d) - 1):
    for cow2 in range(len(d) - 1):
        if cow1 != cow2 and (d[cow1] != '1' and d[cow2] != '1'):
            oldD = d
            d[cow1] = '1'
            d[cow2] = '1'
            maxd.append(lenofzeros(d))
            d = oldD
#  print(maxd)


print(lenofzeros('10001001000010'))