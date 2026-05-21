# #to print output
# print("hello world")
# #variable
# name="vasu"
# age=45
# price=5.09
# print("my name is",name,"and my age is ",age,"and price is ",price)
# #variable should be start with alphabet or underscore
# _ani="hello"
# print(_ani)
# print(type(name))
# print(type(age))
# print(type(price))
# #int datatype '
# a=1
# b=-2
# print(type(a),type(b))
# #STRING DATATYPE
# name="vasu"
# name1='vasu'
# name3="""vasu"""
# name2='''vasu'''
# print(name,name1,name3,name2)
# print(type("hello"))
# #float datatype
# print(type(5.09))
# print(type(5.0))
# print(type(5.))
# #bool datatype
# age=True
# print(type(age))
# print(type(False))
# #NONE
# g=None
# print(type(g))

#TO PRINT SUM OF TWO NUMBERS    
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# sum=a+b
# print(sum)
# diff=a-b
# mul=a*b
# div=a/b
# print(diff,mul,div)

#expressin execution
# 1.string and numeric values can operate with *
# a,b=2,3
# txt="@"
# print(2*txt*3)
# # 2. string and string can operate with +
# a,b="2",3
# txt="@"
# print((a+txt)*b)
# #numeric values can operate with +,-,*,/,%,//,**,//
# a=5
# b=9
# print(a+b*a-b/a//a%a**a)
# #arithmetic operation with int and float will results in float
# a=5.9
# b=8
# print(a+b)
# # result of division of two int will result float
# a=9
# b=8
# print(a/b)
# print(a//b)#integer divison 

# #integer division with float and int will result in float
# a=1.4
# b=2
# print("normal div",a/b)
# print(a//b)
# #floor division will give closrst integer which is either lesser or equal to the actual value
# a,b=12,5
# print(a//b)
# a,b=-12,5
# print(a//b)
# a,b=12,-5
# print(a//b)
# #result of floor division(a//b) is equal to floor value of(a/b)

# #modulus operator
# a,b=-5,2
# print(a%b)
# a,b=5,2
# print(a%b)
# a,b=5,-2
# print(a/b)
# print(a%b)

# """ multi line comment """
# #single line comment
# '''multi line comment'''

# #input
# #string input
# name=input("enter your name")
# print(name)
# #int input
# age=int(input("enter your age"))
# print(age)

# #float input
# price=float(input("enter price"))
# print(price)

#best practise
p=float(input("enter first principal"))
r=float(input("enter second rate"))
t=float(input("enter third time"))
si=p*r*t/100
print("simple interest is ",si)

