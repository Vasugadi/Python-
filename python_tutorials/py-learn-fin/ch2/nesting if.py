#nested if
age_of_raayan=int(input("enter your age"))
if age_of_raayan>18:
    if age_of_raayan>70:
        print("you cant drive")
    else:
        print("you can drive")
else:
    print("you cant drive")