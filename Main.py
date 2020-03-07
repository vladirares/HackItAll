from VendingMachine import VendingMachine
from Payment import Cash
from Button import Button,PaymentButton , Text , PriceText
import pygame
import os


Machine = VendingMachine(2,2,2,2,2,2,Cash())
print(Machine.totalCash.getMoney())
Machine.totalCash.insertMoney(1)
Machine.totalCash.insertMoney(1)
print(Machine.totalCash.getMoney())

selectedPaymentOption = ""


pygame.init()
win = pygame.display.set_mode((1000,436))
pygame.display.set_caption("Vending Machine")
x = 50
y = 50
width = 40
height = 60
vel = 5

aviraPrimePath = os.path.join('images', 'aviraPrime.jpg') #93x133
antivirusProPath = os.path.join('images', 'antivirusPro.jpg') #93x132
phantomVPNPath = os.path.join('images', 'phantomVPN.jpg') #93x132
systemSpeedupPath = os.path.join('images', 'systemSpeedup.jpg') #93x133
passwordManagerPath = os.path.join('images', 'passwordManager.png') #93x133
optimizerPath = os.path.join('images', 'optimizer.jpg') #93x133
cashPath = os.path.join('images', 'Cash.jpg') #60x32
cardPath = os.path.join('images', 'Card.jpg') #60x32

aviraPrimeBtn = Button((0, 10), (93, 133),'Avira Prime',aviraPrimePath)
antivirusProBtn = Button((0, 152), (93, 132),'Antivirus PRO',antivirusProPath)
phantomVPNBtn = Button((0, 294), (93, 132),'Phantom VPN',phantomVPNPath)
systemSpeedupBtn = Button((143, 10), (93, 133),'System Speedup',systemSpeedupPath)
passwordManagerBtn = Button((143, 153), (93, 133),'Password Manager',passwordManagerPath)
optimizerBtn = Button((143, 294), (93, 133),'Optimizer',optimizerPath)

NoAviraPrimeText = Text ('x' + str(Machine.getNoAviraPrime()), (113, 72))
NoAntivirusProText = Text ('x' + str(Machine.getNoAntiVirusPRO()), (113, 214))
NoPhantomVPNText = Text ('x' + str(Machine.getNoPhantomVPN()), (113, 357))
NoSystemSpeedupText = Text ('x' + str(Machine.getNoSystemSpeedup()), (256, 72))
NoPasswordManagerText = Text ('x' + str(Machine.getNoPaswordManager()), (256, 214))
NoOptimizerText = Text ('x' + str(Machine.getNoOptimizer()), (256, 357))

PriceAviraPrimeText = PriceText (str(Machine.getPriceAviraPrime())+ '$', (120, 102))
PriceAntivirusProText = PriceText (str(Machine.getPriceAntiVirusPRO())+ '$', (122, 244))
PricePhantomVPNText = PriceText (str(Machine.getPricePhantomVPN())+ '$', (120, 387))
PriceSystemSpeedupText = PriceText (str(Machine.getPriceSystemSpeedup())+ '$', (263, 102))
PricePasswordManagerText = PriceText (str(Machine.getPricePaswordManager())+ '$', (265, 244))
PriceOptimizerText = PriceText (str(Machine.getPriceOptimizer())+ '$', (263, 387))

paymentMethodText = Text ('payment method:',(800,20))
CreditText = PriceText("current credit:"+str(Machine.getCredit())+'$',(500,20))
cashBtn = PaymentButton((670, 50), (60, 32),'Cash',cashPath)
cardBtn = PaymentButton((870, 50), (60, 32),'Card',cardPath)



def redrawGameWindow():

    aviraPrimeBtn.draw(win)
    antivirusProBtn.draw(win)
    phantomVPNBtn.draw(win)
    systemSpeedupBtn.draw(win)
    passwordManagerBtn.draw(win)
    optimizerBtn.draw(win)

    cashBtn.draw(win)
    cardBtn.draw(win)

    NoAviraPrimeText.draw(win)
    NoAntivirusProText.draw(win)
    NoPhantomVPNText.draw(win)
    NoSystemSpeedupText.draw(win)
    NoPasswordManagerText.draw(win)
    NoOptimizerText.draw(win)

    PriceAviraPrimeText.draw(win)
    PriceAntivirusProText.draw(win)
    PricePhantomVPNText.draw(win)
    PriceSystemSpeedupText.draw(win)
    PricePasswordManagerText.draw(win)
    PriceOptimizerText.draw(win)

    paymentMethodText.draw(win)
    if PaymentButton.payment_method == "Cash":
        CreditText.draw(win)


    paymentMethodText.draw(win)



    pygame.display.update()



run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        aviraPrimeBtn.event_handler(event)
        antivirusProBtn.event_handler(event)
        phantomVPNBtn.event_handler(event)
        systemSpeedupBtn.event_handler(event)
        passwordManagerBtn.event_handler(event)
        optimizerBtn.event_handler(event)
        cashBtn.event_handler(event)
        cardBtn.event_handler(event)

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     print(pos)
            # get a list of all sprites that are under the mouse curso

    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    win.fill((0,0,0))

    redrawGameWindow()


#print(Machine.getNoAviraPrime())