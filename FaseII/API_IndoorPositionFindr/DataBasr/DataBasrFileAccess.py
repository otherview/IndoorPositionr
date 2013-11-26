#-------------------------------------------------------------------------------
# Name:        DataBasrFileAccess
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     23/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class DataBasrFileAccess():
    
    def __init__(self,path = '../../DataBase/'):
        
        files = {'survey':'Survey-19_10-35_pos.csv','measurepath':'scan-19-10_caminhada-Tratado.csv'}

        self.surveyPoints = self.loadSurveyPointsFromDataBase(path+files['survey'])
        self.measuredPathPoints = self.loadMeasuredPathPointsFromDataBase(path+files['measurepath'])
        return
    
    def loadSurveyPointsFromDataBase(self,path):
        
        class SurveyPoints():
            def __init__(self):
                self.surveyAccessPoint = {}
                self.surveyPosition = {}
                
            def addAccessPoint(self, accessPoint, position, values):
                if not self.surveyPosition.has_key(accessPoint):
                    self.surveyAccessPoint[accessPoint] = {}
                self.surveyAccessPoint[accessPoint][position] = values
                
                if not self.surveyPosition.has_key(position):
                    self.surveyPosition[position] = {}
                self.surveyPosition[position][accessPoint] = values
                
        tmpSurveyPoints = SurveyPoints()
        
        with open(path,'r') as filename:
            for line in filename:
                accessPointBssi = line.split(",")[:4][1]
                #print "cenas"
                #print line.split(",")[:4][2]
                linha = line.replace("]","").replace("[","").split(",")
                valores = map(int, linha[4:])
                tmpSurveyPoints.addAccessPoint( accessPointBssi, (float(line.split(",")[:4][2]),float(line.split(",")[:4][3])), valores)
        return tmpSurveyPoints

    def loadMeasuredPathPointsFromDataBase(self,path):
        class MeasuredPathPoints():
            def __init__(self):
                self.measuredPathAccessPoint = {}
                self.measuredPathPosition = {}
                
            def addAccessPoint(self, accessPoint, position, values):
                if not self.measuredPathPosition.has_key(accessPoint):
                    self.measuredPathAccessPoint[accessPoint] = {}
                self.measuredPathAccessPoint[accessPoint][position] = values
                
                if not self.measuredPathPosition.has_key(position):
                    self.measuredPathPosition[position] = {}
                self.measuredPathPosition[position][accessPoint] = values
                
        tmpMeasuredPathPoints = MeasuredPathPoints()
        
        with open(path,'r') as filename:
            for line in filename:
                accessPointBssi = line.split(",")[:4][1]
                #print "cenas"
                #print line.split(",")[:4][2]
                linha = line.replace("]","").replace("[","").split(",")
                valores = map(int, linha[4:])
                tmpMeasuredPathPoints.addAccessPoint( accessPointBssi, (float(line.split(",")[:4][2]),float(line.split(",")[:4][3])), valores)
        return tmpMeasuredPathPoints


def main():
    database = DataBasrFileAccess('../../DataBase/')

    print "End of DataBasrFileAccess"
    
if __name__ == '__main__':
    main()