# 43. Write a python program which will accept list of words any print those words
# which contains atleast one vowel.
print('enter (stop) for stop the program')
lst = []
while True:
    ch = input('Enter a word: ').lower()
    if ch== 'stop':
        break
    lst.append(ch)
print('Your List is {}'.format(lst))
vl = []
cl = []
for i in lst:
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
        vl.append(i)
    else:
        cl.append(i)
print('*'*50)
print('\n Vowel list--->{} \n Consonant List----> {} '.format(vl, cl))
