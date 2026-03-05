#variables(value changes in variables in memory):
#variable is a name given to a memory location in the program.(we don't need data type in python for variables.)
name="Aliyakhanam" #string
age=19          #integer
number=10.5        #float

print("My name is: ",name)
print("My age is: ",age)
print("My name is: ",number)
print(number)

#finding data type of variables we use 
#Type function:
print(type(name))
print(type(age))
print(type(number))

print("Type of name is:",type(name))

#program
a=10
b=20
print("before swaping: ",a,b)
temp=a
a=b
b=temp
print("after swaping:",a,b)


#keywords: 
#keywords are reversed words that have pre-defined and have some special meaning.There are 33 keywords in python.For example: for,while,if,else,true,false,or,and

#(having variables rules)
#1.variable can't start with digit
#2.variable length can be any
#3. capital letter underscore small we can start variable

#Operators:(special type of symbols we use them to perform any task)
#e.g a+b*c-5 (3 opperendse.g a(that contain  value),and signs are operators that perform operations on opperends)
#Types of operators:
#1) Arithmetic operators(+,-,*,/,%,**)
a=20
b=10
print("Addition",a+b)
print(a-b)
print(a%b)
print(a*b)
print(a**b)


c=a*b
c=a-b
c=a/b
print(c)

#2) Relational operators: Also comparison operator 
#e.g ==,!=,<,>,<=,>=
x=100
y=200
print(x<y)



#some are constants like py