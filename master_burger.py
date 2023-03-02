import random

class Order () :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
    
    def randomBurgers(self) :
        self.random_burger = random.randint(0,20)
        return self.random_burger

class Person() :
    def __init__(self) :    
        self.customer_name = self.randomName()

    def randomName (self) :
        
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        random_name = random.randint(0,8)

        CustomerName = asCustomers[random_name]
        return CustomerName

class Customer (Person) :
    def __init__(self) :
        super().__init__()
        self.order = Order()

queue = []

customer_info = {}

iCustomerCount = 100

for iCount in range(1, iCustomerCount) :
    customer = Customer()
    queue.append(customer)
    customer_name = customer.customer_name
    burger_count = customer.order.burger_count
    if customer_name in customer_info :
        customer_info[customer_name] = customer_info[customer_name] + customer.order.burger_count
    else:
        customer_info[customer_name] = customer.order.burger_count

listSortedCustomers = sorted(customer_info.items(), key=lambda x: x[1], reverse = True)

print("\n")
for customer in listSortedCustomers:
    print(customer[0].ljust(19),str(customer[1]))
print("\n")

oPerson = Person()
