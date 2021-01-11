def permutation(n):
    binLst = [x for x in range(2 ** n)]

    ans = []
    for mNum in binLst:
        currentString = ""

        bitmask = mNum
        for i in range(n):
            currentString += str(bitmask & 1)
            bitmask >>= 1

        ans.append(currentString)

    return ans

print(permutation(3))
print([bin(x).replace('0b', '') for x in range(2**3)])