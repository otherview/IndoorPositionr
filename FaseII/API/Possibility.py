#-------------------------------------------------------------------------------
# Name:        Possibility
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     23/10/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  from math import sqrt
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
  
  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)

    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
	    
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]

class Possibility:
   
    def __init__(self, data ):
        
        self.initDataset(data)
    
    def initDataset(self, data):
        import numpy as np
        self.dataset = {}
        for pos in data:
            if not self.dataset.has_key(pos):
                self.dataset[pos] = {}
                
            for bssi in data[pos]:
                self.dataset[pos][bssi] = np.asscalar(np.absolute(np.average(data[pos][bssi])))
                
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
        
        
    
    
    def getRecomendation(self, data,scan=True,load=False ):
        if scan:
            self.scanToDataset(data)
        else:
            self.loadToDataset(data)    
        self.dataset.update(self.scannedDataset)
        #print getRecommendations(self.dataset,(0,0))
        print "top Matches:"
        matches= topMatches(self.dataset,(0,0),n=5,similarity=sim_pearson)
        print matches
        returnMatches = {}
        for match in matches:
            
            returnMatches[match[0]] = match[1]+ (self.dataset[match[1]],)
        
        return returnMatches
    
            
        
        
        
# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1

  # if they have no ratings in common, return 0
  if len(si)==0: return 0

  # Add up the squares of all the differences
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                      for item in prefs[person1] if item in prefs[person2]])

  return 1/(1+sum_of_squares)
    
        
# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  from math import sqrt
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
  
  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_distance):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)

    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
	    
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

# Returns the best matches for person from the prefs dictionary. 
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]


def main():
    possible = Possibility((0,0))
    
if __name__ == '__main__':
    main()