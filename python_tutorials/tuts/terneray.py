food=input("enter the food u like: ")
eat="yes" if(food=="chicken" or food =="mutton") else "no"
print(eat)

#ternary operator is used to replace if else statement
#type 2
food ="biryani"
print("yes i want ")if(food=="biryani")else print("no i don't want")

#clever if (false,true)[condition]
age=int(input("enter your age: "))
drive=("yes u can ","no")[age<=18]
print(drive)

sal=int(input("enter your salary: "))
tax=sal*(0.1,0.2)[sal>50000]
print(tax)