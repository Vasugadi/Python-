# python can be used to read and write files
# it can perform file operations such as opening, reading, writing, closing, and more

# day to day life we deal with file
#by opening a file we can read or write data to it and then close
#f =open('filename', 'mode')
#mode can be 'r' for reading, 'w' for writing, 'a' for appending, 'x' for creating, 'b' for binary, 't' for text, '+' for updating

#to read a file
#f = open('filename', 'r')
#data = f.read()
#print(data)
#f.close()
#or
#with open('filename', 'r') as f:
#    data = f.read()
#print(data)

#to write a file
#f = open('filename', 'w')
#f.write('data to write')
#f.close()
#or
#with open('filename', 'w') as f:
#    f.write('data to write')

# f=open("demo.txt", "r")
# data=f.read()
# print(data)
# print(len(data))
# f.close()

# "r"  open for reading (default)
# "w"  open for writing, truncating the file first
# "x"  create a new file and open it for writing
# "a"  open for writing, appending to the end of the file if it exists
# "b"  binary mode
# "t"  text mode (default)

# "r+"  open for reading and writing
# "w+"  open for reading and writing, truncating the file first
# "x+"  create a new file and open it for reading and writing
# "a+"  open for reading and writing, appending to the end of the file if it exists
# "b+"  binary mode


# data=f.read(5) reads characters
# data=f.readline() reads a line

# f=open("demo.txt", "r")
# data=f.read()
# print(data)

# d1=f.readline()#read line in output it will give u an empty line
# print(d1)

# d2=f.readline()#read line
# print(d2)

# f.close()


r=open("C:\Users\HP\Desktop\py-learn-fin\ch9\demo.txt", "r")
data=r.read()
print(data)
data2=r.readlines()#read lines
print(data2)
r.close()