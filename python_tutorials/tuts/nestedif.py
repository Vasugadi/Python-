age=int(input("enter the age: "))
if(age>=18):
    if(age>=60):
        print("senior citizen you cant drive")
    else:
        print("adult you can drive")
else:
    print("minor you cant drive")