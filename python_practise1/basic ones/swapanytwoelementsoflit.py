#list=[23,65,19]pos=1,pos2=3
#output=[19,65,23,90]

list=[23,65,19,90]

pos1=1

pos2=3

list[pos1],list[pos2]=list[pos2],list[pos1]
print(list)

#using pop method
mylist=[23,65,19,90]
w1=mylist.pop(pos1)
w2=mylist.pop(pos2-1)
mylist.insert(pos1,w2)
mylist.insert(pos2,w1)
print(list)


#using tuple
mylist=[23,65,19,90]
get=(mylist[pos1],mylist[pos2])
mylist[pos2],mylist[pos1]=get
print(mylist)

|