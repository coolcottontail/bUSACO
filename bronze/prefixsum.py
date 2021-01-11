a = [0] + [x for x in range(1,5)]
sum = 0

pre = []
for i in range(len(a)):
    sum += a[i]
    pre.append(sum)

print(a)
print(pre)


sum1020 = 0

end = 4
start = 1

for i in range(start,end + 1):
    sum1020 += a[i]

print(sum1020)
b_sum1020 = 0

print(pre[end] - pre[start - 1])