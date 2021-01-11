fin, fout = open('backforth.in'), open('backforth.out', 'w')
firstBarnBs = list(map(int, fin.readline().split()))
secondBarnBs = list(map(int, fin.readline().split()))


s = set()
for day1 in firstBarnBs:

    firstBarnBs.remove(day1)
    secondBarnBs.append(day1)

    for day2 in secondBarnBs:

        secondBarnBs.remove(day2)
        firstBarnBs.append(day2)

        for day3 in firstBarnBs:
            firstBarnBs.remove(day3)
            secondBarnBs.append(day3)

            for day4 in secondBarnBs:
                secondBarnBs.remove(day4)
                firstBarnBs.append(day4)

                barn1 = 1000

                barn1 -= day1
                barn1 += day2
                barn1 -= day3
                barn1 += day4

                s.add(barn1)
                secondBarnBs.append(day4)
                firstBarnBs.remove(day4)
                if (day1, day2, day3, day4) == (1, 5, 2, 6):
                    print(barn1)
            firstBarnBs.append(day3)
            secondBarnBs.remove(day3)

        secondBarnBs.append(day2)
        firstBarnBs.remove(day2)


    firstBarnBs.append(day1)
    secondBarnBs.remove(day1)

fout.write(str(len(s)))
print(s)