#write a program to input 2 numbers and print their sum
a=int(input("entr the vlaue of a: "))
b=int(input("entr the value of b: "))
sum=a+b
print("the sum of a and b is: ",sum)

#wap to input a side of asquare and print its area
side=int(input("enter the side of  square: "))
area=side*side
print("the area of square is: ",area)

#wap to input a  floating numbers and print their average
a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
avg=(a+b)/2
print("the average of a and b is: ",avg)

a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
print("TRUE") if(a>b or a==b) else print("FALSE")
val=("true","false")[a>=b]
print(val)