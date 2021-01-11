n = int(input())
oldarr = list(map(int, input().split()))
newarr = oldarr

count = 0
for z in range(n - 1):
    first = oldarr[z]
    second = oldarr[z + 1]
    if first > second:

        count += first - second
        oldarr[z + 1] = second + (first - second)
print(count)