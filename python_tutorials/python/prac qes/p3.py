#wap to check if a number entered by the user is even or odd

num=int(input("enter a number: "))
rem=num%2
if rem==0:
    print("even")
else:
    print("odd")
print("end of program")

# wap to check if a number is greater among 3 numbers
a=int(input("enter value of a:"))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
if(a>b and a>c):
    print("a is greater")
elif(b>c):
    print("b is greater")
else:   
    print("c is greater")


#wap to checj if a number is multiple of 7 or not
num=int(input("enter a number: "))
if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")