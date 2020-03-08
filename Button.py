import pygame
from Payment import Cash
from VendingMachine import VendingMachine
from plot import plot
import os
# --- class ---

class Button(object):
    def __init__(self, position, size , name , image_path):
        # create 3 images
        self._images = [
            pygame.Surface(size),
            pygame.Surface(size)
        ]

        charImage = pygame.image.load(image_path)
        charImage = charImage.convert()

        self._images[0].blit(charImage,(0,0))
        self._images[1].fill((0,255,0))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        self.name = name

        # select first image
        self._index = 0

    def draw(self, screen):

        # draw selected image
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    #self._index = (self._index+1) % 2 # change image
                    if VendingMachine.getInstance().products[self.name]>=1:
                        VendingMachine.insertProduct(self)
                        VendingMachine.getInstance().products[self.name] -= 1

                    print(self.name)

class PaymentButton(Button):
    payment_method = ""
    def __init__(self,position, size , name , image_path):
        super().__init__(position, size , name , image_path)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self._rect.collidepoint(event.pos):  # is mouse over button
                    #self._index = (self._index + 1) % 2  # change image
                    if self.name == "Cash" and PaymentButton.payment_method !="Cash":
                        PaymentButton.payment_method = "Cash"
                        print(PaymentButton.payment_method)
                    elif self.name == "Cash" and PaymentButton.payment_method =="Cash":
                        PaymentButton.payment_method = ""

                    else:
                        PaymentButton.payment_method = "Card"
                        print(PaymentButton.payment_method)


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400

class Text:
    def __init__(self,text,pos):
        self.pos = pos
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.text = self.font.render(str(text), True, green, blue)

        self.textRect = self.text.get_rect()

        self.textRect.center = (pos)

    def draw(self, screen):
        screen.blit(self.text, self.textRect)

class PriceText(Text):
    def __init__(self,text,pos,size = 20,left = False):
        super().__init__(text,pos)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = self.font.render(str(text), True, green, blue)
        if left == True:
            self.textRect.midleft = pos

class TakeMoney(Text):
    Bani2 = VendingMachine

    def __init__(self, text, pos):
        super().__init__(text, pos)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render(str(text), True, green, blue)
        self.button_rect = self.textRect

    def event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self.button_rect.collidepoint(event.pos):  # is mouse over button
                    VendingMachine.credit.clearMoney()
                    TextButton.requsted_change = False

class CoinsText(Text):
    def __init__(self,text,pos,value):
        super().__init__(text,pos)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render(str(text), True, green, blue)
        self.button_rect = self.textRect
        self.value = value

    def event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self.button_rect.collidepoint(event.pos):  # is mouse over button
                   VendingMachine.credit.insertMoney(self.value)

class TextButton(Text):
    requsted_change = False
    def __init__(self,text,pos):
        super().__init__(text,pos)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render(str(text), True, green, blue)
        self.button_rect = self.textRect

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self.button_rect.collidepoint(event.pos):  # is mouse over button
                    if VendingMachine.credit.getMoney() < VendingMachine.getBasketPrice():
                        print("insufficient funds")
                    else:
                        items = [0] * 6
                        for item in VendingMachine.Basket:
                            if item == "Avira Prime":
                                items[0] += VendingMachine.Basket[item]
                            if item == "System Speedup":
                                items[1] += VendingMachine.Basket[item]
                            if item == "Antivirus PRO":
                                items[2] += VendingMachine.Basket[item]
                            if item == "Password Manager":
                                items[3] += VendingMachine.Basket[item]
                            if item == "Phantom VPN":
                                items[4] += VendingMachine.Basket[item]
                            if item == "Optimizer":
                                items[5] += VendingMachine.Basket[item]
                        pricelist = VendingMachine.getPrices()
                        VendingMachine.readItems()
                        i = 0
                        for value in items:
                            if value != 0:
                                if i == 0:
                                    VendingMachine.itemHistory[i].append(int(VendingMachine.itemHistory[i][-1]) + value * pricelist["Avira Prime"])
                                if i == 1:
                                    VendingMachine.itemHistory[i].append(int(VendingMachine.itemHistory[i][-1]) + value * pricelist["System Speedup"])
                                if i == 2:
                                    VendingMachine.itemHistory[i].append(int(VendingMachine.itemHistory[i][-1]) + value * pricelist["Antivirus PRO"])
                                if i == 3:
                                    VendingMachine.itemHistory[i].append(int(VendingMachine.itemHistory[i][-1]) + value * pricelist["Password Manager"])
                                if i == 4:
                                    VendingMachine.itemHistory[i].append(int(VendingMachine.itemHistory[i][-1]) + value * pricelist["Phantom VPN"])
                                if i == 5:
                                    VendingMachine.itemHistory[i].append(int(VendingMachine.itemHistory[i][-1]) + value * pricelist["Optimizer"])
                            i += 1

                        with open("plot_input.txt", "w") as f:
                            for i in range(6):
                                for value in VendingMachine.itemHistory[i]:
                                    if int(value) != 0:
                                        f.write("%d " % int(value))
                                f.write('\n')
                        VendingMachine.itemHistory = [[],[],[],[],[],[]]
                        VendingMachine.vendorBalance.append(float(VendingMachine.vendorBalance[-1]) + VendingMachine.getBasketPrice())
                        VendingMachine.credit.setMoney(VendingMachine.getInstance().totalCash.getRest(VendingMachine.credit.getMoney(),VendingMachine.getBasketPrice()))
                        VendingMachine.clearBasket()
                        TextButton.requsted_change = True

class PlotText(Text):
    def __init__(self,text,pos):
        super().__init__(text,pos)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render(str(text), True, green, blue)
        self.button_rect = self.textRect

    def event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self.button_rect.collidepoint(event.pos):  # is mouse over button
                   prodplot = plot()
                   prodplot.getProductsPlot('plot_input.txt')
                   prodplot.getPlot(VendingMachine.vendorBalance)
