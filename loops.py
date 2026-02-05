fruits=['mangoes','bananas','oranges','lemon']

for i in fruits:
    print('jaba')
x=[1,2,3,4,5,]

for i in x:
    print ('alex')

numbers=list(range(101))
print(numbers)
for xb in numbers:
    print(xb)

#range()used to create a list of items

numbers=list(range(10,51))
print(numbers)
for y in numbers:
    if y%2==0:
        print(y)
#display odd number
number=list(range(10,51))
print(numbers)
for num in numbers:
    if num % 2 !=0:
        print(num)

numbers=list(range(10,51))
even_number=[]
for num in numbers:
    if num%2==0:
        even_number.append(num)
print(even_number)

numbers=list(range(10,84))
odd_number=[]
for odd in numbers:
    if odd % 2 !=0:
        odd_number.append(odd)
print(odd_number)

#break used to stop a loop
numbers=list(range(1,1000))
for i in numbers:
    print(i)
    if i==22:
        break
print(i)

numbers=list(range(1,4))
for i in numbers:
    pin=input('enter pin:')
    correct_pin='3909'
    if pin==correct_pin:
        print('yes')
        break
    else:
        print('mbwa wewe')
