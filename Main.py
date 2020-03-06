from VendingMachine import VendingMachine
from Payment import Cash
#import pygame


Machine = VendingMachine(2,2,2,2,2,2,Cash())
print(Machine.totalCash.getMoney())
Machine.totalCash.insertMoney(1)
Machine.totalCash.insertMoney(1)
print(Machine.totalCash.getMoney())


#print(Machine.getNoAviraPrime())