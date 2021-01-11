import itertools

n = int(input())
permute = list(map(list, list(itertools.permutations(list(map(str, list(range(1, n + 1)))), n))))

se = set()

mysum = sum(list(range(1, n + 1)))

print(permute)

for x in permute:
    for s in range(1, n):
         if sum(list(map(int, x[:s]))) << 1 == mysum:
             print(x[:s], s, x)

