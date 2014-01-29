#-------------------------------------------------------------------------------
# Name:        IndoorPositionr
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     20/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class IndoorPositionr():
    
    
    def __init__(self ):
        
        import DataBasr.DataBasr as DataBasr
        import PositionFindr.PositionFindr as PositionFindr
        self.database = DataBasr.DataBasr('../DataBase/')
        self.positionr = PositionFindr.PositionrFindr(self.database)
        self.mobileData = {}

        return None


    def getSurveyedPositions(self):
        import Jsonr.Jsonr as Jsonr
        
        return Jsonr.prepareSendJsonSurveyedPositions( self.database.getSurveyedPositions() )


  
    def getMeasuredPathPositions(self):
        import Jsonr.Jsonr as Jsonr
        
        return Jsonr.prepareSendJsonSurveyedPositions( self.database.getMeasuredPathPositions() )



    def getLocationPossibility(self,scannedValuesAndBSSI):
        import Jsonr.Jsonr as Jsonr

        return Jsonr.prepareSendJsonSurveyedPositions( self.positionr.getPossibleLocations(scannedValuesAndBSSI) )



    def getLocationPossibilityFromMeasuredPathPoint(self,point):
        import Jsonr.Jsonr as Jsonr
        
        
        return Jsonr.prepareSendJsonSurveyedPositions( self.positionr.getPossibleLocationsFromMeasuredPathPoint(point, self.database.getMeasuredPathPositions() ) )
        
  
    def getLocationPossibilityFromScan(self):
        import Jsonr.Jsonr as Jsonr
        import Wlanr.Wlanr as Wlanr
        
        
        return Jsonr.prepareSendJsonSurveyedPositions( self.positionr.getPossibleLocationsFor( Wlanr.getScan()  ) )
        

    def getLocationPossibilityFromContinuousScan(self):
        import Jsonr.Jsonr as Jsonr
        import Wlanr.Wlanr as Wlanr
        
        tmpScan = Wlanr.getScan()
        positions = self.positionr.getPossibleLocationsFor( tmpScan )
        
        self.database.updateContinuousScan(tmpScan, positions )
        
        return Jsonr.prepareSendJsonSurveyedPositions( positions  )
        


    def stopContinuousScan(self):
        import json
        self.database.saveContinuousScan( )
        
        return json.dumps({200:"OK"})
        
        
    def getPositionsFromTestWalk(self):
        import Jsonr.Jsonr as Jsonr
        
        tmpPositions = {}
        testWalk = self.database.getMeasuredWalkPoints()
        for point in testWalk:

            tmpPositions[point] = self.positionr.getPossibleLocationsFor(testWalk[point]['powerRSSI'])
        
        return Jsonr.prepareSendJsonSurveyedPositions(tmpPositions)

    def add_Mobile_Location_Data(self,mobileData,mobileID ):
        import json
        self.mobileData = {}
        self.mobileData[mobileID] = {}

        for mac in mobileData:
            self.mobileData[mobileID][mac] = mobileData[mac]

        return self.mobileData
    
    def get_Mobile_Location(self):
        import Jsonr.Jsonr as Jsonr
        import json
        
        tmpReturn = {}
        
        for user in self.mobileData:
            tmpLocation = self.positionr.getPossibleLocationsFor(self.mobileData[user])
            tmpReturn[user] = tmpLocation
        
        import logging
        log = logging.getLogger('werkzeug')
        
        log.warning(tmpReturn)
    
        return json.dumps(tmpReturn)
    
     
def main():
    indoorPositionr = IndoorPositionr()
    surveyPoints = indoorPositionr.getSurveyedPositions()
    measuredTestPath = indoorPositionr.getMeasuredPathPositions()
    #possiblePointsFromMeasuredPath = indoorPositionr.getLocationPossibilityFromMeasuredPathPoint((-2.89122818147, -49.2175293434))
    #possiblePointsFromScan = indoorPositionr.getLocationPossibilityFromScan()
    #positionFromTestWalk = indoorPositionr.getPositionsFromTestWalk()
    import json
    data = json.loads('{"00:24:c4:2d:a2:c0":-64,"0c:68:03:49:cc:d0":-66,"00:24:97:fb:d8:e1":-85,"0c:68:03:49:cc:d1":-67,"0c:68:03:4b:cc:c1":-68,"00:17:5a:10:80:c1":-91,"0c:68:03:4b:cc:c0":-67,"0c:68:03:4d:24:21":-86,"0c:68:03:4d:24:20":-86,"48:5b:39:e7:41:41":-93}')
    mobileData = indoorPositionr.add_Mobile_Location_Data(data)
    mobilePosition = indoorPositionr.get_Mobile_Location()
    print indoorPositionr.mobileData
    print mobilePosition
    
    
    
    
    pass
    
    
if __name__ == '__main__':
    main()
