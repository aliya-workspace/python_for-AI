#type casting mean aik data type ko dosri data type me convert kar dain kisi bhi variable ki value ko aik type sy dosti type sy (float to int or int to float)
#Two types of converiosn:
#1) Implicit casting        2)Explicit casting

#IMplicit casting: 
#Internal: Automatically means system do it own
#it convert smaller data type to larger data type (int(2 byte) to float(4 bytes))
"""a=2
b=5.7
sum=a+b
print(sum)
print ("sum: ",sum)
"""

#Excplicit casting:
#External: means outside programmer will convert data type its a manual converison,forcefull conversion
#larger to smaller data types 

"""a="10" #string
b=5 #int
add=a+b
print(add)
"""
#we can't add or multiply string so now we will forcefully convert it.
"""c=int("10")
d=5
sum= c+d
print("sum is: ",sum)"""

"""
a="10"
b=5
sum=int(a)+b
print(sum)
"""

a = 10
b = 2.5
c = a * b

print(c)
print(type(c))