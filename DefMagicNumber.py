# 59. Write a python program which will decide weather given number is
# magic or not using function. 5-->25  25-->625

def CheckMagic(x):
    s = str(x ** 2)
    R = f'\n{x} is Not a magic Number----square of {x} is {s}'
    y = s[:-len(str(x)) - 1:-1]
    y = y[::-1]
    if int(y) == x:
        R = f'\n{x} is a magic Number----square of {x} is {s}'
    return R


r = CheckMagic(25)
p = CheckMagic(5)
q = CheckMagic(125)
print(p, q, r)
