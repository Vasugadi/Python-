







mylist=[1,2,3,4,5,6]
print(mylist.count(2)) #count occurence of element in list

# 
count=0
for i in mylist:
    if i==2:
        count+=1
print(count)

#
count=0
for i in range(len(mylist)):
    if mylist[i]==5:
        count=+1
print(count)


#print(f"count of 5 is {count}")
#print("{}has occured {} times".format(5,count))


#counter method
from collections import Counter

print(Counter(mylist)) # out will be in the form of dictionary with element as key and count as value
print(Counter(mylist)[5])
