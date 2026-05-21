f1=open("prac1.txt","w")
f1.write("hi every  one, \n we are learning file i/o ,\n using java\n,i like programming in java ")

f1.close()

with open("prac1.txt","r") as f:
    print(f.read())
    f.close()

f2=open("prac1.txt","a")

with open("prac1.txt","r") as f2:
    data=f2.read()
    new_Data=data.replace("java","pyt")
    print(new_Data)
    f2.close()

with open("prac1.txt","w")as f4:
    f4.write(new_Data)
    f4.close()
with open("prac1.txt","r") as f3:
    print(f3.read())
    f3.close()

def find_word():
    word="learning"
    with open("prac1.txt","r") as f5:
        data=f5.read()
        if data.find(word) !=-1:
            print("word is present")
        else:
            print("word is not present")
find_word()

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("prac1.txt","r") as f6:
        while data:
            data=f6.readline()
            if word in data:
                print("word is present in line",line_no)
                break
            line_no+=1
    return -1

print(check_for_line())

count=0
with open("practise3.txt","r") as A:
    data=A.read()
    print(data)
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)