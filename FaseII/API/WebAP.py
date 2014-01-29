#-------------------------------------------------------------------------------
# Name:        WebAP
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     15/10/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
def fixpath(path):
    if "\\" in path:
        print "Encontrei"
        if os.name == "posix":
            path = path.replace("\\","/")
    return os.path.abspath(os.path.expanduser(path))


class WebAP():
    
    
    def __init__(self ):
        import sys
        sys.path.append(fixpath('../../FaseI/Wlanlist'))
        from API import PhysicalAccessPoint as APF
    
        
        self.APFisicos = APF.PhysicalAccessPoint()
        self.APFisicosScanned = APF.PhysicalAccessPoint()

    def getKnownAPsJSON(self ):
        import json
        
        apReturn ={}
        
        for ap in self.APFisicos.APlocations:
            if self.APFisicos.APlocations[ap].has_key('mapaWeb'):
                apTemp = {"apMAC":ap,"mapaWeb":self.APFisicos.APlocations[ap]['mapaWeb'],"local":self.APFisicos.APlocations[ap]['local']}
                apReturn[ap] = apTemp
        
        #print json.dumps(apReturn)
        
        return json.dumps(apReturn)
    
    def getSelfPositionJSON(self ):
        import json
        import sys
        sys.path.append('../../FaseI/Wlanlist')
        from _AppGridSplitter import GridAPI 
        import API.winWlanApi as wlanAPI
        
        grid = GridAPI.GridAPI()
        wifiScan = wlanAPI.get_BSSI()
    
        grid.addScannedAPs(wifiScan)
        grid.locateAP()
        grid.givePositionsGetGrid()
        print "cenas"
        
    
    def scanAreaPosition(self, position ):
        import API.winWlanApi as wlanAPI
        import API.AccessPoint as AP
        import time
        
        print "Started to Scan for 5x1s"
        for i in range(0,1):
            wifiScan = wlanAPI.get_BSSI()
            for bssi in wifiScan:
                apTemp = AP.AccessPoint(bssi, wifiScan[bssi][0])
                apTemp.addValues(position,int(wifiScan[bssi][1]))
                self.APFisicosScanned.insert(apTemp)
            time.sleep(1)
            
        return 
    
    def saveToCSV(self, fileName ):
        self.APFisicosScanned.saveToCSV(fileName)
        return
        
        
    def getSurveyedPositions(self ):
        import sys, os, copy
        sys.path.append(fixpath('../../FaseI/Wlanlist'))
        import TrataDadosAPI.buscaValoresMedias_TESTE_ALPHA as buscaValoresMedias
        buscaValoresMedias.init_busca_Valores(fixpath(os.path.dirname(__file__) + '\\..\\Resultados\\TESTE_BETA\\RAW\\scan-19-10_35_posicoes-Tratado.csv'),gridSplitter=False,webApp=True)
        self.positionsSurveyed = copy.deepcopy( buscaValoresMedias.valores_RSSI)
        self.powersSurveyed = copy.deepcopy( buscaValoresMedias.valores_GridSplitter_RSSI)
        print "cenas"
        tmpReturnArray = {}
        i=0
        for x in self.positionsSurveyed:
            tmpReturnArray[i]={'lat':x[0],'lng':x[1]}
            i+=1
        return tmpReturnArray
    
    def loadMeasuredPath(self ):
        import sys, os, copy
        sys.path.append(fixpath('../../FaseI/Wlanlist'))
        import TrataDadosAPI.buscaValoresMedias_TESTE_ALPHA as buscaValoresMedias
        buscaValoresMedias.init_busca_Valores(fixpath(os.path.dirname(__file__) + '\\..\\Resultados\\TESTE_BETA\\RAW\\scan-19-10_caminhada-Tratado.csv'),gridSplitter=False,webApp=True)
        pointMeasured = copy.deepcopy(buscaValoresMedias.valores_RSSI)
        
        returnPoints = {}
        i=0
        for point in pointMeasured:
            returnPoints[i] = point +(pointMeasured[point],)
            i+=1
        
        self.measuredPath = pointMeasured
        return returnPoints
    
    def getPossibility(self, measuredPoint=None ):
        import Possibility as pos
        import API.winWlanApi as wlanAPI

            
        self.loadMeasuredPath()
        self.possibility = pos.Possibility(self.positionsSurveyed)
        if not measuredPoint:
            
            print "Point : "+str(measuredPoint)
            possibilities = self.possibility.getRecomendation(wlanAPI.get_BSSI() ,scan=True,load=False)
            #possibilities = self.possibility.getRecomendation(self.mesuredPath)
            print "end"
        else:
            print "Point : SCAN"
            possibilities = self.possibility.getRecomendation(self.measuredPath[measuredPoint],scan=False,load=True)
  
        x = [possibilities[p][0] for p in possibilities]
        y = [possibilities[p][1] for p in possibilities]
        centroid = (sum(x) / len(possibilities), sum(y) / len(possibilities))
        possibilities["1"] = centroid+(self.possibility.dataset[(0,0)],)
        
        
        
        return possibilities
    


def main():
    webAP = WebAP()
    #webAP.getKnownAPsJSON()
    #webAP.getSelfPositionJSON()
    #webAP.scanAreaPosition((-5.7908968128719565,-80.15625))
    #webAP.saveToCSV("cenas.csv")
    #webAP.scanAreaPosition((0,1))
    #webAP.saveToCSV("cenas.csv")
    cenas = webAP.loadMeasuredPath()
    webAP.getSurveyedPositions()
    possibilities = webAP.getPossibility()#(-10.1263099801,-82.9663086869))
    print "possibilities"
    return
    
if __name__ == '__main__':
    main()
