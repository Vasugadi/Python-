# def prod(a,b):
#     mul=a*b
#     print(mul)
#     return mul

# prod()
# if we dont assaign any arguments it will give error

#default parameters 
# assaigning a default value to a parameter,which is used if no argument is passed to the function

def prod(a=9,b=5):
    mul=a*b
    print(mul)
    return mul

prod()

#give default values to the parameters from last to first