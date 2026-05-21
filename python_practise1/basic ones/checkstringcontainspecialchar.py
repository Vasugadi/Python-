input="welcome to python programming"

for i in input:
    if i.isalpha() or i.isspace():
        continue
    else:
        print("special character found")
        break
    
#
import re
str="welcome to python programming"
regex=re.compile("[^a-zA-Z0-9 ]")
if(regex.search(str)==None):
    print("No special character found ")
else:
    print("special character found")
    