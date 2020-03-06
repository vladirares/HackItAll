from VendingMachine import VendingMachine
from Payment import CashPayment
masina = VendingMachine(2,2,2,2,2,2)

plata = CashPayment(20)
print(plata.getMoney())

plata.insertMoney(1)
print(plata.getMoney())


print(masina.getNoAviraPrime())