fin, fout = open('crosswords.in'), open('crosswords.out', 'w')

N, M = list(map(int, fin.readline().split()))

graph = []
for x in range(N):
    graph.append(fin.readline().strip())
print(graph)
for i in range(N):
    for j in range(M):
        print(i, j)
        if graph[i][j] == "#":
            continue
        # Check
        good = False
        try:
            if i - 1 > 0:
                raise KeyError
            if graph[i + 1][j] == "#":
                pass

            elif graph[i + 2][j] == "#":
                pass
            else:
                good = True
        except:
            pass

        # Check
        try:
            if j + 1 < N and graph[i][j + 1] == "#":
                pass
            elif j + 2 < N and graph[i][j + 2] == "#":
                    pass
            else:
                good = True
        except:
            pass

        if good:
            fout.write(str(i + 1) + ' ' + str(j + 1) + '\n')