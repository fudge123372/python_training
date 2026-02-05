if 20<10:
    print('yes')
else:
    print('no')

#print 50 is greater if 10 is less than 50
if 10>50:
    print('50 is greater')
else:
    print('rubaba')


number=10
#check if number is even
if number%2==0:
    print('even number')

#check if number is odd
if number%2!=1:
    print('odd')

password=input('enter your password')
correct_pass='@amdin123'
if password==correct_pass:
    print('granted')
else:
    print('denied')

age=input('enter your age:')
age=int(age)
#check if age is greater or equal to 30 print adult if age is greater than 18 and less than 30 youth,if age is greater than 10 and less than 18 teenager otherwise print minor
if age >=18:
    print('adult')
elif age>=18 and age<30:
    print('youth')
elif age>=10 and age<18:
    print('teenager')
else:
    print('minor')

marks=input('your marks:')
marks=(int(marks))
#check if marks is greater than 80 print grade A,if marks is 70 to 80 print grade B,if marks is 60 to 69 print grade C,if marks is 50 to 59 print grade D otherwise print grade E
if marks>80:
    print('grade A')
elif marks>=70 and marks<=80:
    print('grade B')
elif marks>=60 and marks<=69:
    print('grade C')
elif marks>=50 and marks <=59:
    print('grade D')
else:
    print('grade E')

temperature=input('enetr tempertaure:')
temperature=float(temperature)
if temperature>30:
    print('the temperature is too high')
elif temperature>15:
    print('normal tempereature')
else:
    print('cold temperature')

