# Code Wars 7 kyu kata
# In this little assignment you are given a string of space separated numbers, 
# and have to return the highest and lowest number.
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, 
# and highest number is first.

def high_and_low(numbers):
    # Split the string into a list
    number_list = numbers.split()
    int_number_list = []
    for i in number_list:
        int_number_list.append(int(i))    
    sorted_list = sorted(int_number_list, reverse = True)
    highest = sorted_list[0]
    lowest = sorted_list[-1]

    return(f"{highest} {lowest}")

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low('1 2 3'))