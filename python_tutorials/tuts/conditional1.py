age=int(input("enter your age: "))
if(age>=18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#elif statements
light=input("enter the light: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("ready")
else:
    print("go")

#elif
a=5
g='m'
if((a==1 or a==2)and g=='m'):
    print("fee is 100")
elif((a==3 or a==4)and g=='f'):
    print("fee is 20")
else:
    print("no fee")

