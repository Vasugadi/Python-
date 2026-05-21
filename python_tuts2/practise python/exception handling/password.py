
def check_Password(password):
    if len(password) < 8:# its custom exception
        raise Exception("Password is too short")
    print("Password is valid")
    
try:
    password = input("Enter password: ")
    check_Password(password)
except Exception as e:
    print(e)
    
    