class AccessPoint:

    #Base comum para todos os APS

    
    def __init__(self, bssi, essid):

        self.bssi = str(bssi)
        self.essid = str(essid)
        self.valores = {}
        self.variancia = {}
        self.media = {}
        self.ptp = {}
        self.color = False
        
    def addValues(self, position,values):
        import numpy as np
        if self.valores.get(position):
            self.valores[position].extend(values)
        else:
            if isinstance(values,int):
                self.valores[position] = [values]
            else:
                self.valores[position] = values
        
        if isinstance(values,int):
            self.variancia[position] = np.var([values])
            self.media[position] = np.average([values])
            self.ptp[position] = np.ptp([values])
        else:
            self.variancia[position] = np.var(values)
            self.media[position] = np.average(values)
            self.ptp[position] = np.ptp(values)
        return True



    def name(self):
        #print "BSSI : "+ str(self.bssi)+" ESSID: "+ str(self.essid)
        return self.bssi

    def printValues(self, position = False):
        if not position:
            for i in self.valores:
                print self.valores[i]
        else:
            print self.valores[position]
    
    def printVariance(self, position = False):
        if not position:
            for i in self.media:
                print self.media[i]
        else:
            print self.media[position]

    def printAverage(self, position = False):
        if not position:
            for i in self.variancia:
                print self.variancia[i]
        else:
            print self.variancia[position]
 
    def printPointToPoint(self, position = False):
        if not position:
            for i in self.ptp:
                print self.ptp[i]
        else:
            print self.ptp[position]
            
    def getPositions(self):
        return self.valores.keys()

    def getAverage(self,position):

        if self.media.has_key(position):
            return self.media[position]
        else:
            return

    def getVariance(self,position):
        if self.variancia.has_key(position):
            return self.variancia[position]
        else:
            return
    
    def getVarTotEntrePosicoes(self, bssi, positions ):
        for position in positions:
            if self.variancia.has_key(position):
                
                return self.variancia[position]
            else:
                return
    def getAllValues(self):
        return self.valores
    
    def getValues(self, position):
        if self.valores.has_key(position):
            return self.valores[position]
        else:
            print "Nao ha valores na posicao : "+str(posicao)
            return 
            
    def setColor(self, color):
        self.color = color
    
    def getColor(self ):
            return self.color
        
    def getEssid(self ):
        return self.essid
    
    def givePowerGetPositions(self, power, rangePower):
        import numpy as np
        positions = []
        power=float(power)
        for posicao in self.media:
            if round(self.media[posicao]) in np.arange(float(power-rangePower),float(power+rangePower)):
                #Pede todos os aps que tem este power
                #print "AP: "+self.bssi+"--> "+str(posicao) +"Power DB: "+ str(round(self.media[posicao]))+" Power mesured -->"+str(power)
                
                positions.append(posicao)
        
        return positions

            
    def hasPowerEverywhere(self ):
        print "Contagem de Posicoes: "+self.name()+" -> "+ str(len(self.media))
        if len(self.media) == 41:
            return True
        return False
    
    
    
if __name__ == '__main__':
        
    cenas = AccessPoint("123123","44444")
    cenas.name()
    cenas.addValues((0,0),[-1,-2,-3,-4])
    cenas.addValues((0,1),[-9,-8,-7,-6])
    cenas.printValues()
    cenas.name()
    cenas.printValues((0,0))
    cenas.printAverage()
    cenas.printPointToPoint((0,0))
    cenas.printVariance((0,1))
    cenas.addValues((0,0),[-9,-8,-7,-6])
    cenas.printValues((0,0))
    print "cenas"