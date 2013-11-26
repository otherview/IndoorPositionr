valores_RSSI={}
#Valores_RSSI  {'BSSI1': ('ESSID1', {(0, 1): [-40,-50,-50], (0, 2): [-40,-50,-50]})}
#Valores_RSSI  {'BSSI1': ('ESSID1', NOME)}
#Valores_RSSI  dict {'BSSID'}
#                       [0] : 'ESSID'
#                       [1] : {(position):valores}
#
#                                  BSSI  Pos   XY    Power DBM
#                   valores_RSSI["BSSI1"][1][(0,2)] = -30
#
#                                  BSSI  ESSID   nome
#                   valores_RSSI["BSSI1"][0]  = eduroam
#PARA ROTATIVIDADE VALOR DE POSICAO x=TEMPO y = 0
#
#
valores_GridSplitter_RSSI={}
#valores_GridSplitter_RSSI  {'BSSI1': {'POWER', [(0, 1), (2, 2)]}}
#valores_GridSplitter_RSSI  {'BSSI1': {'POWER', LISTA_POSICOES_ONDE_HA_ESSE_POWER_DESSE_AP}}
#
#
#                                  BSSI  PowerDB        XY   
#                   valores_RSSI["BSSI1"]['88'] = [(0,2),(0,2),(5,1)] 
#

#
#



def addValue(bssi, essid, position, valores):
    if not valores_RSSI.has_key(bssi):
        valores_RSSI[bssi]=[]
        valores_RSSI[bssi].append("Nao apontei")
        valores_RSSI[bssi].append({})
    valores_RSSI[bssi][1][position] = valores
    
def busca_Valores_Rotatividade(fileCSV):
    with open(fileCSV) as infile:
        for line in infile:
            if not 'Saving Info at' in line:
                linha = line.strip().split(",")
                essid = linha[0]
                bssi = linha[1]
                position = (float(linha[3]),int(linha[2]))
                valores = int( linha[4])
                #print str(bssi)+str(essid)+str(position)+str(valores)
                
                addValue(bssi, essid, position, valores)
       

def busca_Valores_WalkAndMesure(fileCSV):
    with open(fileCSV) as infile:
        for line in infile:
            linha = line.strip().split(",")
            essid = linha[2]
            bssi = linha[2]
            position = (int(linha[0]),int(linha[1]))
            valores = map(int, linha[3:])
            #print str(bssi)+str(essid)+str(position)+str(valores)
            
            addValue(bssi, essid, position, valores)
    return True
   
####################### ---- Buscar Valores para o GridSplitter ---- ##############

def addValue_GridSplitter(bssi, valor, position):
    if not valores_GridSplitter_RSSI.has_key(bssi):
        valores_GridSplitter_RSSI[bssi]={}
    
    if not valores_GridSplitter_RSSI[bssi].has_key(valor):
        valores_GridSplitter_RSSI[bssi][valor] =[]
        
    valores_GridSplitter_RSSI[bssi][valor].append(position)
    
    
    
def busca_Valores_GridSplitter(fileCSV):
    with open(fileCSV) as infile:
        for line in infile:
            linha = line.strip().split(",")

            bssi = linha[2]
            position = (int(linha[0]),int(linha[1]))
            valores = map(int, linha[3:])
            for valorIterator in valores:
                addValue_GridSplitter(bssi[:-1], valorIterator, position)
                
            
            
    return True   
            
####################### ---- Buscar Valores para a WebApp ---- ##############

def addValue_webApp(position, bssi, valores):
    if not valores_RSSI.has_key(position):
        valores_RSSI[position]={}
        
    valores_RSSI[position][bssi]= valores


def busca_Valores_webApp(fileCSV):
    with open(fileCSV) as infile:
        for line in infile:
            line = line.replace("]","").replace("[","")
            linha = line.strip().split(",")

            bssi = linha[1]
            position = (float(linha[2]),float(linha[3]))
            
            valores = map(int, linha[4:])
            for valorIterator in valores:
                addValue_GridSplitter(bssi[:-1], valorIterator, position )
                addValue_webApp(position, bssi[:-1], valores)
            
    return True   



def init_busca_Valores(fileCSV,gridSplitter=False,webApp=False):
    valores_GridSplitter_RSSI.clear()
    valores_RSSI.clear()
    if gridSplitter:
        busca_Valores_GridSplitter(fileCSV)
    elif 'Rotatividade' in fileCSV:
        busca_Valores_Rotatividade(fileCSV)
    elif webApp:
        busca_Valores_webApp(fileCSV)    
    else: 
        busca_Valores_WalkAndMesure(fileCSV)     
    

if __name__ == '__main__':
    import os
    #init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\TESTE-ALPHA\\walkAndMesure2-LOG-TESTE-ALPHA-FULL.csv')
    #init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\TESTE-ALPHA\\RealTime-Scan-Medicao-Rotatividade.csv')
    #init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\TESTE-ALPHA\\walkAndMesure2-LOG-TESTE-ALPHA-FULL.csv',True)
    init_busca_Valores(os.path.dirname(__file__) + '\\..\\..\\..\\FaseII\\Resultados\\TESTE_BETA\\RAW\\scan-19-10_35_posicoes-Tratado.csv',webApp=True)
    
    print "cenas"
    
    
    

