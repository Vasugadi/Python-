# #private attributes are meant to be used only within the class 
# #and they are not accessible outside the class

# class Account:
#     def __init__(self, acc_no, acc_paa):
#         self.acc_no = acc_no
#         self.__acc_paa = acc_paa #its now private

#     def reset(self):
#         self.__acc_paa = 1234 #we can access it using this syntax

# acc1=Account(123456, 1234)
# print(acc1.acc_no)
# print(acc1.reset())
# print(acc1.Account__acc_paa) #we can access it using this syntax








class Person:
    __name="John" #private attribute

    def __hello():
        print("Hello") #private method
        
    def welcome(self):
        print("Welcome", self.__name)


p1=Person()
# print(p1.__name)
 #this will give an error
p1.welcome()