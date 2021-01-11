import random

def usaco(x, n):
    n = open(n + '.py', 'w')
    ah = random.choice(['fIn, fOut = open("' + x + '.in"), open("' + x + '.out", "w")', 'fin, fout = open("' + x + '.in"), open("' + x + '.out", "w")'])
    n.write(ah)
    return ah

def add(x, n, s):
    file = open(x + '.py', 'a')
    file.write('\n' + s)

def start_usaco():
    file = input("File Name (Without .py): ")
    file2 = input('2: ')
    afile = usaco(file, file2)

    if afile.find('fIn') != -1:
        afile == 'fIn'
    else:
        afile == 'fin'

    firstLine = input('One-Line Int for i, One-Line str for s, Multi-int Line for mi, Nothing is nothing: ')

    if firstLine == 'i':
        add(file2, 'N = int(' + afile + '.readline())')

if __name__ == '__main__':
    start_usaco()