#Codewars 7 kyu kata
# A square of squares
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
# Given an integral number, 
# determine if it's a square number:

import math

def is_square(n):    
    if n < 0:
        return False
    elif n == 0:
        return True
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n
 
    return False

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))