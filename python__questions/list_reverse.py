list=[1,2,3,4,5]

#method 1
list.reverse()  

#method 2
list1=list[::-1]



#method 4
list3=[]

for i in range(len(list)-1,-1,-1):
    list3.append(list[i])
print(list)

#
st=list[0]
end=len(list)-1
while(st<end):
    list[st],list[end]=list[end],list[st]
    st+=1
    end-=1
print(list)