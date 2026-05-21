#armstrong number is a number in which sum of cubes of the number equals to the number
num=int(input("enter the number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    cube=digit**3
    sum+=cube    
    temp//=10
if(sum==temp):
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
