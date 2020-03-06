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

    def __init__(self,noAviraPrime,noAntivirusPRO,noPhantomVPN,noPaswordManager,noOptimizer,noSystemSpeedup,totalCash):
        if VendingMachine.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AviraPrime = Product("Avira Prime",75)
            AntiVirusPRO = Product("Antivirus PRO", 35)
            PhantomVPN = Product("Phantom VPN",50)
            PaswordManager = Product("Password Manager",20)
            Optimizer = Product("Optimizer",10)
            SystemSpeedup = Product("System Speedup",25)

            self.products = {AviraPrime.getName(): noAviraPrime,
                             AntiVirusPRO.getName(): noAntivirusPRO,
                             PhantomVPN.getName(): noPhantomVPN,
                             PaswordManager.getName(): noPaswordManager,
                             Optimizer.getName(): noOptimizer,
                             SystemSpeedup.getName(): noSystemSpeedup}

            self.totalCash = totalCash
            self.credit = 0



            VendingMachine.__instance = self

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