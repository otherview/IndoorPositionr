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
        
  

def main():
    indoorPositionr = IndoorPositionr()
    surveyPoints = indoorPositionr.getSurveyedPositions()
    measuredTestPath = indoorPositionr.getMeasuredPathPositions()
    possiblePointsFromMeasuredPath = indoorPositionr.getLocationPossibilityFromMeasuredPathPoint((-2.89122818147, -49.2175293434))
    pass
    
    
if __name__ == '__main__':
    main()
