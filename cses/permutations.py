n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print('NO SOLUTION')
elif n == 4:
    print('2 4 1 3')
else:
    if n % 2 == 1:
        for x in range(n -1, 0, -2):
            print(x, end=' ')
        for x in range(n, -1, -2):
            print(x, end=' ')
    else:
        for x in range(n, 0, -2):
            print(x, end=' ')
        for x in range(n - 1, -1, -2):
            print(x, end=' ')