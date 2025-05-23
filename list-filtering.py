# Code Wars 7 kyu kata
# In this kata you will create a function that takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.

# def filter_list(l):
#     new_list = []
#     for i in l:
#         if isinstance(i, str):
#             continue
#         else:
#             new_list.append(i)
#     return(new_list)

def filter_list(l):
    return [i for i in l if not isinstance(i, str)]

print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))