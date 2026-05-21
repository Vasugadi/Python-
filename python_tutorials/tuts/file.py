f1=open("demo.txt","r")
data=f1.read()
print(data)
f1.close()

f2=open("demo.txt","a")
f2.write("\nNew line added")
f2.close()

f3=open("demo.txt","r")
data=f3.read()
print(data)

f4=open("demo.txt","w")
f4.write("This is a new file")
f4.close()

f5=open("demo.txt","a")
f5.write("This is a new file")
f5.close()

f6=open("demo.txt","r")
data=f6.readline()
print(data)

# to over ride the things
f7=open("demo.txt","r+")
f7.write("hey")
f7.close()

f8=open("demo.txt","r")
data=f8.read()
print(data)

#w+ mode will truncate the data and it will writes the data
#a+ mode will append the data to the existing file and writes the data if there is no such file it will create
with open("demo.txt","a+") as f:
    f.write("This is a new file")
    data=f.read()
    print(data)

import os
# os.remove("demo.txt")
# os.mkdir("demo.txt")
# os.rename("demo.txt","demo1.txt")
# os.rmdir("demo1.txt")
#os.rmdir("demo.txt") # it will remove the directory
#os.mkdir("demo.txt") # it will create the directory

#os.rename("demo.txt","demo1.txt") # it will rename the file
    
with open("d1.txt","r")as f:
    # f.write("Hi everyone \n we are learning python \n using java \n i like programming")
    data=f.read()
    print(data)

with open("d1.txt","r+")as f:
    data=f.read()
    data.replace("java","python")
    print(data)
    
with open("d1.txt","w")as f:
    f.write(data)

with open("d1.txt","r")as f:
    data=f.read()
    print(data)


def check_for_word():
    word="learning"
    with open("d1.txt","r") as f:
        data=f.read()
        if(data.find(word)!= -1):
            print("python is present")
        else:
            print("python is not present")
check_for_word()

data="lear"
print(data[0])

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("d1.txt","r")as f:
        while data:
            data=f.readline()
            if(word in data):
                 print(line_no)
            line_no+=1
    return -1
print(check_for_line())