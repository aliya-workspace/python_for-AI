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

#3)Logical operators:
# these are between compound expression jis me 2 ya 2 sy ziyada expressions ko combine kiya jata hai
#Types of Logical opertaors:
#AND: agar sari expressin ture ho to result ture ho ga (exp1 and ep2 ---> ture)
#OR: agar 2 me sy aik bhi expression ture ho to result ture ho ga (exp1 or exp2---> ture)
#Not: opposite answer dey ga yani input ko reverse kar ky output dy ga(  ture--->False or agar false---->ture)

#Practice program:(logical opertaor:)
#1:
val1= True
val2=False
print("And opertaor is: ",val1 and val2)
print("OR opertaor is: ",val1 or val2)
print("NOt opertaor is: ",not val2)

#2:
a=5
b=10
print("And opertaor ",(a>=b) and (a<b))
print("OR opertaor ",(a>=b) or (a<b))
print("NOT opertaor ",not(a>=b))
 
#4) Assignment opertaor: (+=,-=,*=,/=,%=,**=)
#1): this is not advance method
a=10
a=a*20
print("value of a: " ,a)
#use of assignment operator:
a=10
a*=10
b-=10
print("value of a: " ,a)
print("value of a: " ,b)



 






#some are constants like py