def rec(num):
    if(num==0):
        return 0
    else:
        return num+rec(num-1)
    
def fac(num):
    if(num==0):
        return 1
    else:
        return num*fac(num-1)

print(rec(5))