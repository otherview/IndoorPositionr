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
        import DataBasrFileAccess as fileAcess
        
        self.fileAccess = fileAcess.DataBasrFileAccess(path)
    
        
        return
    
    
    def getSurveyedPositions(self):
    
        return  self.fileAccess.surveyPoints.surveyPosition
        

    def getMeasuredPathPositions(self):
        
        return self.fileAccess.measuredPathPoints.measuredPathPosition


def main():
    database = DataBasr()
    
    
if __name__ == '__main__':
    main()
