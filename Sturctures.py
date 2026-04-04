#Control Structures:
#control structures give flow of program control or order of execution called as control structures.
#Types:
#Sequential Statements
#Conditional Statements
#Iterative Statements

#Sequential Statements:
#all statemnets execute in sequence
a=5
b=10
c=a+b
c=a*b
c=a/b
c=a-b
print(a*b)
d=15
e=a*d
print(e)
#program will execute in sequence each step will be execute and display

#Conditional Statements:
#jin satatments me conditions ati hain.. jesy jab students ky marks likhny ho...50 sy uper wo pass hain or jo 50 below wo fail hain same like odd even number ,postive negetive etc statemnats
#syntax:
#if condition:
#  statment
#else:
#  statement
#Write a program in which take any number and show that number is even or odd
#number=20
#if (number%2==0):
#    print("even")
#else:
 #   print("odd")

#by taking number from user
#number=(input("Enter number: "))
#if (number%2==0):
 #   print("even")
#else:
#    print("odd")

#positive netgive
#number=(input("Enter number: "))
#if (number>=0):
#    print("positive")
#else:
#   print("negative")

#multiple if else statments
marks=(input("Enter marks of students: "))
if marks>=80:
    print("Grade:A")
elif marks>=70:
    print("Grade:B")
elif marks>=60:
    print("Grade:C")
elif marks>=50:
    print("Grade:D")
elif marks>=40:
    print("Grade:E")
else:
    print("Fail")



