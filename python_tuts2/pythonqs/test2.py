num=int(input("Enter a number: "))
if num > 0:
    print("Positive number")


if num %2==0:
    print("Even number")
else:
    print("Odd number")

num2=int(input("Enter another number: "))
area=num*num2
print("Area of rectangle:", area)


char=input("Enter a character: ")
list=['a','e','i','o','u']
if char in list:
    print("Vowel")
else:
    print("Consonant")


num3=int(input("enter a number: "))
if(num3 >0 and num3<=9):
    print("Single digit")
elif(num3 >=10000 and num3<=99999):
    print("Five digit")
else:
    print("Invalid number")