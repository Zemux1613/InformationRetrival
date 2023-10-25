import sys


def digit_sum(n):
    if len(n) > 4:
        return -1

    qsum = 0

    for number in n:
        qsum += int(number)

    return qsum


def info(*numbers):
    count = 0
    for i in numbers:
        count += 1
    min = sys.maxsize
    max = 0

    for i in numbers:
        if i > max:
            max = i

        if min > i:
            min = i

    return count, min, max
