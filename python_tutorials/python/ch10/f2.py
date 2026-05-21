# r---- open for reading 
# w-----open for writing
# x----create a new file and open it for writing
# a----open for appending at the end of the file 
# b----binary mode
# t----text mode(default)
# +----open a disk file for updating (reading and writing)

#reading a file

# data=f.read()# reads entire file
# print(data)
# data=f.readline()#reads one line at a time
# print(data)

# to print the starting 5 letters
d=open("demo.txt","r")
data=d.read(5)
print(data)

# to print the starting line
d=open("demo.txt","r")
data=d.readline()
print(data)

