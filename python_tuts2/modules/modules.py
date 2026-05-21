#inbuilt modules math random date and time
import math
print(math.sqrt(16))
print(math.factorial(5))
print(math.pi)
print(math.e)
print(math.sin(0))
print(math.cos(0))
print(math.tan(0))
print(math.log(10))
print(math.log10(10))
print(math.log2(10))
print(math.log1p(10))

print(math.pow(2,3))

#random module
import random
print(random.randint(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.uniform(1,10))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],3))
print(random.shuffle([1,2,3,4,5]))

#date and time
import datetime
a=datetime.datetime.now()
print(a)

y=datetime.datetime(2022,1,1)
print(y)