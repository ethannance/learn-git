# Nya Croft

from random import randint

class Order :
    def __init__ (self) :
        self.burger_count = self.randomBurgers()

    def randomBurgers (self) :
        iRandomNum = randint (1,20)
        return iRandomNum

class Person : 
    def __init__ (self) : 
        self.customer_name = self.randomName()
    
    def randomName (self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        iCustomerCount = len(asCustomers)
        iRandomCustomer = randint(0, iCustomerCount - 1)
        return asCustomers[iRandomCustomer]
    
class Customer (Person):
    def __init__ (self, oCustomer) :
        super().__init__()
        self.order = Order()

        #queueCustomers = []
    
oCustomer = Person()
