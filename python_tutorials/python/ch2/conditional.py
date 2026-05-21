#conditional statement have some conditions and based on that we can do some operations

# if else 
# if (condtion):
#     #do something
# else:
#     do something

# if else if else

# if (condtion):
#     #do something
# elif (condtion):
#     #do something
# else:
#     do something

# age=int(input("entr your age: "))
# if(age>18):
#     print("you are adult")
# else:
#     print("you are not adult")


light=input("enter the color of the light: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("wait")
else:
    print("go")
    


marks=int(input("enter the marks: "))
if(marks>=90 and marks<=100):
    print("A grade")
elif(marks>=80 and marks<90):
    print("B grade")
elif(marks>=70 and marks<80):
    print("C grade")
else:
    print("you got a job")

A=5 
G="m"
if((A==1 or A==2)and G=="m"):
    print("your fee is 100")
elif(A==3 or A==4 or G=="f"):
    print("your fee is 200")
else:
    print("your fee is 0")

#ternery operator
# var=<val1>if<condition>else<val2>

food=input("enter the food you wanted  to eat: ")
print("yes") if(food=='biryani' or food =='chicken') else print("no willing to eat")

food=input("enter food: ")
eat="yes" if(food=='cake') else "n0"
print(eat)



# clever if 
# var=[false,true] [condtition]
age=int(input("enter the value: "))
vote=("yes","no") [age>=18]
print(vote)

sal=float(input("enter the vlaue: "))
tax=sal*(0.1,0.2)[sal>=5000]
print(tax)