class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setPrice(self,price):
        self.price = price
    def getPrice(self):
        return self.price
    def setQuantity(self,quantity):
        self.quantity = quantity
    # def getQuantity(self):
    #     return self.quantity
    # def decreaseQuantity(self):
    #     self.quantity -= 1
