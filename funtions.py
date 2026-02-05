#calculating the are of a circle
def area_circle():
    area=pie*radius*radius
    print(area)



print('hi')
print('hello')

def area_triangle(base,height):
    area=0.5*base*height
    print(area)

area_triangle(10,20)
area_triangle(7,10)

def check_password(x):
    correct_password='zuri'
    if x==correct_password:
        print('access granted')
    else:
        print('mbwa wewe')

user_password=input('enter password: ')
print(user_password)
check_password(user_password)

def hello(name):
    print('hello {name}')

hello('larry')

#Take three inputs from a user, separately. Print the largest of the numbers.
 #Hint: Determine what type of data is taken in as input

def largest_number(a,b,c):
    if a>b and a>c:
        print(f'{a} is the largest')
    elif  b>a and b>c:
        print(f'{b}is the largest')
    else:
        print(f'{c}is the largest')

num1=input('enter first name:')
num2=input('enter second name:')
num3=input('enter last name:')
num1=int(num1)
num2=int(num2)
num3=int(num3)
largest_number(num1,num2,num3)




