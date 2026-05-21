list=[1,2,3,4,5]
print(max(list))
print(min(list))

import numpy as np

a=np.array([1,2,3,4,5])
print(np.max(a))
print(np.min(a))

#
ma_x=0
mi_n=600
for i in range(0,len(list)):
    if list[i]>ma_x:
        ma_x=list[i]
    if list[i]<mi_n:
        mi_n=list[i]
print(ma_x)
print(mi_n)


# or 
mylist = [1, 2, 3, 4, 5]
ma_x = mylist[0]
mi_n = mylist[0]

for i in range(len(mylist)):
    ma_x = max(mylist[i], ma_x)
    mi_n = min(mylist[i], mi_n)

print("Maximum:", ma_x)
print("Minimum:", mi_n)


#
list=[1,2,3,4,5]
list.sort()
print(min,list[0])
print(max,list[-1])

