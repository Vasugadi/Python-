# function is a block of code which is executed only when it is called
# def function_name(parameters): # function definition
#     some work
#     return something

# def greet(name):// name is a parameter
#     print(f"hello {name}")// f is used to format the string

#     print("how are you")

# greet("marco") // marco is an argument // totally its called function calling

# normal 
a=8
b=9
sum=a+b
print("normal method",sum)

# function
def add(a,b):
    sum=a+b
    return sum
a=add(6,8)
print(a)
# print(f"function {add(8,9)}")
# print(add(4,5))
# print(add(5,6))

# code redundance is not allowed in programming
#code redundance means writing the same code again and again
# code reusability is allowed in programming
# to avoid the redundant code and reusability we use functionsa

def calcprof(x,y):
    prod=x*y
    return prod
print(calcprof(5,6))

#ideally it do 
# input---->function------>output

