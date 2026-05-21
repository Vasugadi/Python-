lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))

sum=0
for num in range(lower,upper+1):
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if sum==num:
        print(num)
    else:
        break
