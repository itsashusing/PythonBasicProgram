# 17. Write a Python program to generate and
# print a list except for the first 5 elements,
# where the values are square of numbers
# between 1 and 30 (both included).
lst = list()
for i in range(1, 31):
    if i < 6:
        continue
    else:
        lst.append(i ** 2)
print(lst)
