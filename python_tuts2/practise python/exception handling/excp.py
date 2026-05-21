"""  
exception - an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions.
1- start running
2- warning sign
3- catch and handle, program  crash

exception handling - a mechanism in Python for handling runtime errors so that the program can continue to run instead of crashing.

try - block - code that might raise an exception
except block - code that runs if an exception is raised in the try block
finally - block - code thate runs no matter what happens in the try and except blocks


try - code error
except - error handling 
finally block -- is used to 



"""
try:
    num = int(input("Enter a number: "))
    print(num)
    result=10/num
    print(f'result:{result}')
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Invalid input. Please enter a number.")
except Exception as e:
    print("An error occurred:", str(e))
    
    
    
try:
    file= open("C:\\Users\\HP\\OneDrive\\Desktop\\Programming languages\\python\\practise python\\exception handling\\notes.txt")
    content=file.read()
    print(content)
    
except FileNotFoundError:
    print("File not found.")
    
finally:
    
    file.close()
    