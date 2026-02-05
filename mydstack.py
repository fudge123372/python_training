my_ds=[23,'jane',(560),['lesson','maths',{'currency':'kes'}],987,(76,'john')]
print(my_ds)
print(type(my_ds))
print(my_ds[3][2]['currency'])
print(my_ds[2])
print(my_ds[3][1])


number=[1,2,3,4,5]
count=len(number)
if count > 3:
    print(f'list has{count} elements')
    
if (count:=len(number))>3:
    print(f'list has{count}elements')

x=15
y=4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y)
print(x**y)
print(x//y)

x=5
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

x=5
print(1<x<10)
print(1<x and x < 10)

if 20<10:
    print('yes')