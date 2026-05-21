#String and numeric values can operate together with *
A,B=2,3
Txt='@'
print(A*Txt*3) #@@@@@@

#string and string can oprate with +  {we }
A,B="2",3
txt="@"
print((A+txt)*B) #2@2@2@

#numeric values can operate with + - * / % ** //
A,B=2,3
C=4
print(A+B*C) #14 by using BODMAS RULE

#arithmetic expressions with integer and float will result in float
A,B=2,4.0
C=A*B
print(C) #8.0

#result of division operator with two integers will be float
A,B=2,3
C=A/B
print(C) #0.6666666666666666

#integer division operator with float and int will give int displayed as float
A,B=1.5,3
C=A//B
print(C,A/B) #0.0 0.5

#floor gives closest integer which is lesser than or equal to the float value
#result of a//b is same as floor(a/b)
A,B=12,5
C=A//B
print(C) #2

A,B=-12,5
C=A//B
print(C) #-3

A,B=12,-5
C=A//B
print(C) #-3