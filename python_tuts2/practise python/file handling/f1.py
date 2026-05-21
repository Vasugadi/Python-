""" 
we need to open the file 
to open we use open(filename,mode)

 
"""
f=open("C:\\Users\\HP\\OneDrive\\Desktop\\Programming languages\\python\\practise python\\exception handling\\notes.txt","r")
data=f.read() #to read the file
f.close()
print(data)


with open("C:\\Users\\HP\\OneDrive\\Desktop\\Programming languages\\python\\practise python\\exception handling\\notes.txt","r") as f:
    d=f.read()
    print()
    
with open("file.txt","w") as f:
    f.write("hello world")
    f.close()
    
with open("file.txt","r") as f:
    do=d.read()
    f.close()
print(do)