#-------------------------------------------------------------------------------
# Name:        Datasetr
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     25/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Datasetr:
    def __init__(self,data):
        self.baseSurvey = {}
        self.loadBaseSurveyDataset(data)


    def loadBaseSurveyDataset(self,data):
        import numpy as np
        self.baseSurvey = {}
        data = data.fileAccess.surveyPoints.surveyPosition
        for pos in data:
            if not self.baseSurvey.has_key(pos):
                self.baseSurvey[pos] = {}
                
            for bssi in data[pos]:
                self.baseSurvey[pos][bssi] = np.asscalar(np.absolute(np.average(data[pos][bssi])))
        
        return
    
    def convertOnePointToDataset(self,data):
        import numpy as np
        tmpDataset = {}
        
        for bssi in data:
            tmpDataset[bssi] = np.asscalar(np.absolute(np.average(data[bssi])))
        
        return tmpDataset
    
    
    
    def loadToDataset(self, data):
        import numpy as np
        self.scannedDataset = {}
        self.scannedDataset[(0,0)] = {}
        tmpDict = {}
        for bssi in data:
            avgPower = np.average(data[bssi])
            if tmpDict.has_key(bssi):
                tmpDict[bssi].update(avgPower)
            tmpDict[bssi] = float(avgPower)
            
        for bssi in tmpDict:
            self.scannedDataset[(0,0)][bssi] = np.asscalar(np.absolute(np.average(tmpDict[bssi])))
        
        return


    def scanToDataset(self, data):
        import numpy as np
        self.scannedDataset = {}
        self.scannedDataset[(0,0)] = {}
        tmpDict = {}
        for bssi in data:
            if tmpDict.has_key(bssi):
                tmpDict[bssi].update(float(data[bssi]))
            tmpDict[bssi] = float(data[bssi][1])
            
        for bssi in tmpDict:
            self.scannedDataset[(0,0)][bssi[:-1]] = np.asscalar(np.absolute(np.average(tmpDict[bssi])))
        
        return

  
def main():
    pass


if __name__ == '__main__':
    main()