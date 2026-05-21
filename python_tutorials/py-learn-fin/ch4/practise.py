#wap to ask the user to  enter names of 3 favourite movieees and store it in list
mov=[]
movie1=input("enter the names of 3 favourite movies: ")
mov.append(movie1)
movie2=input("enter the names of 3 favourite movies: ")
mov.append(movie2)
movie3=input("enter the names of 3 favourite movies: ")
mov.append(movie3)

print(list)

#wap to print whether its palindrome or not
num=[1,2,3,4,5]
check=num.copy()
num.reverse()
print(num)
if num==check:
    print("palindrome")
else:
    print("not palindrome")


#to count numbers of students with a grade
list=("A","B","C","D","E")
li=[list]
li.sort()
print(li)
print(list.count("A"))

#