my_list=["geeks","for","geeks","is","best","for"]
word="for"
n=2
count=0
for i in range(len(my_list)):
    if my_list[i]==word:
        count+=1
    if count==n:
        print("The word is present at the nth occurance")
        del my_list[i]
print(my_list)
    