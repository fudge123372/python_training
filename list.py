list1=[10,20,30,['alex','jimbo','mailo'],40,50,['cynthia',[100,200,300],'larry','emily'],60,70]
print(list1[3])
print(list1[3][2])
print(list1[6][1][2])

list1=[10,20,30,['alex','mike',[100,200,800,['a','e','i']],'brian'],40,50,['mary',['kelvin','david'],'jane'],60,70]

print(list1[3])
print(list1[3][1])
print(list1[3][2][2])

#display 1
print(list1[3][2][3][2])

#display david
print(list1[6][1][1])

#list operations
#update on item
content=['mon','tue','wed','thur','fri']
content[1]='tuesday'
content [3]='dog'
print (content)
print(content)
content[4]='friday'

print(content)

#list methods
#methods are functions inside a class
# .append(elements)=>used to add elements at the list
content=['mon','tue','wed','thur','fri']
content.append('sat')
content.append('sun')
print(content)

#clear()clears all items on the list
#content.clear()
#print(content)

#copy()fives a shallow copy of the list
x=content.copy()
print(x)

#extend()used to extend a list with another
number=[10,20,30,40]
my_number=[50,60,70,80,90]
number.extend(my_number)
number.append(my_number)
print(number)

#.sort()used to arrange items in a list
x=[10,2,90,70,20,40,23]
x.sort()
print(x)
names=['mike','kim','alex']
names.sort(reverse=True)
print(names)

#.count()used to count the appearance of an item/element
x=[10,1,90,70,20,40,23,100,10,10]
print(x.count(10))

#.reverse()
x.reverse()
print(x)

#len()used to count the number of items in a list
print(len(x))


#.pop()removes the item at the end of the list
names=['mike','kim','alex','davis']
names.pop(1)
print(names)

#remove(item)removes a specific item
names=['mike','kim','chandle','mwikali']
names.remove('mike')
print(names)

#.insert(index,item)adds an item at a specified index
names=['mike','kim','joey','chandler']
names.insert(2,"Noor")
print(names)

#membership we use in operator to check if an item is in a list
names=['mike','kim','alex','mwikali']
print('kelvin' in names)
print('alex'in names)
