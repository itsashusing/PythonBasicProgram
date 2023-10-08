# 20. Write a python program which will implement the following problem ---
# accept employ name , dsg, basic salary
# if basicsal>= 10000 then give
#   	da= 20% basicsal
# 	    Ta= 15% basicsal
#   	Hra= 16% basicsal
#   	Ma=2% basicsal
# 	    cca=1% basicsal
# Deduction
# 	    lic=2% basicsal
#   	gpf=1.5% basicsal
# => if 0<basic<10000 then give
# 	    da= 10% basicsal
# 	    Ta= 7.5% basicsal
#   	Hra= 8% basicsal
#   	Ma=1.2% basicsal
#   	cca=0.5% basicsal
# Deduction
#   	lic=2% basicsal
# 	    gpf=1.5% basicsal
# => Calculate Netsal:   (Netsal= basicsal+Da+Ta+hra+Ma+cca)-(lic+gpf)
name = input('Enter Name of the employ: ')
dsg = input('Enter dsg of the employ: ')
basic_sal = int(input('Enter Salary of the employ: '))
print('*' * 80)
# code
if (basic_sal) >= 10000:
    da = (20 / 100) * basic_sal
    Ta = (15 / 100) * basic_sal
    Hra = (16 / 100) * basic_sal
    Ma = (2 / 100) * basic_sal
    cca = (1 / 100) * basic_sal
    lic = (2 / 100) * basic_sal
    gpf = (1.5 / 100) * basic_sal
    Net_sal = (basic_sal + da + Ta + Hra + Ma + cca) - (lic + gpf)
elif 0 < (basic_sal) < 10000:
    da = (10 / 100) * basic_sal
    Ta = (7.5 / 100) * basic_sal
    Hra = (8 / 100) * basic_sal
    Ma = (1.2 / 100) * basic_sal
    cca = (0.5 / 100) * basic_sal
    lic = (2 / 100) * basic_sal
    gpf = (1.5 / 100) * basic_sal
    Net_sal = (basic_sal + da + Ta + Hra + Ma + cca) - (lic + gpf)
else:
    print('Enter valid salary OR salary should be greater than 0 ')
print('Name: {}, DSG: {}, Basic_Salary: {} & Net_Salary is  {} '.format(name, dsg, basic_sal, Net_sal))
print('*' * 80)
