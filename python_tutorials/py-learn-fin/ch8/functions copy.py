#functions in python
#block of code that performs a specific task
#code re-usability increases by using  functions
#redundant code is avoided


#function definition
def calc_sum(a,b):
    sum=a+b
    print(sum)

    return sum

#function calling
calc_sum(1,2)
calc_sum(3,4)
calc_sum(5,6)
calc_sum(7,8)
calc_sum(9,10)

#professional way of doing a thing
def calc_sum(a,b):
    return a+b

x=1
y=3
result=calc_sum(x,y)
print(result)

#average 
def calc_average(a,b):
    average=(a+b)/2
    print(average)
    # return average
result=calc_average(1,2)
print(result)