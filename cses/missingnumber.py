n = int(input())
arr = list(map(int, input().split()))

arrofbool = [False] * n
for x in arr:
    arrofbool[x - 1] = True

for x in range(len(arrofbool)):
    if not arrofbool[x]:
        print(x + 1)