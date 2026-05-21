#a functiom calls itself repeatedly is called recursion
#base case
def factorial(n):
    if n==1 or n==0 :
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5)) 

#call stack 
def show(n):
    if(n==0):
        return  
    print(n)
    show(n-1)
show(5)
# |__________________|n=1 layers
# |                  |n=2
# |                  |n=3
# |                  |n=4
# |__________________|n=5

def show (n):
    if(n==100):
        return
    print(n)
    show(n+1)
    print("end")

show(1)

#factorial 
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
 