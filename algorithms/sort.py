import random
lst = [x for x in range(1, 11)]
random.shuffle(lst)


def selection_sort(myList):
    for yellow in range(len(myList)):
        minI = yellow
        for blue in range(yellow, len(myList)):
            if myList[minI] > myList[blue]:
                minI = blue

        myList[minI], myList[yellow] = myList[yellow], myList[minI]

    return myList

print(selection_sort(lst))

lst = list(map(int, "6 5 3 1 8 7 2 4".split()))

def insertion_sort(myList):
    for pointer in range(1, len(myList)):
        pointer2 = pointer
        if myList[pointer] > myList[pointer - 1]:
            continue
        while myList[pointer] >= myList[pointer2] and pointer2 > 0:
            myList[pointer2], myList[pointer2 - 1] = myList[pointer2 - 1], myList[pointer2]

            pointer2 -= 1

    print(myList)


insertion_sort(lst)
