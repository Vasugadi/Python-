while True:
    name =input("entr your name:")
    total=0
    while True:
        print("enter the amount and quatity of items")
        amout=float(input("enter the amount:"))
        quantity=int(input("enter the quantity:"))
        total=total+(amout*quantity)
        repeat=input("do you want to add more items? (yes/no):")
        if repeat == 'no' or repeat == 'No' or repeat == 'NO':
            break
    print("_"*40)
    print("total amount is:",total)
    print("_"*40)
    print("thank you for shopping", name)
    repeat=input("do you want to continue? (yes/no):")
    if (repeat == 'no' or repeat == 'No' or repeat == 'NO'):
        print("thank you for shopping", name)
        break
    