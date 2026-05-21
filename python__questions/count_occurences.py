my=[15,6,7,10,12,20,10,28,10]

tar=10
cnt=0
for i in my:
    if i==tar:
        cnt+=1
print(cnt)

#using count method

print(my.count(tar))

#using dictionary
my_dict={}
for i in my:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1
print(my_dict)
        
from collections import Counter
x=10
my_dict2=Counter(my)
print('{} has occured {} times'.format(x,my_dict2[x]))
