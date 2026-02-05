#create a dictionary
my_dict={
    'name':'Larry Mokua',
    'city':'Nairobi',
    'age':22

}
print(my_dict)
print(type(my_dict))

#displaying values
print(my_dict['city'])

#age
print(my_dict['age'])

#name
print(my_dict['name'])

#adding items
my_dict['operations']='software developer'
my_dict['skills']=['building','running','jumping','video editing']
print(my_dict)

#add contact

#update items
my_dict['city']='kakamega'
print(my_dict)
my_dict['age']='23'
print(my_dict)

#remove specific items
my_dict.pop('age') 
print(my_dict)
my_dict.popitem()# removes the last item on the list
print(my_dict)

#.values()used to display a list of only values in the dictionary
print(my_dict.values())

#.keys()used to display a list of only keys in the dict
print(my_dict.keys())

#.itens()used to display the list of all items in tuples
print(my_dict.items())

#.get(key)used to get values in dict
print(my_dict.get('city'))