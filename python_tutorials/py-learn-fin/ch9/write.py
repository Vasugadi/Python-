w=open("demo.txt","w")
data=w.write("hello world\n")
print(data)

w.close()

#to append data to the file
a=open("demo.txt","a") # append adds at the end
data=w.write("hello world\n")


a.close()

# write= w that means over write
# append =a that means add at the end