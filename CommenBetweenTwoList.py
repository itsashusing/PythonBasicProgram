# 11. Write a Python function that takes two lists and returns True
# if they have at least one common member.
def listCommon(x,y):
    res=False
    for i in x:
        for j in y:
            if i == j:
                res=True
    return res


l1=[1,2,3,4,5,8]
l2=[1,5,6,3,2]
a=listCommon(l1,l2)
print(a)