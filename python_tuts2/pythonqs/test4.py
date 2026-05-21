#sum of all even numbers from upto 50
sum = 0
for i in range(0,51,2):
    sum+= i
print("Sum of all even numbers from 0 to 50 is:", sum)

#first 20 numbers and their squares
for i in range(1,21):
    print(i, "squared is", i**2)


#sum of all odd numbers from 0 to 50
sum=0
n=0
while n <=50:
    if n % 2 != 0:
        sum += n
    n += 1

print("Sum of all odd numbers from 0 to 50 is:", sum)


for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i)
    else:
        print('NA')


#billing system at supermarket
while True:
    print("Welcome to the supermarket billing system")
    print("1. Add item")
    print("2. Remove item")
    print("3. View bill")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        print(f"Added {quantity} of {item} at ${price} each.")
        
    elif choice == '2':
        item = input("Enter item name to remove: ")
        print(f"Removed {item} from the bill.")
        
    elif choice == '3':
        print("Viewing bill...")
        
        
    elif choice == '4':
        print("Exiting the billing system.")
        break
        
    else:
        print("Invalid choice, please try again.")
    

