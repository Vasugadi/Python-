def sum(a,b):
    sum=a+b
    print(sum)
sum(10,20) #30
sum(20,30) #50


def greet():
    print("hello")
greet()

def greet(name="raju",city="mumbai"):
    print("hello",name,"from",city)
    
greet() #hello raju from mumbai


#local
def msg():
    choice="i love you"
    print(choice)
msg()
print(choice) #it throws error because choice is not defined outside the function

#global 
choice="i love you"
def msg():
    print(choice)
msg()
print(choice) #it works because choice is defined outside the function