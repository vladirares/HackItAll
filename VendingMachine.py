from Product import Product
from Payment import Cash

class VendingMachine:
    """
    this class is a singleton
    """
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if VendingMachine.__instance == None:
            VendingMachine()
        return VendingMachine.__instance

    def __init__(self, noAviraPrime, noAntivirusPRO, noPhantomVPN, noPasswordManager, noOptimizer, noSystemSpeedup, totalCash):
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
            self.credit = 0



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
