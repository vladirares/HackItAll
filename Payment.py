class Payment:
    def __init__(self,cost):
        self.cost = cost

class CashPayment(Payment):
    def __init__(self,cost):
        super().__init__(cost)
        self.money = {0.01:0 , 0.05:0 , 0.1:0,
                         0.25:0 , 0.5:0,
                         1:0 , 2:0 , 5:0 , 10:0 ,
                         20 : 0 , 50 : 0 , 100:0 }

    def insertMoney(self, amount):
        self.money[amount] += 1

    def getMoney(self):
        suma = 0
        for value in self.money.keys():
            suma += value*self.money.keys()[value]
        return suma

class CardPayment(Payment):
    pass
