# range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# range(start, stop, step)

# start: The value of the first number in the sequence.
# stop: The value of the last number in the sequence (not included).
# step: The value by which the sequence increments (optional).
# Example 1: Print numbers from 0 to 9
for i in range(10):
    print(i)

# Example 2: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Example 3: Print numbers from 0 to 10 with a step of 2
for i in range(0, 11, 2):
    print(i)


print(range(23))
# Output: range(0, 23)

seq= range(23)
li=list(seq)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
tup=tuple(li)
print(tup)
print(li)

print(seq[0])
# Output: 0 
print(seq[1])
# Output: 1

se=range(10)
for i in se:
    print(i)