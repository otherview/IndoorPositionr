import os
def fixpath(path):
    if "\\" in path:
        print "Encontrei"
        if os.name == "posix":
            path = path.replace("\\","/")
    return os.path.abspath(os.path.expanduser(path))

class PhysicalAccessPoint :
    
    
    def __init__(self):
 
        self.physicalAPs = {}
        self.APlocations = self.initAPLocations()
        self.cor =1
        self.color = False
        
    def initAPLocations(self):
        import os
        localizacaoAPS = {}
        
        with open(fixpath(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\APS - MACS.csv')) as infile:
            for line in infile:
                linha = line.strip().split(";")
                localizacaoAPS[linha[0].upper()[:-1]] = {}
                localizacaoAPS[linha[0].upper()[:-1]]['local'] = linha[1]+" "+ linha[4]
                localizacaoAPS[linha[0].upper()[:-1]]['piso'] =linha[5]
                if(linha[6]):
                    localizacaoAPS[linha[0].upper()[:-1]]['mapa'] = (int(linha[6]),int(linha[7]))
                if(linha[8]):
                    localizacaoAPS[linha[0].upper()[:-1]]['mapaWeb'] = (float(linha[8]),float(linha[9]))
                    
               
        return localizacaoAPS
    
    def insert(self, ap):
        if self.physicalAPs.has_key(ap.name()[:-1]):
            #print "ja existe AP Fisico"
            pass
        else:
            self.physicalAPs[ap.name()[:-1]] = {}
        
        if self.physicalAPs[ap.name()[:-1]].has_key(ap.name()):
            #print "Ja existe AP virtual"
            for tmpPosition in ap.getAllValues():
                self.physicalAPs[ap.name()[:-1]][ap.name()].addValues(tmpPosition,ap.getValues(tmpPosition))
        else:
            self.physicalAPs[ap.name()[:-1]][ap.name()] = ap
            if ap.name()[:-1] in self.APlocations:
                self.physicalAPs[ap.name()[:-1]]['location'] = self.APlocations[ap.name()[:-1]]['local']
                self.physicalAPs[ap.name()[:-1]]['piso'] = self.APlocations[ap.name()[:-1]]['piso']
        
        #if self.physicalAPs[ap.name()[:-1]][ap.name()].hasPowerEverywhere():
        #    self.physicalAPs[ap.name()[:-1]][ap.name()]['hasPowerEverywhere'] = True
        #else:
        #    self.physicalAPs[ap.name()[:-1]][ap.name()]['hasPowerEverywhere'] = False
        
        return True
    

    
    def getAPFisicoPerPiso(self, piso, numbAP=10):
        
        APperPiso = []
        
        for ap in self.physicalAPs:
            if self.physicalAPs[ap].has_key('location') and self.physicalAPs[ap].has_key('piso'):
                if self.physicalAPs[ap]['piso'] == str(piso):
                    APperPiso.append(ap)
                    
            
        
        return APperPiso
        
    def getPositions(self,bssi,rangeX=(0,11),rangeY=(0,1)):
        #junta as posicoes em que ha valores
        posicoes =  []
        
        for apBssi in self.physicalAPs[bssi]:
            if not type(self.physicalAPs[bssi][apBssi]) == str :
                for tmpPosicoes in self.physicalAPs[bssi][apBssi].getPositions():
                    if tmpPosicoes[0] in range(rangeX[0],rangeX[1]) and tmpPosicoes[1] in range(rangeY[0],rangeY[1]):
                    
                        if not tmpPosicoes in posicoes:
                            posicoes.append(tmpPosicoes)
        
        return sorted(posicoes)
    
    def getAverage(self, bssi, position):
        import numpy as np
        tmpValores = []
        
        for apBssi in self.physicalAPs[bssi]:
            if not type(self.physicalAPs[bssi][apBssi]) == str :
                tmpvalor = self.physicalAPs[bssi][apBssi].getAverage(position)
                if tmpvalor:
                    tmpValores.append(tmpvalor)
        if tmpValores:
            return np.average(tmpValores)
        else :
            return 0

    def getVariance(self, bssi, position):
        import numpy as np
        tmpValores = []
        
        for apBssi in self.physicalAPs[bssi]:
            if not type(self.physicalAPs[bssi][apBssi]) == str :
                tmpvalor = self.physicalAPs[bssi][apBssi].getVariance(position)
                if tmpvalor:
                    tmpValores.append(self.physicalAPs[bssi][apBssi].getVariance(position))
        if tmpValores:
            return np.average(tmpValores)
        else :
            return 0
        
    def getLocation(self,bssi):
        return self.physicalAPs[bssi]['location']
        
    def getAPName(self,bssi):
        return self.physicalAPs[bssi]['location'].split()[0]
        
    def getAPMultipleNames(self,bssi):
       
        if self.APlocations.has_key(bssi):
            return self.APlocations[bssi]['local']
        tmpNames = []
        for ap in self.getVirtualAPs(bssi):
            tmpNames.append(self.physicalAPs[bssi][ap].getEssid())
        
        return " ".join(tmpNames)
        
    def getLocMap(self,bssi):
        if self.APlocations[bssi].has_key('mapa'):
            return self.APlocations[bssi]['mapa']
        else:
            return (0,0)
    
    def getColor(self, bssi ):
        import sys, colorsys
        from matplotlib import cm
        from colour import Color
        import random
        try:
            if self.color == False:
                self.color =     [Color("#1B0C90"),Color("#502D1B"),Color("#7E492A"),Color("#B4603C"),
                                  Color("#C38B4B"),Color("#D29879"),Color("#E4C7AF"),Color("#FAF5F0"),
                                  Color("#2C6020"),Color("#2E8A51"),Color("#A7B83D"),Color("#94DBAE"),
                                  Color("#3EBB4D"),Color("#1F5C52"),Color("#204860"),Color("#532673"),
                                  Color("#326795"),Color("#993333"),Color("#BB4D3E"),Color("#C34BA3"),
                                  Color("#7E2A66"),Color("#CC0300"),Color("#47000C"),Color("#FF0A33"),
                                  Color("#9F85FF"),Color("#85FFD0"),Color("#160AFF"),Color("#001B85"),
                                  Color("#B6FF94"),Color("#CFFF57"),Color("#EA29FF"),Color("#C7006D"),
                                  Color("#857E00"),Color("#572E00"),Color("#333300"),Color("#330E00")]
                random.shuffle(self.color)

            
            apTmp = ""
            for ap in self.getVirtualAPs(bssi):

                if self.physicalAPs[bssi][ap].getColor() != False:
                    #print "AP -> "+ap+ " Cor -> "+str(self.physicalAPs[bssi][ap].getColor())
                    return self.physicalAPs[bssi][ap].getColor()
                else:
                    i=0
                    
                    cor0 = self.color[self.cor].rgb[0]
                    cor1 = self.color[self.cor].rgb[1]
                    cor2 = self.color[self.cor].rgb[2]
                    while cor0 > 1 or cor1 > 1 or cor2 >1:
                        if cor0 > 1:
                            cor0 += -1
                        if cor1 > 1:
                            cor1 += -1
                        if cor2 > 1:
                            cor2 += -1
                    
                    self.physicalAPs[bssi][ap].setColor((cor0,cor1,cor2,1.0))
                    #self.physicalAPs[bssi][ap].setColor( cm.jet(1.*self.cor/15))   #len(self.APlocations)))
                    apTmp = ap  
                    self.cor+=1
            return self.physicalAPs[bssi][apTmp].getColor()
                
        except Exception:
            print "Exception: getColor() ",sys.exc_info()[0]
            print "Exception in color : "+str(self.color[self.cor])
        
    def getVirtualAPs(self, APphysicalBSSI):
        import API.AccessPoint as AP
        tmpAP =[]
        for ap in self.physicalAPs[APphysicalBSSI]:
            if isinstance(self.physicalAPs[APphysicalBSSI][ap],AP.AccessPoint):
                tmpAP.append(ap)
        return tmpAP
        
    def getKnownAPs(self,position=False ):
        

        tmpAPs = []
        for ap in self.physicalAPs:
            if self.APlocations.has_key(ap):
                if position and self.getAverage(ap,position):
                    tmpAPs.append(ap)
                elif not position:
                    tmpAPs.append(ap)

        return tmpAPs
    
    def saveToCSV(self, file):
        import time
        with open(file,"ab") as f:
            f.write("Saving Info at : "+time.strftime("%H:%M:%S")+"\n")
            for phyBSSI in self.physicalAPs:
                for virBSSI in self.getVirtualAPs(phyBSSI):
                    for posicao in self.physicalAPs[phyBSSI][virBSSI].valores:
                        linewrite = str(phyBSSI)+","+str(virBSSI)+","+str(posicao[0]) + "," +str(posicao[1]) + ","+str(self.physicalAPs[phyBSSI][virBSSI].valores[posicao])+"\n"
                        f.write(linewrite)
                        print linewrite
        print "Info Saved "
        print "cenas"
    
    
    def givePowerGetPositions(self,power,rangePower):
        import API.AccessPoint as AP
        possiblePositions = {}
        
        for ap in self.physicalAPs:
            possiblePositions[ap] = []
            for apBssi in self.physicalAPs[ap]:
                if isinstance(self.physicalAPs[ap][apBssi],AP.AccessPoint):
                    possiblePositions[ap].append( self.physicalAPs[ap][apBssi].givePowerGetPositions(power,rangePower))
            #print possiblePositions
                    #JA TA ITERAR TODOS E DEVOLVER AS POSICOES QUE AQUELE AP TEM AQUELA POTENCIA
        return possiblePositions
    
    def givePowerAndAPsGetPositions(self,ScannedBSSIList,rangePower=1.0):
        import API.AccessPoint as AP
        possiblePositions = {}
        
        for ap in self.physicalAPs:
            for apBssi in self.physicalAPs[ap]:
                if isinstance(self.physicalAPs[ap][apBssi],AP.AccessPoint) and apBssi[:-1] in ScannedBSSIList and len(self.physicalAPs[ap][apBssi].media)==41:
                    possiblePositions[ap] = []
                    
                    position = self.physicalAPs[ap][apBssi].givePowerGetPositions(ScannedBSSIList[apBssi[:-1]],rangePower)
                    possiblePositions[ap].extend(position)
                   
                    #print "AP: "+apBssi+"--> "+str(position) +"\nPower mesured : "+ str(ScannedBSSIList[apBssi[:-1]])+"\n"#+"Power in DB :"
                    print "AP Counted: "+apBssi
        return possiblePositions
                    #JA TA ITERAR TODOS E DEVOLVER AS POSICOES QUE AQUELE AP TEM AQUELA POTENCIA
    
    
    
    
if __name__ == '__main__':
    import AccessPoint as AP
    
    APsFisicos = PhysicalAccessPoint()
    
    cenas = AP.AccessPoint("123123","44444")
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
    APsFisicos.insert(cenas)
    
    cenas2 = AP.AccessPoint("123121","55555")
    APsFisicos.insert(cenas2)
    print APsFisicos.getColor("12312")

    cenas3 = AP.AccessPoint("AAA3","66666")
    APsFisicos.insert(cenas3)
    print APsFisicos.getColor("AAA")
    print "cenas"