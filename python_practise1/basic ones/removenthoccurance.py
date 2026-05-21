#list=["geeks","for","geeks","is","best"]

#list.remove("geeks")
occurance=2
#this means we should delete the 2nd geeks
list=["geeks","for","geeks","is","best"]
words="geeks"
count=0
for i in  range(0,len(list)):
    if list[i]==words:
        count+=1
        if count==occurance:
            del list[i] #it means that we are deleting the 2nd geeksfor geeks
            break
print(list)