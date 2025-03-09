'''
#write a program to print "Bring IT Career" ten times using for loop
a="Bring IT Career"
for i in range(10):
    print(a)

#write a program to print 1-20 numbers using while loop
a=1
while(a<=20):
    print(a)
    a=a+1

#write a program to equal and not equal operators
a=int(input("enter value"))
b=int(input("enter value"))
print(a==b)
print(a!=b)

#write a program to print the odd and even numbers
a=[1,2,3,4,5,6,7,8,9,10]
print("even numbers=")
for i in a:
    if i%2==0:
        print(i,end=" ")
print("\nodd numbers=")
for i in a:
    if i%2!=0:
        print(i,end=" ")

#write a program to print largest number among three numbers
a=89
b=98
c=78
if a>b and a>c:
    print("a is largest")
elif b>c:
    print("b is largest")
else:
    print("c is largest")

#write a program to print even numbers in between 10-20 using while
a=10
b=20
print("even numbers between 10 to 20=",end=' ')
while a<=b:
    if a%2==0:
        print("{0}".format(a),end=' ')
    a=a+1
print()

#write a program to print 1-10 using d0_while
a=1
print("print 1-10:",end=' ')
while True:
    print(a,end=" ")
    a=a+1
    if(a>10):
        break
print()

#Armstrong number or not
a=int(input("enter number:"))
s=0
temp=0
temp=a
while temp>0:
    r=temp%10
    s=s+r**3
    temp=temp//10
if a==s:
    print(a,"Armstrong number")
else:
    print(a,"Not Armstrong number")

#write a program to find the numbr=er is prime or not
n=int(input())
fc=0
for i in range(1,n+1):
        if (n%i)==0:
            fc=fc+1
if fc==2:
        print("Prime Number")
else:
    print("not prime")

#write a program to palindrome or not
n=int(input())
temp=n
r=0
while(n>0):
    s=n%10
    r=r*10+s
    n=n//10
if(temp==r):
    print("Palindrome")
else:
    print("Not Palindrome")'''


#Program to check whether a number is EVEN or ODD.
a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print("{0} is Even ".format(a))
else:
    print("{0} is Odd ".format(a)) 