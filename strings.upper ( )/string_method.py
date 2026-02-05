myname="Larry Agustino"
myname = myname.upper()
print(myname)
myname=myname.lower()
print(myname)

x="  python programming"
print(x)
x=x.strip()
print (x)

# clean full_name="  lARry AgUSTino    " to  ' larry agustino'
full_name = "  lARry  Agustino"
full_name=full_name.strip()
full_name=full_name.lower()

# replace =>
myname = "Larry Agustino"
print(myname)
myname=myname.replace('Larry','Jones')
print(myname)
# clean text ="  python programming    "   to "JAVA PROGRAMMING"
text = "  python programming"