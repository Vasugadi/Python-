def callen(list):
    print(len(list))

a=[1,2,3,4,5]
callen(a)

def print_list(l):
    for el in l:
        print(el,end=" ")

print_list(a)   


def fac(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
    return f
a=fac(8)
print(a)
print(fac(5))   


# to convert usd to inr
def usd_to_inr(usd):
    inr=usd*74.5
    print(inr)
usd_to_inr(100) # 7450.0 

# to convert inr to usd
def inr_to_usd(inr):
    usd=inr/74.5
    print(usd)
inr_to_usd(7450) # 100.0

def evorod(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
    
x=int(input("enter a number: "))
evorod(x)