import copy

fin, fout = open('backforth.in'), open('backforth.out', 'w')
firstBarnBs = list(map(int, fin.readline().split()))
secondBarnBs = list(map(int, fin.readline().split()))

def c(x):
    return x

def odd(bucket, farm1, farm2):
    farm2.append(farm1.pop(farm1.index(bucket)))
    return farm1, farm2

def even(bucket, farm1, farm2):
    farm1.append(farm2.pop(farm2.index(bucket)))
    return farm1, farm2

s = set()
dbg = set()



def tuesday(bucket):
    pass

counting = set()
for day1 in firstBarnBs:
    TsecondBarnBs1 = copy.deepcopy(secondBarnBs)
    TfirstBarnBs1 = copy.deepcopy(firstBarnBs)

    TfirstBarnBs1.remove(day1)
    TsecondBarnBs1.append(day1)

    for day2 in c(TsecondBarnBs1):
        TsecondBarnBs2 = copy.deepcopy(TsecondBarnBs1)
        TfirstBarnBs2 = copy.deepcopy(TfirstBarnBs1)

        TsecondBarnBs2.remove(day2)
        TfirstBarnBs2.append(day2)

        for day3 in c(TfirstBarnBs2):
            TsecondBarnBs3 = copy.deepcopy(TsecondBarnBs2)
            TfirstBarnBs3 = copy.deepcopy(TfirstBarnBs2)

            TfirstBarnBs3.remove(day3)
            TsecondBarnBs3.append(day3)
            for day4 in c(TsecondBarnBs3):
                TsecondBarnBs4 = copy.deepcopy(TsecondBarnBs3)
                TfirstBarnBs4 = copy.deepcopy(TfirstBarnBs3)

                TsecondBarnBs4.remove(day4)
                TfirstBarnBs4.append(day4)

                barn1 = 1000

                barn1 -= day1 # 1000 - 2 = 998
                barn1 += day2 # 998 + 5 = 1003
                barn1 -= day3 # 1003 - 5 = 998
                barn1 += day4 # 998 + 1 = 999

                if barn1 == 1008:
                    print(day1, day2, day3, day4)

                s.add(barn1)
                dbg.add((day1, day2, day3, day4))
            TsecondBarnBs = copy.deepcopy(secondBarnBs)
            TfirstBarnBs = copy.deepcopy(firstBarnBs)

print(s)
n = input()
fout.write(str(len(s)))

""" 
1 1 1 1 1 1 1 1 5 
5 5 5 5 5 5 5 5 5 2 1
"""