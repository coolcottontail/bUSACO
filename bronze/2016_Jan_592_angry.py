fIn, fOut = open("angry.in"), open("angry.out", "w")

N = int(fIn.readline())
cows = sorted([int(fIn.readline()) for _ in range(N)])


def input_is_x(x, direction):
    count = 0
    t = 1
    for i in range(x + 1, N - 1):
        if abs(cows[i] - cows[i - 1]) < t + 1:
            count += 1
        else:
            t += 1
            break


    return count

for i in range(N):
    print(i, input_is_x(i, 1), input_is_x(i, -1), cows[i])
