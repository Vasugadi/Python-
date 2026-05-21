#lambda
#lambda attributes:expression
#print(lambda x:x+1)
add = lambda x, y: x + y
print(add(5, 6))

#lambda with filter
numbers = [1, 2, 3, 4, 5, 6]
result= list(filter(lambda x: x % 2 == 0, numbers))
print(result)
#filter is used to filter the elements of a list based on a condition. In this case, we are filtering out the even numbers from the list of numbers using a lambda function as the condition. The lambda function takes an element x and checks if it is divisible by 2 (i.e., if it is even). The filter function returns an iterator that contains only the elements that satisfy the condition, which we convert to a list using the list() function.

#lambda with map
numbers = [1, 2, 3, 4, 5, 6]
result= list(map(lambda x: x * 2, numbers))
print(result)
#map is used to apply a function to each element of a list. In this case, we are using a lambda function to multiply each element of the list of numbers by 2. The map function returns an iterator that contains the results of applying the function to each element, which we convert to a list using the list() function.


students = [("Ram", 85), ("Sam", 72), ("Raj", 90)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#sorted is used to sort a list of tuples based on a specific key. In this case, we are sorting the list of students based on their scores (the second element of each tuple). The lambda function takes a tuple x and returns the second element (x[1]), which is used as the key for sorting. The sorted function returns a new list of tuples sorted in ascending order based on the scores.


#df["salary_lakh"] = df["salary"].map(lambda x: x / 100000)


check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(5))