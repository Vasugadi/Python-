 
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5)

def calc_Sum(n):
    if n==0:
        return 0
    return n+calc_Sum(n-1)
print(calc_Sum(5))

def calc_Fact(n):
    if n==0:
        return 1
    return n*calc_Fact(n-1)
print(calc_Fact(5))

# to print all elements in a list
def print_list(l,idx=0):
    if idx==len(l):
        return
    print(l[idx])
    print_list(l,idx+1)
print_list([1,2,3,4,5])
