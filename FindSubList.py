# 32. Write a Python program to check whether a list contains a sublist.
# 33. Write a Python program to generate all sublist of a list.

lst = [7, 1, 2, 3, 4, 5, 1, 2, 6]
sub_lst = [1, 2]
for i in range(len(lst)):
    if lst[i:i + 2] == sub_lst:
        print(sub_lst)
