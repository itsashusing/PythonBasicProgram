# 54. Write a python program which will accept list of words and print the highest length word.
print('Enter @ to stop: ')
lst=list()
while True:
    ch= input('Enter any word: ')
    if ch == '@':
        break
    else:
        lst.append(ch)
print(lst)
print('*'*50)
d={}
for word in lst:
    d[word]=len(word)
else:
    val= d.values()
    ml= max(val)
    for k,v in d.items():
        if ml==v:
            print(k)