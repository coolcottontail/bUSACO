fin, fout = open('citystate.in'), open('citystate.out', "w")

N = int(fin.readline())
s = {}


count = 0
for _ in range(N):
    f = fin.readline().split()
    a = f[0][0:2]+ f[1]
    city = f[1] + f[0][0:2]
    if city == a:
        continue
    if city in s:
        count += s[city]
        #print(city, 'found!', count)
    try:
        s[a] += 1
    except:
        s[a] = 1
    #print(s)




fout.write(str(count))