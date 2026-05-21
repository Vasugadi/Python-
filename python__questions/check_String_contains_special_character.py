import re
string="hello@world"

regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]') #regular expression to match special characters
if regex.search(string)==None:
    print("string does not contain any special character")
else:
    print("string contains special character")