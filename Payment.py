class Payment:
    def __init__(self,cost):
        self.cost = cost

class CashPayment(Payment):
    def __init__(self,cost):
        super().__init__(cost)
        self.money = {  0.01:0 , 0.05:0 , 0.1:0,
                        0.25:0 , 0.5:0,
                        1:0 , 2:0 , 5:0 , 10:0 ,
                        20 : 0 , 50 : 0 , 100:0 }

    def insertMoney(self, amount):
        self.money[amount] += 1

    def getMoney(self):
        suma = 0
        dictionar = self.money
        for value in dictionar.keys():
            suma += value*dictionar[value]
        return suma


class CardPayment(Payment):
    pass


class Cash:
    def __init__(self):
        self.money = {0.01: 0, 0.05: 0, 0.1: 0,
                      0.25: 0, 0.5: 0,
                      1: 0, 2: 0, 5: 0, 10: 0,
                      20: 0, 50: 0, 100: 0}

    def setMoney(self,cash):
        self.money=cash

    def clearMoney(self):
        self.money = {0.01: 0, 0.05: 0, 0.1: 0,
                      0.25: 0, 0.5: 0,
                      1: 0, 2: 0, 5: 0, 10: 0,
                      20: 0, 50: 0, 100: 0}

    def insertMoney(self, amount):
        self.money[amount] += 1

    def initTotalMoney(self):
        self.money = {0.01: 50, 0.05: 50, 0.1: 50,
                      0.25: 50, 0.5: 50,
                      1: 100, 2: 50, 5: 50, 10: 50,
                      20: 50, 50: 10, 100: 5}

    def getRest(self,currentcredit,totalcartvalue):
        #merge cu greedy pentru ca singura banconta care nu respecta regula e cea de 20, in rest toate le divid pe cele mai mari
        toreturn=currentcredit-totalcartvalue;
        moneyList=[int(x*100) for x in self.money]
        returnList={}
        i=11
        while toreturn and i>=0:
            x=moneyList[i]
            a=x/100
            if a>=1: a=int(a)
            if self.money[a] and a<=toreturn:
                toreturn-=a
                if a in returnList.keys():
                    returnList[a]+=1
                else:
                    returnList[a]=1
            else:
                i-=1

        return returnList




    def getMoney(self):
        suma = 0
        dictionar = self.money
        for value in dictionar.keys():
            suma += value * dictionar[value]
        return suma