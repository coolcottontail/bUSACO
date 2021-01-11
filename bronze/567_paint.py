fin, fout = open('paint.in'), open('paint.out', 'w')
l1 = list(map(int, fin.readline().split()))
l2 = list(map(int, fin.readline().split()))
l = l1 + l2


if l1[0] < l2[1] + 1 and l2[0] >= l1[1] + 1:
    fout.write(str((l1[1] - l1[0]) + (l2[1] - l2[0])))

elif l1[0] >= l2[1] + 1 and l2[0] < l1[1] + 1:
    fout.write(str((l1[1] - l1[0]) + (l2[1] - l2[0])))

else:
    fout.write(str(max(l) - min(l)))
