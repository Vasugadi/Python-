class Acc:
    def __init__(self, acc_no,acc_pass):
        self.__acc_no = acc_no  # private attribute
        self.__acc_pass = acc_pass  # private attribute
        
    def change_pass(self, old_pass, new_pass):
        
        if old_pass == self.__acc_pass:
            print("not need to change")
        elif old_pass != new_pass:
            self.__acc_pass = new_pass
        else:
            print("Invalid Password")
    
    def display(self):
        print(f"Account Number: {self.__acc_no}")
        print(f"Account Password: {self.__acc_pass}")
    
s1=Acc(123456,"abc@123")
s1.change_pass("abc@123","xyz@123")
s1.display()