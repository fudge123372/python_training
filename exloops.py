numbers=list(range(1,51))
print(numbers)
divisible_seven=[]
for i in numbers:
    if i%7==0:
        divisible_seven.append(i)
print(divisible_seven)

divisible_five=[]
for z in numbers:
    if z% 5==0:
        divisible_five.append(z)
print(divisible_five)

total=0
for i in range(10,41):
    total+=i
print(total)

total=0
count=0

for T in range(10,41):
    total+=T
    count+=1
average=total/count
print(average)

numbers=list(range(10,51))
print(numbers)
odd_numbers=[]
for num in numbers:
    if num % 2 !=0:
        odd_numbers.append(num)
print(odd_numbers)

