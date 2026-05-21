class Delete:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Object {self.name} is being deleted")


d1 = Delete("John")
del d1
print("Deleted")
print(d1.name)  # This will raise an error since d1 is deleted
# del d1.name


