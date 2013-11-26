

dicionarioAPS = {}
dicionarioAPSPISO = {}

def initDicionario():
    with open("APS - MACS.csv") as infile:
        for line in infile:
            linha = line.strip().split(";")
            dicionarioAPS[linha[0].upper()] = linha[1]+" "+ linha[4]+" "+linha[5]
            dicionarioAPS[linha[0].upper()[:16]+"1"] = linha[1]+" "+ linha[4]+" "+linha[5]
            dicionarioAPS[linha[0].upper()[:16]+"2"] = linha[1]+" "+ linha[4]+" "+linha[5]
            dicionarioAPSPISO[linha[0].upper()] =linha[5]
            dicionarioAPSPISO[linha[0].upper()[:16]+"1"] =linha[5]
            dicionarioAPSPISO[linha[0].upper()[:16]+"2"] =linha[5]
    
def getAPPiso(AP):
    if dicionarioAPSPISO.get(AP) :
        return "Piso-"+str(dicionarioAPSPISO[AP])
    else:
        return "NAO LISTADO"

def getAP(AP):
    
    if not dicionarioAPS :
        initDicionario()
    print "Procura AP : "+AP
    if dicionarioAPS.get(AP) :
        return str(dicionarioAPS[AP])
    else:
        return "AP NAO LISTADO"

if __name__ == '__main__':
    

    with open("APS - MACS.csv") as infile:
        for line in infile:
            linha = line.strip().split(";")
            dicionarioAPS[linha[0].upper()] = linha[1]+" "+ linha[4]
            print linha
    print "fin"
