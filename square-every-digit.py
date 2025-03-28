# Code Wars 7 kyu kata
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out,
# because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625
# because 7**2 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.

def square_digits(num):
    squared_digits = ''
    s = str(num)
    for c in s:
        n = int(c)**2
        new_c = str(n)
        squared_digits = squared_digits + new_c
    return int(squared_digits)

print(square_digits(9119))
print(square_digits(0))