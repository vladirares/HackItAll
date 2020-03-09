from VendingMachine import VendingMachine
from Payment import Cash, Card
from Button import Button, CashButton, CardButton
from Button import Text, PriceText, CoinsText, TextButton, TakeMoney, PlotText, PinText, InpText, ErrText, InsText
import pygame
import os

Machine = VendingMachine(10,10,10,10,10,10,Cash(),Card())
print(Machine.totalCash.getMoney())
Machine.totalCash.initTotalMoney()
print(Machine.totalCash.getMoney())
print(Machine.balance.getFunds())

selectedPaymentOption = ""

pygame.init()
win = pygame.display.set_mode((1000,436))
pygame.display.set_caption("Vending Machine")
x = 50
y = 50
width = 40
height = 60
vel = 5

Products = []
Change = []
total = PriceText("Total: "+str(VendingMachine.getBasketPrice())+"$", (315, height+20), 17, True)

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

PriceAviraPrimeText = PriceText (str(Machine.getPriceAviraPrime())+ '$', (120, 102))
PriceAntivirusProText = PriceText (str(Machine.getPriceAntiVirusPRO())+ '$', (122, 244))
PricePhantomVPNText = PriceText (str(Machine.getPricePhantomVPN())+ '$', (120, 387))
PriceSystemSpeedupText = PriceText (str(Machine.getPriceSystemSpeedup())+ '$', (263, 102))
PricePasswordManagerText = PriceText (str(Machine.getPricePaswordManager())+ '$', (265, 244))
PriceOptimizerText = PriceText (str(Machine.getPriceOptimizer())+ '$', (263, 387))

paymentMethodText = Text ('Payment Method:',(800,20))
CreditText = PriceText("Current Credit:"+str(VendingMachine.credit.getMoney())+'$',(500,20))
FundsText = PriceText("Current Credit:"+str(VendingMachine.card.getFunds())+'$',(500,20))
BillsText = PriceText("Insert Money:",(772,110))
ProductsText = PriceText ("Products : ",(400,50))
RestText = PriceText ("Change : ",(570,50))

plotText = PlotText("Display Statistics", (900,400))

cashBtn = CashButton((670, 50), (60, 32),'Cash',cashPath)
cardBtn = CardButton((870, 50), (60, 32),'Card',cardPath)
oneCentBtn = CoinsText("1¢",(690,150),0.01)
fiveCentBtn = CoinsText("5¢",(730,150),0.05)
tenCentBtn = CoinsText("10¢",(780,150),0.1)
twentyFiveCentBtn = CoinsText("25¢",(830,150),0.25)
fiftyCentBtn = CoinsText("50¢",(880,150),0.5)
oneDollarBtn = CoinsText("1$",(690,200),1)
twoDollarBtn = CoinsText("2$",(730,200),2)
fiveDollarBtn = CoinsText("5$",(780,200),5)
tenDollarBtn = CoinsText("10$",(830,200),10)
twentyDollarBtn = CoinsText("20$",(880,200),20)
fiftyDollarBtn = CoinsText("50$",(700,250),50)
oneHundredDollarBtn = CoinsText("100$",(760,250),100)
insfunds = InsText("Insufficient Funds", (450, 300))

pinzero = PinText("0", (800,300), 0)
pinone = PinText("1", (700,250), 1)
pintwo = PinText("2", (800,250), 2)
pinthree = PinText("3", (900,250), 3)
pinfour = PinText("4", (700,200), 4)
pinfive = PinText("5", (800,200), 5)
pinsix = PinText("6", (900,200), 6)
pinseven = PinText("7", (700,150), 7)
pineight = PinText("8", (800,150), 8)
pinnine = PinText("9", (900, 150), 9)
inppin = InpText("Submit PIN", (600,150))
err1 = ErrText("Retry PIN", (830,200))
err2 = ErrText("Insufficient Funds", (830,200))

requestChangeBtn = TextButton("Pay and request change", (860,310))
takeChange = TakeMoney("Take Change", (600, 20))

