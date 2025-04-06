# Codewars 7 kyu kata
# Your task is to make a function that can take any non-negative integer 
# as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    s = str(num)
    sorted_s = ''.join(sorted(s, reverse=True))
    return int(sorted_s)
    

print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))