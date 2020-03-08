import matplotlib.pyplot as plt

class plot:
    def __init__(self):
       pass

    def getPlot(self,array):
        y=[(i+1) for i in range(len(array))]
        with plt.style.context('dark_background'):
            fig=plt.figure()
            fig.canvas.set_window_title('Vending Machine Balance')
            plt.plot(y,array, 'r-o')
            plt.title('Vending Machine Balance')
            plt.ylabel('Balance')
            plt.xlabel('Number of Transactions')
        plt.show()

    def getProductsPlot(self,fileName):
        f=open(fileName)
        lineIndex=1
        for line in f.readlines():
            if lineIndex==1:
                v1=[int(x) for x in line.split()]
            if lineIndex==2:
                v2=[int(x) for x in line.split()]
            if lineIndex==3:
                v3=[int(x) for x in line.split()]
            if lineIndex==4:
                v4=[int(x) for x in line.split()]
            if lineIndex==5:
                v5=[int(x) for x in line.split()]
            if lineIndex==6:
                v6=[int(x) for x in line.split()]
            lineIndex+=1
        f.close()

        with plt.style.context('dark_background'):
            fig, prod = plt.subplots(2,3)
            for p in prod.flat:
                p.set( ylabel='Income')
            fig.canvas.set_window_title("Products Stats")
            fig.set_size_inches(12,8)
            y = [(i + 1) for i in range(len(v1))]
            prod[0,0].plot(y,v1,'tab:red')
            prod[0,0].set_title("Avira Prime")
            y = [(i + 1) for i in range(len(v2))]
            prod[0,1].plot(y,v2,'tab:red')
            prod[0,1].set_title("Avira System Speedup")
            y = [(i + 1) for i in range(len(v3))]
            prod[0,2].plot(y,v3,'tab:red')
            prod[0,2].set_title("Avira Antivirus Pro")
            y = [(i + 1) for i in range(len(v4))]
            prod[1,0].plot(y,v4,'tab:red')
            prod[1,0].set_title("Avira Password Manager")
            y = [(i + 1) for i in range(len(v5))]
            prod[1,1].plot(y,v5,'tab:red')
            prod[1,1].set_title("Avira Phantom VPN")
            y = [(i + 1) for i in range(len(v6))]
            prod[1,2].plot(y,v6,'tab:red')
            prod[1,2].set_title("Avira Optimization")
            plt.show()
