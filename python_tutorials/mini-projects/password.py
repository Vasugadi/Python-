import random
import string

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)
#ascii -- american standard code for information interchange
#97-122 are lowercase letters
#65-90 are uppercase letters




charset=string.ascii_letters + string.digits + string.punctuation

password_length = 12
password = ""
for i in range(password_length):
    # print(random.choice(charset))
    password += random.choice(charset)

print("the passwor is ",password)

