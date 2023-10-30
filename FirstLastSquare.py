# 16. Write a Python program to generate and
# print a list of first and last 5 elements
# where the values are square of numbers
# between 1 and 30 (both included).
l = list()
for i in range(1, 31):
    if i in range(1, 6) or i in range(25, 31):
        l.append(i)
print('list of squares ', l)
