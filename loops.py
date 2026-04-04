#loops:
#repeitition or iteration aik ciz ko baar bar execute  karna hai means same pice of block ko multiple type print karwana 

#Types of Loop
#for and while

#1) for loop:
#for and while have same working but for loop me pehley sy hi size ka pat hota hai fixed size iterations hoty hain condition already khnown hoti hain pehley sy pata hota hai ky ye kam itni dafa karna hai is purpose ky liye for loop use hoti 
#Example : display number 1 to 10 or printa satatment 20 times
#(starting value, second value jitna chalana hai usey,increment karna hai )
#for i in range(1,11,1):
    #print(i)

#another program finding even numbers 1 to 50
#for i in range(1,50,1):
    #if i%2==0:
     #print(i)

#printing odd numbers 
#for i in range(1,50,1):
   #if i%2!=0:
     #print(i)


#passing one paramter
#for i in range(5):
    #print(i)
#its mean its last limit or intial value by defalt zero set ki jati hai



#2) while loop jab hamey condition unknown hoti hai we are based on condition means jab tak condition true hai tab tak program chalta rehy ga jesy hi false hoi program end

#i=1
#while(i<=20):
    #print(i)
    #i=i+1
#take a number from user and display number 1 to n .... n user sy lyna hai 

#n = int(input("Enter number: "))
#i=1
#while(i<=n):
    #print(i)
    #i=i+1

#display sum from 1 to n 
n = int(input("Enter number: "))
i=1
sum=0
while(i<=n):
    sum=sum+1
    i=i+1
    print("sum is: ",sum)