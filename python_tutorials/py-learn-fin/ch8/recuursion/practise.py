#write a program to print sum of first n natural numbers using recursion

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum(5))

def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n

res=sum(5)
print(res)


def l(list,idx):
    if(idx==len(list)):
        return 0
    print(list[idx],end=" ")
    return l(list,idx+1)

l([1,2,3,4,5],0)