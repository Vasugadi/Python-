"""
What is map()?

map() applies a function to every item in an iterable (like a list, tuple, etc.) and returns a map object (which you usually convert to a list).

"""

#map(function, iterable)


numbers = [1, 2, 3, 4]

def square(x):
    return x * x

result = list(map(square, numbers))
print(result)


#using map with lambda
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

#map with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))
print(result)


#convert string to integers
nums = ["1", "2", "3"]
ints = list(map(int, nums))
print(ints)

#apply function to pandas 
#df["salary_lakh"] = df["salary"].map(lambda x: x / 100000)