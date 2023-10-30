# 5. Write a Python program to count the number of strings where the
# string length is 2 or more and
# the first and last character are  same from a given list of strings.
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2
n= int(input('Enter How many words you want to enter: '))
l=[]
s=1
p=[]
for i in range(1,n+1):
    val= input('Enter {} value: '.format(i))
    l.append(val)
else:
    for word in l: # aba
        if len(word) >2:
            if word[0] == word[len(word)-1]:
                p.append(word)
    else:
        print('~'*50)
        print('\tWord which first and last character are same {}'.format(p))
        print('\t'+str(len(p)))
        print('~'*50)
