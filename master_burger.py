#Ethan Nance
#This program will use recent concepts learned in class/textbook to track exactly how many hamburgers each customer eats in the door dash example

#Import random
import random

#Create the Order class with constructor
class Order () :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
    
    #Create the random burgers method
    def randomBurgers(self) :
        self.random_burger = random.randint(0,20)
        return self.random_burger

#Create the person class with constructor
class Person() :
    def __init__(self) :    
        self.customer_name = self.randomName()

    #Create the random name method
    def randomName (self) :
        
        #Create list of names to use, and assign each name an integer value
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        random_name = random.randint(0,8)

        #Return customer name
        CustomerName = asCustomers[random_name]
        return CustomerName

#Create the customer class with constructor, and call parent class using super
class Customer (Person) :
    def __init__(self) :
        super().__init__()
        self.order = Order()

#Create a queue to hold customers
queue = []

#Create a dictionary to hold customer information
customer_info = {}

#Set customer count to 100
iCustomerCount = 100

#Loop to create and add customers to queue and update customer information in dictionary
for iCount in range(1, iCustomerCount + 1) :
    customer = Customer()
    queue.append(customer)
    customer_name = customer.customer_name
    burger_count = customer.order.burger_count
    if customer_name in customer_info :
        customer_info[customer_name] = customer_info[customer_name] + customer.order.burger_count
    else:
        customer_info[customer_name] = customer.order.burger_count

#Sort the customer information in descending order by the number of burgers eaten
listSortedCustomers = sorted(customer_info.items(), key=lambda x: x[1], reverse = True)

#Print out the customer information
print("\n")
for customer in listSortedCustomers:
    print(customer[0].ljust(19),str(customer[1]))
print("\n")
