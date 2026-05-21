string="hello world"
sub_str="world"
res=string.find(sub_str)#returns the starting index of the substring if found, otherwise returns -1

if res!=-1:
    print(sub_str,"is present in the string")
else:
    print(sub_str,"is not present in the string")
