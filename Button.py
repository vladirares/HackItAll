import pygame
from Payment import Cash
from VendingMachine import VendingMachine
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
                    self._index = (self._index+1) % 2 # change image
                    VendingMachine.insertProduct(self)

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
                    self._index = (self._index + 1) % 2  # change image
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


# ###
# class ProductText(Text):
#     def __init__(self, text, pos):
#         super().__init__(text, pos)
#         self.font = pygame.font.Font('freesansbold.ttf', 20)
#         self.text = self.font.render(str(text), True, green, blue)
# ###

class CoinsText(Text):
    Bani2 = VendingMachine
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
                    TextButton.requsted_change = True


