fin, fout = open('crosswords.in'), open('crosswords.out', 'w')

rowCount, colCount = list(map(int, fin.readline().split()))

graph = []
for x in range(rowCount):
    graph.append(fin.readline().strip())
print(graph)
for i in range(rowCount):
    for j in range(colCount):
        if graph[i][j] == "#":
            continue

        good = False
        # Check
        if i + 2 < rowCount and not (graph[i + 1][j] == "#") and not (graph[i + 1][j] == "#"):
            good = True

        # Check
        print(graph[i][j], i, j)
        if j + 2 < colCount:
            if [j + 1][i] == "." and graph[j + 1][i] == ".":
                good = True


        if good:
            fout.write(str(i + 1) + ' ' + str(j + 1) + '\n')