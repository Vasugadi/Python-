with open("practise.txt","w") as dt:
    dt.write("hello world\nwe are learning file I/o\n")
    dt.write("this is the end of the file")


with open("practise.txt","r")as f:
    data=f.read()
    print(data)
    new_Data=data.replace("hello","hi")
    print(new_Data)

word=input("enter the word you want to search")
with open("practise.txt","r") as f:
    data=f.read()
    print(data)
    if (data.find(word)!=-1):
        print("word found")
    else:
        print("word not found")


def check_for_line():
    wprd="learning"
    data=True
    line_no=1

    with open("practise.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
        return -1
check_for_line()
        

