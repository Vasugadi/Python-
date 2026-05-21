def rec(n):
    if n==0:
        return
    print(n,end=" ")
    rec(n-1)

rec(10)

def recc(n):
    if n==0:
        return 1
    return (n+recc(n-1))
print(recc(5))
    
def fac(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*fac(n-1))
print(fac(5))

def printList(list,idx):
    if(idx==len(list)):
            return 
    print(list[idx],end=" ")
    printList(list,idx+1)
printList([1,2,3,4,5],5)