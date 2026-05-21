list=[3,2,4]
product=1
for i in list:
    product*=i
print(product)

import numpy as np
list=[3,2,4]
print(np.prod(list)) #built in function to calculate the product of all elements in list
