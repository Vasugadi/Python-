#super method used to call parent class method
class A:
    def show(self):
        print("in class A")
class B(A):
    def show(self):
        print("in class B")
        super().show()
        
b=B()
b.show()
