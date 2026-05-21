class Ele:
    def __call__(self, name):
        self.n=name

s1=Ele()
s1("Sai")
print(s1.n)
del s1.n
print(s1.n) #AttributeError: 'Ele' object has no attribute 'n'
del s1