def redrawGameWindow():
    NoAviraPrimeText = Text('x' + str(Machine.getNoAviraPrime()), (113, 72))
    NoAntivirusProText = Text('x' + str(Machine.getNoAntiVirusPRO()), (113, 214))
    NoPhantomVPNText = Text('x' + str(Machine.getNoPhantomVPN()), (113, 357))
    NoSystemSpeedupText = Text('x' + str(Machine.getNoSystemSpeedup()), (256, 72))
    NoPasswordManagerText = Text('x' + str(Machine.getNoPaswordManager()), (256, 214))
    NoOptimizerText = Text('x' + str(Machine.getNoOptimizer()), (256, 357))

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

    plotText.draw(win)

    paymentMethodText.draw(win)
    if CashButton.payment_method == "Cash":
        CreditText.draw(win)
        BillsText.draw(win)
        oneCentBtn.draw(win)
        fiveCentBtn.draw(win)
        tenCentBtn.draw(win)
        twentyFiveCentBtn.draw(win)
        fiftyCentBtn.draw(win)
        oneDollarBtn.draw(win)
        twoDollarBtn.draw(win)
        fiveDollarBtn.draw(win)
        tenDollarBtn.draw(win)
        twentyDollarBtn.draw(win)
        fiftyDollarBtn.draw(win)
        oneHundredDollarBtn.draw(win)
        requestChangeBtn.draw(win)
        ProductsText.draw(win)
        for product in Products:
            product.draw(win)
        if TextButton.requested_change == True:
            if VendingMachine.credit.getMoney() != 0:
                for rest in Change:
                    rest.draw(win)
                RestText.draw(win)
                takeChange.draw(win)
            else:
                VendingMachine.credit.clearMoney()
                TextButton.requested_change = False

        if VendingMachine.getBasketPrice()>0:
            total.draw(win)
            if InsText.requested_change == True:
                insfunds.draw(win)
    elif CardButton.payment_method == "Card":
        FundsText.draw(win)
        pinzero.draw(win)
        pinone.draw(win)
        pintwo.draw(win)
        pinthree.draw(win)
        pinfour.draw(win)
        pinfive.draw(win)
        pinsix.draw(win)
        pinseven.draw(win)
        pineight.draw(win)
        pinnine.draw(win)
        for product in Products:
            product.draw(win)
        if InpText.requested_change == True:
            inppin.draw(win)
        if VendingMachine.getBasketPrice()>0:
            total.draw(win)
    elif CardButton.payment_method == "Err":
        if ErrText.requested_change1 == True:
            err1.draw(win)
        if ErrText.requested_change2 == True:
            err2.draw(win)

    paymentMethodText.draw(win)
    pygame.display.update()

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        aviraPrimeBtn.event_handler(event)
        antivirusProBtn.event_handler(event)
        phantomVPNBtn.event_handler(event)
        systemSpeedupBtn.event_handler(event)
        passwordManagerBtn.event_handler(event)
        optimizerBtn.event_handler(event)
        cashBtn.event_handler(event)
        cardBtn.event_handler(event)

        plotText.event_handler(event)

        if CashButton.payment_method == "Cash":

            oneCentBtn.event_handler(event)
            fiveCentBtn.event_handler(event)
            tenCentBtn.event_handler(event)
            twentyFiveCentBtn.event_handler(event)
            fiftyCentBtn.event_handler(event)
            oneDollarBtn.event_handler(event)
            twoDollarBtn.event_handler(event)
            fiveDollarBtn.event_handler(event)
            tenDollarBtn.event_handler(event)
            twentyDollarBtn.event_handler(event)
            fiftyDollarBtn.event_handler(event)
            oneHundredDollarBtn.event_handler(event)
            takeChange.event_handler(event)

            requestChangeBtn.event_handler(event)

        if CardButton.payment_method == "Card":
            pinzero.event_handler(event)
            pinone.event_handler(event)
            pintwo.event_handler(event)
            pinthree.event_handler(event)
            pinfour.event_handler(event)
            pinfive.event_handler(event)
            pinsix.event_handler(event)
            pinseven.event_handler(event)
            pineight.event_handler(event)
            pinnine.event_handler(event)
            inppin.event_handler(event)

        if CardButton.payment_method == "Err":
            if ErrText.requested_change1 == True:
                err1.event_handler(event)
            else:
                err2.event_handler(event)

    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    if CashButton.payment_method == "Cash":
        CreditText = PriceText("Current Credit:"+str(VendingMachine.credit.getMoney())+'$',(500,20))

    if CardButton.payment_method == "Card":
        FundsText = PriceText("Current Credit:"+str(VendingMachine.card.getFunds())+'$',(500,20))
    
    Products = []
    height = 80
    if Machine.getBasket() != "":
        lines = Machine.getBasket().split("/n")
        for line in lines:
            Products.append(PriceText(line, (315, height),14,True))
            height += 25
        total = PriceText("Total: "+str(VendingMachine.getBasketPrice())+"$", (315, height+20), 17, True)
    
    Change = []
    changeDict = Machine.totalCash.getRest(VendingMachine.credit.getMoney(),VendingMachine.getBasketPrice())
    changeLines = []
    for note in changeDict.keys():
        changeLines.append(str(changeDict[note])+" x "+str(note))
    height2 = 80
    for change in changeLines:
        Change.append(PriceText(change, (500, height2),14,True))
        height2 += 25
    takeChange = TakeMoney("Take Change" , (600, height2 + 20))

    win.fill((0,0,0))
    redrawGameWindow()
pygame.quit()
