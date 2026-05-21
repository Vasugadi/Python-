# when a function calls itself repeatedly, it is called recursion

def show(n):
    if n == 5:
        return
    else:
        print(n)
        show(n+1)

show(0)#5 ,n-1=4,n-2=3,n-3=2,n-4=1,n-5=0 return


def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)#6*n-1=6*5=30,6*5*4=120,6*5*4*3=360,6*5*4*3*2=720,6*5*4*3*2*1=720

print(fac(6))

# recursion is a powerful tool in programming, but it can also be difficult to understand and debug. It is important to use recursion judiciously and to be aware of the potential for stack overflow errors.
# sum of n natural numbers
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5))

# to print the list
def li(list,idx=0):
    if (idx == len(list)):
        return
    else:
        print(list[idx])
        li(list,idx+1)
li([1,2,3,4,5])

def li(list,idx=0):
    if(idx==len(list)):
        return 0
    else:
        print(list[idx])
        li(list,idx+1)

li([1,2,3,4,5])
        