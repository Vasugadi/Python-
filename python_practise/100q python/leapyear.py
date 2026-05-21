num=int(input("enter the number: "))
if(num%100==0 or num%400==0):
    print("leap year")
else:
    print("not a leap year")