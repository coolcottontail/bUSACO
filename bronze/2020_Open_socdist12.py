import copy

fin, fout = open('socdist.in'), open('socdistout', 'w')

N = int(fin.readline())
stalls = list(fin.readline())
oneList = []

for i in range(len(stalls)):
    if stalls[i] == '1':
        oneList.append(i)

def max_d(l):
    d = []
    maxD = 0
    start = 0

    for i in range(len(l) - 1):
        d.append(l[i + 1] - l[i])
        if l[i + 1] - l[i] > maxD:
            maxD = l[i + 1] - l[i]
            start = l[i]

    return start, start + maxD


def min_d(l):
    d = []
    l.sort()
    print(l)

    for i in range(len(l) - 1):
        d.append(l[i + 1] - l[i])
    return min(d)


start, end = max_d(oneList)
ans = 0

B = copy.deepcopy(oneList)
oneThird = (end - start) // 3
B.append(oneThird + start)
B.append(oneThird * 2 + start)
ans = max(ans, min_d(B))

B = copy.deepcopy(oneList)
if not 0 in B and not N - 1 in B:
    B.append(0)
    B.append(N - 1)
    ans = max(ans, min_d(B))

B = copy.deepcopy(oneList)
if not 0 in B:
    B.append(0)
    B.append((start + end) // 2)

    ans = max(ans, min_d(B))

B = copy.deepcopy(oneList)

if not N - 1 in B:
    B.append(N - 1)
    B.append((start + end) // 2)

    ans = max(ans, min_d(B))

B = copy.deepcopy(oneList)
B.append((start + end) // 2)
start, end = max_d(B)
B.append((start + end) // 2)
ans = max(ans, min_d(B))

print(ans)