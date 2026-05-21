# python can be used to read and write files
# types of all files
#1.text files:.txt,.docx,.log
#2.binary files:.jpg,.png,.mp3,.mp4,.exe,.dll,.iso,.dat,.db,.pdf,.doc,.ppt,.xls,.csv
#3. compressed files:.zip,.rar,.7z
#4. executable files:.exe,.bat,.cmd

a=open("demo.txt","r")
data=a.read()
print(data)
a.close()

# #write file
# a=open("demo.txt",'w')
# a.write("hello world")
# a.close()

# #append file
# a=open("demo.txt",'a')
# a.write("hello world")
# a.close()