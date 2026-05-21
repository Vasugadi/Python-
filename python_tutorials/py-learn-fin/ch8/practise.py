#waf to print the length of list.list is the para meter
def len_list(list):
    print(len(list))

len_list([1,2,3,4,5,6,7,8,9,10])

###############################################################

#waf to print the elements of list in a single line
def print_list(list):
    for i in list:
        print(i)
    print_list([1,2,3,4,5,6,7,8,9,10])

#################################################################

#to print the factorial of a number
def cal_fact(a):
    fac=1
    for i in range(1,a+1):
        fac*=i
    print("this is",fac)
cal_fact(6)

################################################################

#to convert usd to rupee
def usd_to_inr(usd):
    inr=usd*80
    print(inr)
usd_to_inr(10)