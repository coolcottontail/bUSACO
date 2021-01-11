fin, fout = open('censor.in'), open('censor.out', 'w')
s = fin.readline().strip()
t = fin.readline().strip()
ls = len(s)
lt = len(t)

f = s.find(t)
while f != -1:
    s = s[0:f] + s[f + lt: ls]
    f = s.find(t)

fout.write(s)