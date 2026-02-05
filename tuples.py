students=('Alex','Jane','Mike','mary','john')
print(type(students))
print(students)
print(students[3])

#change mary to juma
#convert a tuple to a list using the list()
students=list(students)
print(students)
students[3]='juma'#modify

#convert back to tuple using tuple
students=tuple(students)
print(students)

#add larry between alex and jane
students=list(students)
print(students)
students.insert(1,"Larry")
print(students)
students=tuple(students)
print(students)

days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(len(days))
days=list(days)
print(days)
days[3]='thur'
days=tuple(days)
print(days)
