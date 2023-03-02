# Nya Croft, Matt Layden, Ethan Nance, Adam Kelley, Mclain Bement, Cameron Hammond

# Write a program that generates a random burger number order and assigns it to a random customer name. 
# Add 100 customers to a queue and keep a running total of the burger count using a dictionary. 
# Display the customer name and running burger count total.

# Import random function
from random import randint

# Create Order class
class Order :
    def __init__ (self) :
        self.burger_count = self.randomBurgers()

    # Generate random number for burgers
    def randomBurgers (self) :
        iRandomNum = randint (1,20)
        return iRandomNum

# Create Person class
class Person : 
    def __init__ (self) : 
        self.customer_name = self.randomName()
    
    # Select a random name from the list
    def randomName (self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        iCustomerCount = len(asCustomers)
        iRandomCustomer = randint(0, iCustomerCount - 1)
        return asCustomers[iRandomCustomer]

# Create Customer class
class Customer (Person):
    def __init__ (self) :
        super().__init__()
        self.order = Order()

# Create queue and dictionary
queue = []
customer_info = {}

# Initialize customer count
iCustomerCount = 100

# Add customers to queue and keep a running total of the burger count using a dictionary
for iCount in range (1, (iCustomerCount + 1)) :
    customer = Customer()

    # Add customer to queue
    queue.append(customer)

    customer_name = customer.customer_name
    burger_count = customer.order.burger_count

    # Check to make sure the key exists, and if so, assign burger value. If not, create key
    if customer_name in customer_info :
        customer_info[customer_name] = customer_info[customer_name] + customer.order.burger_count
    else :
        customer_info[customer_name] = customer.order.burger_count

    queue.pop(0)

# Sort customers
listSortedCustomers = sorted(customer_info.items(), key=lambda x: x[1], reverse=True) 

# Print customers and burger count values
print ("\n")
for customer in listSortedCustomers :
    print(customer[0].ljust(19), str(customer[1]))
print ("\n")
