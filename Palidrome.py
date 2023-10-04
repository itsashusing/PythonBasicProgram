#Program accepting any value and decide whether the given value is palindrome or not
n= input('Enter any value: ')
res = 'Palidrome' if n.lower() == n[::-1].lower() else 'not palidrome'
print('*' * 30)
print('The Given value ({}) is {}'.format(n,res))
