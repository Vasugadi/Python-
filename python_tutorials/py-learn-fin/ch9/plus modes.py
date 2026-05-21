file=open("tet.txt","r+")
file.write("hello")
data=file.read()
print(data)
file.close()


f=open("tet.txt","w+")
data=f.read()
print(data)
f.write("hello")
f.close()

# r+ read and write(overwrite) (ptr starts)-- no truncate
# w+ read and write (overwrite) (ptr starts) -- truncate
# a+ read and write (append) (ptr starts) -- no truncate



