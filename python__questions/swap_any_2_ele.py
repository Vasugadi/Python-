list=[23,65,19,90]
pos=1
pos2=3
list[pos],list[pos2]=list[pos2],list[pos]
print(list)

#using pop and insert

a=list.pop(pos)
b=list.pop(pos2-1)
list.insert(pos2,a)
list.insert(pos,b)
print(list)

#using tuple unpacking
my_list=[23,65,19,90]
pos1,pos2=1,3
get=(my_list[pos1],my_list[pos2]) #packing
my_list[pos1],my_list[pos2]=get #unpacking
print(my_list)