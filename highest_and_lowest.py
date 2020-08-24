'''
    Example:

    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"
'''


def high_and_low(numbers):
    srt = sorted([int(x) for x in numbers.split()])[::-1]
    return f"{srt[0]} {srt[len(srt) - 1]}"

