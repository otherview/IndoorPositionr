import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
import TrataDadosAPI.buscaValoresMedias_TESTE_ALPHA as buscaValoresMedias
import API.winWlanApi as wlanAPI
import API.AccessPoint as AP
import API.PhysicalAccessPoint as APF


APFisicos = APF.PhysicalAccessPoint()




def criaAP(bssi,bssi_name):
    
    global APFisicos
    
    apTemp = AP.AccessPoint(bssi_name, bssi[0])
    for position in bssi[1]:
        apTemp.addValues(position,bssi[1][position])
    APFisicos.insert(apTemp)
    
    return

#print buscaValoresMedias.valores_GridSplitter_RSSI

class GridAPI :
    def __init__(self ):
        
        self.scannedAPs = {}
        buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\TESTE-ALPHA\\walkAndMesure2-LOG-TESTE-ALPHA-FULL.csv')
        for bssi in buscaValoresMedias.valores_RSSI:
            criaAP(buscaValoresMedias.valores_RSSI[bssi],bssi)
        #APFisicos.givePowerGetPositions(-76)
        self.APsDB = buscaValoresMedias.valores_GridSplitter_RSSI
        self.grid = []
        self.scannedPositions =[]

    def addScannedAPs(self, scanned):

        for bssi in scanned:

            bssid = bssi[:-1]
            if bssi[:-1] == "00:1F:9F:D1:B0:4":
                bssid = "00:0F:F7:B6:86:B"
            if bssi[:-1] == "00:26:44:04:A4:4":
                bssid = "00:11:21:E0:C7:7"
            power = scanned[bssi][1]
            
            self.scannedAPs[bssid] = power
    
    def locateAP(self,range=5):
        self.scannedPositions =APFisicos.givePowerAndAPsGetPositions(self.scannedAPs,rangePower=1.0)
        #print self.scannedPositions
        
    def givePositionsGetGrid(self,gridSplice=4,gridSizeX=(-10,11),gridSizeY=(-10,11)):
        import numpy as np
        
        #inicializar a grelha
        self.grid = []
        for grelha in np.arange(0,gridSplice):
            
            self.grid.append([])
            
        #adicionar positoes na parte da grelha correcta
        for ap in self.scannedPositions:
            for position in self.scannedPositions[ap]:
                if position[0] >=0 and position[1] >=0 :
                    self.grid[0].append(position)
                if position[0] <=0 and position[1] >=0 :
                    self.grid[1].append(position)
                if position[0] <=0 and position[1] <=0 :
                    self.grid[2].append(position)
                if position[0] >=0 and position[1] <=0 :
                    self.grid[3].append(position)
      
        counterPositions = [len(self.grid[0]),len(self.grid[1]),len(self.grid[2]),len(self.grid[3])]
        mostPositions= counterPositions.index(max(counterPositions))
        print "Quadrante 0 : "+str(len(self.grid[0]))
        print "Quadrante 1 : "+str(len(self.grid[1]))
        print "Quadrante 2 : "+str(len(self.grid[2]))
        print "Quadrante 3 : "+str(len(self.grid[3]))
        print " Posicao: "+str(mostPositions)

        return mostPositions
        
        
    
    
    


if __name__ == '__main__':
    
    grid = GridAPI()
    wifiScan = wlanAPI.get_BSSI()
    
    grid.addScannedAPs(wifiScan)
    grid.locateAP()
    grid.givePositionsGetGrid()
    print "cenas"