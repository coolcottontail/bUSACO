import copy

fIn, fOut = open("homework.in"), open("homework.out", "w")
n = int(fIn.readline())
homework = list(map(int, fIn.readline().split()))

curM = 0
curEat = 0
for eat in range(n - 2):
    temp = copy.deepcopy(homework)
    temp = temp[eat + 1:]
    temp.remove(min(temp))
    n = sum(temp) // len(temp)
    if curM < n:
        curM = n
        curEat = eat

fOut.write(str(eat))