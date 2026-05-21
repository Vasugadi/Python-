# writing to a file
# write will overwrite the file
# write will create a new file if it does not exist
# write will not add new line

# we can write in a file using append() method
#append method will add new line at the end of the file
#append method will create a new file if it does not exist
# we can write in a file using write() method

df=open("sun.txt","w")
kim=df.write("hello world")
print(kim)

df.close()

dt=open("sun.txt","a")
kim=dt.write("hello world")
print(kim)
 
# reading from a file
# read() method will read the whole file
# read() method will return a string
# read() method will return an empty string if the file is empty
# read() method will return an empty string if the file is closed