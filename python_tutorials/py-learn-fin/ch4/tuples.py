#tuples are used to a built in datatypes that create immutable sequence of values
#tuples are written with round brackets and are immutable
#tuples are used to store multiple values in a single variable
tup=()#empty tuple
tup1=(1,2,3,4,5,6,7,8,9,10)
tup2=(1,)#tuple with single value

#index accessing is possible in tuple
tupe=(1,2,3,4)
print(tupe[0])

#item assaignment is not possible in tuple
tup=(1,2,3,4)
tup[0]=5
print(tup)

#answer will diff without , when using single value in tuple
tup=(1)
print(type(tup))
tup=(1,)
print(type(tup))