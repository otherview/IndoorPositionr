#-------------------------------------------------------------------------------
# Name:        DataBasr
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     20/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class DataBasr():
    
    def __init__(self,path= '../../DataBase/'):
        import ContinuousScan as ContinuousScan
        import DataBasrFileAccess as fileAcess
        
        self.path = path
        self.fileAccess = fileAcess.DataBasrFileAccess(self.path)
        self.continuousScan = ContinuousScan.ContinuousScan()
    
        
        return
    
    
    def getSurveyedPositions(self):
    
        return  self.fileAccess.surveyPoints.surveyPosition
        

    def getMeasuredPathPositions(self):
        
        return self.fileAccess.measuredPathPoints.measuredPathPosition

    def updateContinuousScan(self, scan, possiblePositions):
        
        self.continuousScan.updateContinuousScan(scan,possiblePositions)
               
        return
    
    def saveContinuousScan(self):
        
        self.fileAccess.saveContinuousScan(self.continuousScan)
               
        return
    
    def getMeasuredWalkPoints(self):
        
        return self.fileAccess.walkTestPathPoints
    
    
 

def main():
    database = DataBasr()
    
    
if __name__ == '__main__':
    main()
