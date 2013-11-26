import buscaValoresMedias
import numpy
from ..


valores_Bssi_VarAvgPtp = {}
dict_Bssi_AP = {}   #Dict bssi : [bssi]




def agregaAPs():
    for bssi in valores_Bssi_VarAvgPtp:
        bssi_agregado = bssi[:-1]
        
        if not valores_Bssi_agregados.get(bssi_agregado):
            valores_Bssi_agregados[bssi_agregado] = valores_Bssi_VarAvgPtp[bssi]
        else:
            for position in valores_Bssi_agregados[bssi_agregado] :
                valores_Bssi_agregados[bssi_agregado][position]['valores'].append(valores_Bssi_VarAvgPtp[bssi][position]['valores'])
    
        print "cenas"
    return


def calculaVarAvgPtp(bssi,bssi_name):
    global valores_Bssi_VarAvgPtp 
    for position in bssi[1].keys():
        variancia = numpy.var(bssi[1][position])
        media = numpy.average(bssi[1][position])
        difMaximaDeValores = numpy.ptp(bssi[1][position])
        valores = bssi[1][position]
        
        if not valores_Bssi_VarAvgPtp.get(bssi_name):
            valores_Bssi_VarAvgPtp[bssi_name] = {}
        if not valores_Bssi_VarAvgPtp[bssi_name].get(position):
            valores_Bssi_VarAvgPtp[bssi_name][position] = {}
        
        valores_Bssi_VarAvgPtp[bssi_name][position]['var'] = variancia
        valores_Bssi_VarAvgPtp[bssi_name][position]['avg'] = media
        valores_Bssi_VarAvgPtp[bssi_name][position]['ptp'] = difMaximaDeValores
        valores_Bssi_VarAvgPtp[bssi_name][position]['valores'] = valores
        
    
    return




def plotBSSID():
    import numpy as np
    import matplotlib.pyplot as plt
    from random import choice
    import colorsys
    
        
    #Inicializa um vector com cores
    N = 100
    HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    
    t1 = np.arange(-90, 10)
    plt.figure(1)

    plt.axis([0, 11,-90, 0])
    for bssi in valores_Bssi_VarAvgPtp:
        
        cor = choice(RGB_tuples)
        positions = []
        plt.plot( [ x[1] for x in valores_Bssi_VarAvgPtp[bssi].keys()] #tira as posicoes Y 
            , [ valores_Bssi_VarAvgPtp[bssi][x]['avg'] for x in valores_Bssi_VarAvgPtp[bssi].keys()] #tira as avgs de cada posicao
            , color = cor, linestyle='dashed', marker="o")

    plt.show()
    return





if __name__ == '__main__':
    #buscar os valors do dblistings
    #filtrar por valores entre [0,1 e 0,10]
        #atirar valores para um dicionario por AP (3 BSSI para cada AP)
        #fazer a variancia
    #fazer as medias por ponto ? <- faco no fim!
    #fazer o plot da lista
    import os.path
    
    buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\listings_dbm_final-FINAL.csv')
    for bssi in buscaValoresMedias.valores_RSSI:
        calculaVarAvgPtp(buscaValoresMedias.valores_RSSI[bssi],bssi)
    
    agregaAPs()
    
    plotBSSID()