n = 5


for a in range( 2 ** n):
    ans = []
    temp = a
    for i in range(n):
        lsb = temp & 1
        ans = [lsb] + ans
        temp >>= 1
    print(a, ans)