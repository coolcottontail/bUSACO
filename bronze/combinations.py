l = [x for x in range(1, 11)]

def permutations(n):
    answer = []
    for a in range(2 ** n):
        ans = []
        temp = a
        for i in range(n):
            lsb = temp & 1
            ans = [lsb] + ans
            temp >>= 1
        answer.append(ans)
    return answer

def combinations(l):
    ans = []
    for o in permutations(len(l)):
        curC = []
        for i in range(len(l)):
            if o[i] == 1:
                curC.append(l[i])
        ans.append(curC)
    return sorted(ans, key=lambda x: (len(x), x))


for x in combinations(l):
    print(x)