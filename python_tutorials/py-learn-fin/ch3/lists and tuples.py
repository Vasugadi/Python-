#lists:a built in datatype that stores multiple items in a single variable
#it can store elements of different data types
marks1=78.9
marks2=98
marks3=67
marks4=78

marks=[78.9,98,67,78]
print(marks)
print(type(marks))

#indexing/slicing is their in lists'
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[0:])
print(marks[1:])
print(marks[:len(marks)])
print(marks[-1:-3])

#lists are mutable
marks[0]="nikki"
print(marks)

#len -to print length of list
print(len(marks))