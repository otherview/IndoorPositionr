# -*- coding: utf-8 -*-
# Primeiros testes sem refrescamento a cada 1s
#import  TrataDadosAPI.buscaValoresMedias as buscaValoresMedias
#
#Teste ALPHA com refrescamento a cada 1s
import  TrataDadosAPI.buscaValoresMedias_TESTE_ALPHA as buscaValoresMedias

import numpy
import API.AccessPoint as AP
import API.PhysicalAccessPoint as APF
import os.path
import numpy as np
import matplotlib.pyplot as plt
from random import choice
from matplotlib import cm
import colorsys
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg
from pylab import *
import os
import API.PlotWifiHelper as PlotWifiHelper


APFisicos = APF.PhysicalAccessPoint()




def criaAP(bssi,bssi_name):
    
    global APFisicos
    
    apTemp = AP.AccessPoint(bssi_name, bssi[0])
    for position in bssi[1]:
        apTemp.addValues(position,bssi[1][position])
    APFisicos.insert(apTemp)
    
    return




def plotBSSID():

    

    global APFisicos
    
    
    gs = gridspec.GridSpec(2, 2, width_ratios=[2, 1]) 

    ax = plt.subplot(gs[:,0])
    #plt.subplots_adjust(right=0.75)
    

    ax2 = plt.subplot(gs[0,1:])
    #ax3 = plt.subplot(gs[1,1])
    
    #Inicializa o helper de plots
    PlotHelper = PlotWifiHelper.PlotWifiHelper()
    
    #Inicializa um contador de cores
    cor =0
    corArray={}
    plottedAPs={}
    
    #No Rotativity sera sempre o Eixo X
    axisPick = 0 #0 - Eixo X || 1 - Eixo Y
    
    #Mudar os valores axisLimit[0] e axisLimit[1] para definir o espectro a ser desenhado
    axisLimit = [-1,181,-90,0]


    ax.axis(axisLimit)
  
    ax.set_ylabel('Power RSSI')
    ax.set_xlabel('Tempo')
    for bssi in APFisicos.getAPFisicoPerPiso(0,10):
        #Inicializa o sitio para as anotacoes
        annotatePosition=0.0
        if axisPick == 0:
            positions = APFisicos.getPositions(bssi,rangeX=(axisLimit[0],axisLimit[1]),rangeY=(0,1))
        if axisPick == 1:
            positions = APFisicos.getPositions(bssi,rangeX=(0,1),rangeY=(-11,11))
        if positions:
            cor+=1
            corPick = cm.jet(1.*cor/len(APFisicos.getAPFisicoPerPiso(0,10)))
            corArray[APFisicos.getAPName(bssi)]=corPick
            plottedAPs[bssi] = APFisicos.getAPName(bssi)
            
            ax.plot( [ x[axisPick] for x in positions] #tira as posicoes X ou Y AXISPICK 
            , [ APFisicos.getAverage(bssi,x) for x in positions] #tira as avgs de cada posicao
            , color = corPick, linestyle='-', marker="o" , label = APFisicos.getLocation(bssi) )
            
            
            
            for position in positions:
 
                valueBSSI = round(APFisicos.getAverage(bssi,position),2)
                valueVariance = round(APFisicos.getVariance(bssi,position),2)
                
               
                
                if valueVariance :
                    ax.scatter(position[axisPick],valueBSSI,s=valueVariance*20,color=corArray[plottedAPs[bssi]])
                    #ax.annotate("var:"+str(valueVariance),fontsize='xx-small', xy=(position[axisPick], valueBSSI), xytext=(position[axisPick]+0.1, valueBSSI-1.5) )
                    
                
                if annotatePosition != 0 and position[0] != axisLimit[1]-1:
                    if axisPick == 0:
                        previousValueBSSI = round(APFisicos.getAverage(bssi,(position[0]-1,position[1])),2)-valueBSSI
                    else:
                        previousValueBSSI = round(APFisicos.getAverage(bssi,(position[0],position[1]-1)),2)-valueBSSI
                    if previousValueBSSI > 5.0 or previousValueBSSI< -5.0:
                        ax.annotate(str(valueBSSI),fontsize='xx-small', xy=(position[0], valueBSSI), xytext=(position[axisPick]+0.1, valueBSSI+0.5) )
                else:
                    ax.annotate(str(valueBSSI),fontsize='xx-small', xy=(position[0], valueBSSI), xytext=(position[axisPick]+0.1, valueBSSI+0.5) )
                annotatePosition +=1



    img=mpimg.imread(os.path.dirname(__file__) + '\\_Tratamento de Dados\\piso0-tagus.png')
    imgplot1 = ax2.imshow(img)
    #ax2.autoscale_view('tight')
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)
    
    for bssi in plottedAPs:
        
        AP_rect = Rectangle(APFisicos.getLocMap(bssi), 20, 20, facecolor=corArray[plottedAPs[bssi]], edgecolor='black')
        ax2.add_patch(AP_rect)
        AP_linha =  Line2D([240, APFisicos.getLocMap(bssi)[0]], [327, APFisicos.getLocMap(bssi)[1]], lw=2, color=corArray[plottedAPs[bssi]], axes=ax,linestyle='--',linewidth=1000,solid_capstyle="round")
        ax2.add_line(AP_linha)

    
    if axisPick == 0:
        medicao_line = Line2D([240, 250], [327, 365], lw=2, color='green', axes=ax,linestyle='-',linewidth=1000,solid_capstyle="round")
    else:
        medicao_line = Line2D([186, 291], [345, 311], lw=2, color='green', axes=ax,linestyle='-',linewidth=1000,solid_capstyle="round")
    ax2.add_line(medicao_line)
    
    for angleMeasured,angleName in [(0,"0"),(20,"PI/4"),(50,"PI/2"),(70,"3PI/4"),(90,"PI"),(101,"5PI/4"),(121,"3PI/2"),(141,"7PI/4"),(161,"2PI")
        ]:
        ax.plot([angleMeasured, angleMeasured], [-40, -90], 'k-', lw=2,color='green')
        ax.annotate(angleName,fontsize='small', xy=(angleMeasured, -41), xytext=(angleMeasured-1, -39) )
    
   
    #PLT AX3 DA TABELA
   
    #ax3 = PlotHelper.createTable(col_labels = ['col1','col2','col3'],
    #                        table_data = [[11,12,13],[21,22,23],[31,32,33],[11,12,13],[21,22,23],[31,32,33]],
     #                       sub_plot = ax3)
    
    
    
    ax.legend(loc='upper left')
    plt.subplots_adjust(hspace = .001,wspace = 0.02,bottom = 0.01,top = 0.1,left  = 0, right=0.1)
    plt.tight_layout()
    
    plt.figtext(0.1, 0.02, 'Power values are displayed in case of a +/- 5 variance from last measured position, or no value retrieved.')
 
    plt.show()
    #plt.savefig('Medidas-Relative-plot.png')
    return







if __name__ == '__main__':
  
# Primeiros testes sem refrescamento a cada 1s
#buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\_Tratamento de Dados\\listings_dbm_final-FINAL.csv')
#
#Teste ALPHA com refrescamento a cada 1s
    buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\_Tratamento de Dados\\TESTE-ALPHA\\RealTime-Scan-Medicao-Rotatividade.csv')
    for bssi in buscaValoresMedias.valores_RSSI:
        criaAP(buscaValoresMedias.valores_RSSI[bssi],bssi)

    
    plotBSSID()
    
    print "cenas"





