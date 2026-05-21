def factor(num):
    for i in range(1,num):
        if num%i==0:
            print(i)
num=int(input("enter a number: "))
factor(num)