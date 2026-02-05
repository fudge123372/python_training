def square_number(num):
    print(num ** 2)
square_number(4)

def cube_number(num):
    print(num**3)
cube_number(3)

def add_numbers(a,b):
    print(a,b)

add_numbers(18,45)

def check_password(x):
    correct_password='secret123'
    if x == correct_password:
        print("Access granted")
    else:
        print("Access denied")
real_password=input('enter passwprd:')
print(real_password)
check_password(real_password)

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32)*5/9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
    return"hello froom a function"
message=get_greeting()
print(message)

def get_greeting():
    return'hello from a funtion'
print(get_greeting())
