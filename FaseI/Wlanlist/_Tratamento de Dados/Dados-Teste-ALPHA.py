
class DatabaseValues:
    def __init__(self ):
        self.mainValues = {}
        
    def assureValueExists(self, position,BSSI):
        if not self.mainValues.has_key(position):
            self.mainValues[position] = {}
        
        if not self.mainValues[position].has_key(BSSI):
            self.mainValues[position][BSSI] =[]
    
    def addValues(self, position,BSSI,value):
        self.assureValueExists(position,BSSI)
        self.mainValues[position][BSSI] +=value
    
    def getAllValues(self ):
        return self.mainValues
        
    
    
    
    

if __name__ == '__main__':
    BaseDeDados = DatabaseValues()
    with open("Teste-ALPHA/walkAndMesure2-LOG-FULL-testeALPHA.csv") as f:
        for line in f:
            pline= line.strip().split(",")
            print pline[3:]
            BaseDeDados.addValues((pline[0],pline[1]),pline[2],pline[3:])
    print BaseDeDados.getAllValues()
        
