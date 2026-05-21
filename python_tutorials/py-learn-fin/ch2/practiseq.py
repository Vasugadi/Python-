#wap to print a number is  odd or even
val_to_check=int(input("enter a number to check:"))
if val_to_check%2==0:
    print("even")
else:
    print("odd")

#wap to print greatest number among three numbers
val1=int(input("enter first number:"))
val2=int(input("enter second number:"))
val3=int(input("enter third number:"))
if val1>val2 and val1>val3:
    print("val1 is greatest")
elif val2>val1 and val2>val3:
    print("val2 is greatest")
else:
    print("val3 is greatest")

#wap to print whether a number is multiple of 7
num=int(input("enter a number to check:"))
if num%7==0:
    print("multiple of 7")
else:
    print("not a multiple of 7")