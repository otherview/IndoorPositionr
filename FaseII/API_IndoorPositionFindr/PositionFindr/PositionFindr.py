#-------------------------------------------------------------------------------
# Name:        PositionFindr
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     20/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class PositionrFindr:
    def __init__(self,data):
        import Datasetr
        
        self.latestPosition = {}
        self.dataset = Datasetr.Datasetr(data)


#Inicializa a data em formato de dataset para processar nos calculos
    def initDataset(self, data):
        import numpy as np
        self.dataset = {}
        for pos in data:
            if not self.dataset.has_key(pos):
                self.dataset[pos] = {}
                
            for bssi in data[pos]:
                self.dataset[pos][bssi] = np.asscalar(np.absolute(np.average(data[pos][bssi])))
    
    
    
    def getPossibleLocations(self,scannedValuesAndBSSI):
        if scan:
            self.scanToDataset(data)
        else:
            self.loadToDataset(data)    
        self.dataset.update(self.scannedDataset)
        #print getRecommendations(self.dataset,(0,0))
        print "top Matches:"
        matches= topMatches(self.dataset,(0,0),n=5,similarity=sim_distance)
        print matches
        returnMatches = {}
        for match in matches:
            
            returnMatches[match[0]] = match[1]+ (self.dataset[match[1]],)
        
        return returnMatches
    

#Vai buscar o ponto medido no caminho, calcula os mais parecidos, o centro e devolve-os
    def getPossibleLocationsFromMeasuredPathPoint(self, point, measuredPathValues):
        
        measuredPointDataset = {}
        measuredPointDataset[(0,0)] = self.dataset.convertOnePointToDataset(measuredPathValues[point])
        tmpBaseDataset = dict(self.dataset.baseSurvey.items() + measuredPointDataset.items())
        
        #print "top Matches:"
        matches= topMatches(tmpBaseDataset,(0,0),n=5,similarity=sim_distance)
        #print matches
        possibilities = self.getCenter(matches)
        
        
        return possibilities
    
    

    def getPossibleLocationsFor(self,scanData):
        """Recebe o ponto, carrega os pontos do survey base, calcula os mais parecidos, o centro e devolve-os """
        scanTreatedData = {}
        for data in scanData:
            scanTreatedData[data.upper().encode('utf-8')] = scanData[data]
        
        scannedPointDataset = {}
        scannedPointDataset[(0,0)] = self.dataset.convertOnePointToDataset(scanTreatedData)
        tmpBaseDataset = dict(self.dataset.baseSurvey.items() + scannedPointDataset.items())
        
        #print "top Matches:"
        matches= topMatches(tmpBaseDataset,(0,0),n=5,similarity=sim_distance)
        #print matches
        possibilities = self.getCenter(matches)
        
        
        return possibilities
  
 
  
#Calcula o centro dos pontos e devolve-os em formato de dictionarios
    def getCenter(self, possibilities):
        
        totalProbs = sum([p[0] for p in possibilities])
        if totalProbs == 0: 
            possibilities.append((1.0,(0,0)))
            tmpPossibilities = {}
            for pos in possibilities:
                tmpPossibilities[pos[0]] = pos[1]
            
            return tmpPossibilities
        
        normalizedPossibilities = {}
        for p in possibilities:
            normalizedPossibilities[p[1]] = p[0]/totalProbs


        x = [p[1][0]*p[0] for p in possibilities]
        totalX = sum(x)/totalProbs
        
        y = [p[1][1]*p[0] for p in possibilities]
        totalY = sum(y)/totalProbs
        
        #x = [p[1][0] for p in possibilities]
        #totalX = sum(x)/len(x)
        #for p in possibilities:
        #
        #    if totalX > p[1][0]:
        #        totalX -= p[0]
        #    if totalX < p[1][0]:
        #        totalX += p[0]

        
        
        #y = [p[1][1] for p in possibilities]
        #totalY = sum(y)/len(y)
        #for p in possibilities:
        #
        #    if totalY > p[1][1]:
        #        totalY -= p[0]
        #    if totalY < p[1][1]:
        #        totalY += p[0]

                    
                    
        centroid = (totalX , totalY)
        possibilities.append((1.0,centroid))
        
        tmpPossibilities = {}
        for pos in possibilities:
            tmpPossibilities[pos[0]] = pos[1]
        
        return tmpPossibilities
  
def main():
    pass
 




################### Funcoes de calculo de posicao ###############

# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
  def check_rules(prefs,si):
    return 
  
  import math
    
        
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]:
        si[item]=1
    

  # if they have no ratings in common, return 0
  if len(si)==0:
    return 0
  print "SI- "+str(len(si))
  
  # Add up the squares of all the differences
  totalSum = 0.0
  for ap in si:
    
    totalSum += pow(prefs[person1][ap]-prefs[person2][ap],2)
    
  totalSum = totalSum/len(si) 
  result = 1/(1+math.sqrt(totalSum))
  
  
  
  ### Add up the squares of all the differences
  #totalSum = 0.0
  #for ap in prefs[person1]:
  #  print prefs[person1][ap]
  #  if not prefs[person2].has_key(ap):
  #      prefsP2 = 0.0
  #  else:
  #      prefsP2 = prefs[person2][ap]
  #  totalSum += pow(prefs[person1][ap]-prefsP2,2)
  #  
  #totalSum = totalSum/len(prefs[person1])/len(si)
  #result = 1/(1+math.sqrt(totalSum))


  return result
    
        




    


# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_distance):
  def sortMatchesRules(scores):
    import numpy as np
    tmpScore = {}
    for score in scores[1:]:
        tmpDistance = np.linalg.norm(tuple(np.subtract(scores[0][1],score[1])))
        #Esquerda
        if scores[0][1][0] > score[1][0] and 0< tmpDistance <10 and not tmpScore.has_key('esquerda'):
            tmpScore['esquerda']= score
            
        #direita
        elif scores[0][1][0] < score[1][0] and 0< tmpDistance <10 and not tmpScore.has_key('direita'):
            tmpScore['direita']= score
            
        elif 5 < tmpDistance <30 and not tmpScore.has_key('outroLado'):
            modScore = (score[0]/pow((4-scores.index(score)),2),score[1])
            tmpScore['outroLado']= modScore
    
    returnMatches = []
    returnMatches.append(scores[0])
    for score in tmpScore:
        returnMatches.append(tmpScore[score])
    
    return returnMatches
        
  
  scores = []
  for other in prefs:
    if other!=person:
        sim = similarity(prefs,person,other)
        #if sim > 0.1:
        scores.append((sim,other)) 
  
  
  scores.sort()
  scores.reverse()
  #cenas = sortMatchesRules(scores)
  return scores[:n]
  
  
    
if __name__ == '__main__':
    main()
    

