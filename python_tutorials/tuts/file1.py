f1=open("demo.txt","r")
data=f1.read()
print(data)
f1.close()
f2=open("demo1.txt","w")
f2.write(data)
f2.close()
f3=open("demo1.txt","r")
data1=f3.read()
print(data1)
f3.close()

with open('demo.txt',"r") as f1:
    data=f1.read()
    print(data)

with open('demo1.txt',"w") as f2:
    f2.write("data is insered///" )

with open('demo1.txt',"r") as f3:
    data1=f3.read()
    print(data1)

import os
os.remove("demo1.txt")