from Product import Product
from Payment import Cash, Card

class VendingMachine:
    """
    this class is a singleton
    """
    __instance = None
    credit = Cash()
    card = Card()

    Basket = {}

    itemHistory = [[],[],[],[],[],[]]

    vendorBalance = [2995.5]

    pin = []

    @staticmethod
    def inpPin(value):
        VendingMachine.pin.append(value)

    @staticmethod
    def readItems():
        with open("plot_input.txt", "r") as f:
            i = 0
            for line in f:
                values = line.split()
                for value in values:
                    VendingMachine.itemHistory[i].append(value)
                i += 1

    @staticmethod
    def insertProduct(product):
        if product.name not in VendingMachine.Basket :
            VendingMachine.Basket[product.name] = 1
        else:
            VendingMachine.Basket[product.name] += 1

    @staticmethod
    def getBasket():
        products = ""
        for i in VendingMachine.Basket.keys():
            products += str(VendingMachine.Basket[i]) + " x " + i + "/n"
        return products

    @staticmethod
    def getBasketPrice():
        sum = 0
        for i in VendingMachine.Basket.keys():
            sum += VendingMachine.getInstance().prices[str(i)]*VendingMachine.Basket[str(i)]
        return sum

    @staticmethod
    def clearBasket():
        VendingMachine.Basket = {}

    @staticmethod
    def getInstance():
        """ Static access method. """
        if VendingMachine.__instance == None:
            VendingMachine()
        return VendingMachine.__instance

    @staticmethod
    def getPrices():
        AviraPrime = Product("Avira Prime",75)
        AntiVirusPRO = Product("Antivirus PRO", 35)
        PhantomVPN = Product("Phantom VPN",50)
        PasswordManager = Product("Password Manager", 20)
        Optimizer = Product("Optimizer",10)
        SystemSpeedup = Product("System Speedup",25)
        pricelist = {AviraPrime.getName(): AviraPrime.getPrice(),
                    AntiVirusPRO.getName(): AntiVirusPRO.getPrice(),
                    PhantomVPN.getName(): PhantomVPN.getPrice(),
                    PasswordManager.getName(): PasswordManager.getPrice(),
                    Optimizer.getName(): Optimizer.getPrice(),
                    SystemSpeedup.getName(): SystemSpeedup.getPrice()}
        return pricelist

    def __init__(self, noAviraPrime, noAntivirusPRO, noPhantomVPN, noPasswordManager, noOptimizer, noSystemSpeedup, totalCash, cardBalance):
        if VendingMachine.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AviraPrime = Product("Avira Prime",75)
            AntiVirusPRO = Product("Antivirus PRO", 35)
            PhantomVPN = Product("Phantom VPN",50)
            PasswordManager = Product("Password Manager", 20)
            Optimizer = Product("Optimizer",10)
            SystemSpeedup = Product("System Speedup",25)

            self.products = {AviraPrime.getName(): noAviraPrime,
                             AntiVirusPRO.getName(): noAntivirusPRO,
                             PhantomVPN.getName(): noPhantomVPN,
                             PasswordManager.getName(): noPasswordManager,
                             Optimizer.getName(): noOptimizer,
                             SystemSpeedup.getName(): noSystemSpeedup}

            self.prices = {AviraPrime.getName(): AviraPrime.getPrice(),
                             AntiVirusPRO.getName(): AntiVirusPRO.getPrice(),
                             PhantomVPN.getName(): PhantomVPN.getPrice(),
                             PasswordManager.getName(): PasswordManager.getPrice(),
                             Optimizer.getName(): Optimizer.getPrice(),
                             SystemSpeedup.getName(): SystemSpeedup.getPrice()}

            self.totalCash = totalCash

            self.balance = cardBalance

            VendingMachine.__instance = self

    def getCredit(self):
        return self.credit
    def getNoAviraPrime(self):
        return self.products.get("Avira Prime")
    def getNoAntiVirusPRO(self):
        return self.products.get("Antivirus PRO")
    def getNoPhantomVPN(self):
        return self.products.get("Phantom VPN")
    def getNoPaswordManager(self):
        return self.products.get("Password Manager")
    def getNoOptimizer(self):
        return self.products.get("Optimizer")
    def getNoSystemSpeedup(self):
        return self.products.get("System Speedup")

    def getPriceAviraPrime(self):
        return self.prices.get("Avira Prime")
    def getPriceAntiVirusPRO(self):
        return self.prices.get("Antivirus PRO")
    def getPricePhantomVPN(self):
        return self.prices.get("Phantom VPN")
    def getPricePaswordManager(self):
        return self.prices.get("Password Manager")
    def getPriceOptimizer(self):
        return self.prices.get("Optimizer")
    def getPriceSystemSpeedup(self):
        return self.prices.get("System Speedup")
