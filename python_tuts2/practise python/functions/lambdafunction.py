# its also called as anonymous function
# it is a function without name
# it is used to create small functions
# it is used to create functions on the fly
#we use keyword lambda
#lambda arguments: expression condition

#example

add10 = lambda num: num + 10 
print(add10(5))



multiply = lambda num: num * 2
print(multiply(5))

rang=lambda x: x in range(x)

#
even = lambda n: [i for i in range(2, n+1, 2)]
print(even(10))

#
odd_seq = lambda n: list(range(1, n+1, 2))
print(odd_seq(9))

#
even_seq = lambda n: list(range(2, n+1, 2))
print(even_seq(10))
