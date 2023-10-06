# 19.Write a python program Which will accecpt any digit and print name of the digit by dict method.

d={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
n=int(input('Enter a digit: '))
print('*'*30)
res = d.get(n) if (d.get(n)!=None) else 'Its is a number'
print(res)