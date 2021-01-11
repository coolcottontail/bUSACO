x = int(input())

for n in range(1, x + 1):
    print((n*n*(n*n-1))//2 - 4*(n - 1)*(n - 2))