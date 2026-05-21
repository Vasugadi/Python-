# wap to ask the user to enter the names of their 3 favourite books and store them in a list

name1=input("enter the name of your first favourite book")
name2=input("enter the name of your second favourite book")
name3=input("enter the name of your third favourite book")

fav_books=[name1,name2,name3]
print(fav_books)

movies=[]
mov1=input("enter the name of your first favourite movie")
movies.append(mov1)
mov2=input("enter the name of your second favourite movie")
movies.append(mov2)
mov3=input("enter the name of your third favourite movie")
movies.append(mov3)
print(movies)


# wap to  check if a list contains a palindrome of elements
list=[1,2,3,2,1]
list2=list.copy()
list2.reverse()
if list==list2:
    print("palindrome")
else:
    print("not palindrome")

#wap to count the number of occurences of a given element in a tuple
tup=["C","D","A","A","B","A"]
print(tup.count("A"))

TUP=["C","D","A","A","B","A"]
print(TUP.sort())