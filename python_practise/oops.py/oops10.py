class Bank:
    def __init__ (self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)

b1 = Bank("123456789", "password123")
b1.reset_pass()  # Output: password123
print(b1.acc_no)  # Output: 123456789



class Person:
    __name="Anonymous"  # Private variable

    def __hello(self):
        print("Hello, " + self.__name)  # Private method

    def greet(self):
        self.__hello()  # Accessing private method from public method

p1 = Person()
p1.greet()  # Output: Hello, Anonymous
