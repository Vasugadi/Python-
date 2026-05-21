# random password generator
# ascii ---american standard code for information interchange
import random
import string
# random_num=random.choice([1,2,3,4,5,6,7,8,9,0])
# random_char=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
# random_char2=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
# random_char3=random.choice(['@','#','$','%','&','*','(',')','_','+','!','^','~','?','/','<','>','{','}','[',']','|','`',';','\'',':','"'])
charValues=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(0,12):
    password+=random.choice(charValues)

print(password,"its my password")
    


#list comprehension
res="".join([random.choice(charValues) for i in range(0,12)])# .join helps to join the elements of the list
print(res)

