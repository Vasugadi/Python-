start=int(input("enter the starting number: "))
end=int(input("enter the ending number: "))
skip=int(input("enter the number to skip: "))
for i in range(start,end):
    if i==skip:
        continue
    else:
        print(i)