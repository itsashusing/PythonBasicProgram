#Program for accepting any word and Decide weather any  Vowel  present in or not.
a= input('Enter any value: ')
n=a.lower()
res= 'Vowel' if 'a' in n or 'e' in  n or 'i' in n or 'o' in n or 'u' in n else 'Consonent'
print('Given value ({}) is {}'.format(n,res))

