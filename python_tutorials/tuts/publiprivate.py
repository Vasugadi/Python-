class Account:
    def __init__(self, acc_no, acc_pass):
        self.no = acc_no
        self.__apass = acc_pass
#but we cant pass the account password outside the class because it can accessed by many
    def reset_pass(self):
        print(self.__apass)

s1=Account(1234567890, "1234567890")
s1.reset_pass()
print(s1.no)
print(s1.__apass) # it 