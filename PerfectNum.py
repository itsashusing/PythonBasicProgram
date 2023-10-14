# 48.Write a python program which will accept any numerical value and
# decide weather it is a perfect number or not.
# 	perfect number > whose Factors sum == Give Number
# 	case : Give Number : 6
# 	Sum of Fact of 6 = 1+2+3 so 6 is perfect number
# 	case: Given number : 8
# 	Sum of fact is = 1+2+4 so 8 is not perfect number
# 	case: 28
# 	fact 1+2+4+7+14->28 so 28 is a perfect number

n = int(input('Enter a value: '))
fs = 0
if n <= 0:
    print('Invalid Input')
else:
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            print("\t {}".format(i))
            fs = fs + i
    else:
        if fs == n:
            print('Number is Perfect')
        else:
            print('Number is not Perfect')
