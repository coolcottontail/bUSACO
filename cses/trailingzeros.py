
def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
factorial = fact(int(input()))



print(len(str(ffactorial)) - len(str(factorial).rstrip('0')))