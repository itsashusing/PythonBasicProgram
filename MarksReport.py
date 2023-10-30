# 53. Write a python program which will implement the following...
# 	accept Student Number, Student Name and Marks in three subject such as c c++ python
# 	calculate total marks of the student (total mark=cm+cpp+pym)
# 	cal Percentage of marks (percent=total/300*100
# 	Given Grade=Fail Provided Student secured Less than 40 in any one of the subject
# 	Given Grade=Distinction provided total marks ranges between 250 and 300(inclusive)
# 	Given Grade= First provided total marks ranges from 200 and 249 (inclusive)
# 	Given Grade= Second provided total marks ranges form 150 and 199 (inclusive)
# 	Given Grade= Third provided total marks ranges from 120 to 149 (inclusive)
# 	-----------Display the marks Report--------------

# read student number
while True:
    sn = int(input('Enter Student Number between 100-200: '))
    if 100 <= sn <= 200:
        break
    print('\t{} invalid Student Number try again '.format(sn))
# read  student name
sname = input('Enter Student Name:')
# read marks in c cpp python
while True:
    cm = int(input('Enter C language marks: '))
    cppm = int(input('Enter C++ language marks: '))
    pym = int(input('Enter Python Marks: '))
    if 0 <= cm <= 100 and 0 < cppm < 100 and 0 < pym < 100:
        break
    print('Marks should be between 0 to 100')
# calculate Total Marks
tm = cm + cppm + pym
pm = (tm / 300) * 100

if cm < 40 or cppm < 40 or pym < 40:
    Grade = 'Fail'
    print('{} is {} '.format(sname, Grade))
else:
    if 250 <= tm <= 300:
        Grade = 'Distinction'
    elif 200 <= tm <= 249:
        Grade = 'First'
    elif 150 <= tm <= 199:
        Grade = 'Second'
    elif 120 <= tm <= 149:
        Grade = 'Third'
print('{} Marks Report'.format(sname))
print('*' * 50)
print('\tS.N. {}\tStudent Name {} \nMarks Obtain In Subject \n \t C {} | C++ {} | Python {} \n Result is {}'.format(sn,
                                                                                                                    sname,
                                                                                                                    cm,
                                                                                                                    cppm,
                                                                                                                    pym,
                                                                                                                    Grade))
print('*' * 50)
