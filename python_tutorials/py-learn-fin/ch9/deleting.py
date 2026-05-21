# deleting a file using os.remove()
# module : like a code library is a file already 
# a programmer that generally has function we 
#we can use in our program

import os
with open("test.txt", "a") as f:
    f.write("This is a test file")

os.remove("test.txt")

# to install theese kind of packages 
# we use pip install package_name
# here pip means package installer for python