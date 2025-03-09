'''#write a function for arithmetic operators
a=int(input("enter a value"))
b=int(input("enter b value"))
print("sum=",a+b)
print("diff=",a-b)
print("mul=",a*b)
print("div=",a/b)


#write a method for increment and decrement operators
a=5
a+=1
a=a+1
print("the value of a=",a)
print("INCREMENTED FOR LOOP")
for i in range(0,5):
    print(i)
print("\nDECREMENTED FOR LOOP")
for i in range(4,-1,-1):
    print(i)

#write a program to find the two numbers are equal or not
a=int(input("enter a value"))
b=int(input("enter b value"))
if a==b:
    print("both are equal")
else:
    print("both are not equal""")

#write a program for relational operators
a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)'''

#write a program for smaller and larger number
a=input("enter 1st value")
b=input("enter 2nd value")
if a<b:
    print("a is smaller")
else:
    print("a is greater")