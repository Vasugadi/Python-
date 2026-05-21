print("mini calculator")
num=int(input("enter a number: "))
num2=int(input("enter a number: "))
print("1.addition\n2.subtraction\n3.multiplication\n4.division")

choice=int(input("enter your choice: "))
if choice==1:
    print("sum of two numbers is: ",num+num2)
elif choice==2:
    print("subtraction of two numbers is: ",num-num2)
elif choice==3:
    print("multiplication of two numbers is: ",num*num2)
elif choice==4:
    print("division of two numbers is: ",num/num2)
else:
    print("invalid choice")
    