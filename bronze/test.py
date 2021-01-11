import os

fin, fout = open('planting.in'), open('planting.out', 'w')

l = fin.readline()
#fout.write(l)

cwd = os.getcwd()
fout.write(cwd + '\n')

for filename in os.listdir("/bin"):
    fout.write(filename + "\n")

#with open("/etc/issue", 'r') as fin1:
#    fout.write(fin1.read() + '\n')


#fout.write('helloworld')