# 49. Write a python program which will accept an integer value and decide weather
# it is magic number of not
# 	GivenNumber==Last Digit ofSquareNumber
# 	5---->25
# 	25--->625

n = int(input('Enter a value: '))
sq = n ** 2
if str(n) in str(sq):
    print('Number is magic Number')
else:
    print('Number is Not a magic number')
