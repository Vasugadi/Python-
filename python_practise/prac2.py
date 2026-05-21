class Order:
    def __init__ (self,item,price):
        self.item=item
        self.price=price

    def showDetails(self):
        print("Item: ",self.item)
        print("Price: ",self.price)

    def __gt__ (self, other):
        return self.price > other.price
    

order1 = Order("Laptop", 1500)
order1.showDetails()  # Output: Item: Laptop, Price: 1500
order2 = Order("Phone", 800)
order2.showDetails()  # Output: Item: Phone, Price: 800
answer = order1 > order2
print("Is order1 more expensive than order2?", answer)  # Output: Is order