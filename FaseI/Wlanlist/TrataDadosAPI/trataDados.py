import matplotlib.pyplot as plt
from matplotlib.patches import Circle  # $matplotlib/patches.py
import numpy as np
import buscaValoresMedias
import ListaNomesAPs

def circle( xy, radius, color="lightsteelblue", facecolor="none", alpha=1, ax=None ):
    """ add a circle to ax= or current axes
    """
        # from .../pylab_examples/ellipse_demo.py
    e = Circle( xy=xy, radius=radius )
    if ax is None:
        ax = plt.gca()  # ax = subplot( 1,1,1 )
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_edgecolor( color )
    e.set_facecolor( facecolor )  # "none" not None
    e.set_alpha( alpha )
    
def format_float(numb):
    #if numb%1: Nao vale apena por decimas
    #    return "%.2f" % round(numb,2)
    #    
    #else:
        return str(int(numb))
        
def place_anotation(xText,yText):
    return 0
    


X = [i for i in range(-10,11)] + [0 for i in range(-10,11)]
for i in range(1,11):
    X.append(i)
    X.append(i+1)
del X[-5:]

Y = [0 for i in range(-10,11)] + [i for i in range(-10,11)] 
for i in range(-1,-11,-1):
    Y.append(i)
    Y.append(i)
del Y[-5:]



i=0
buscaValoresMedias.init_busca_Valores("listings_dbm_final-FINAL.csv")
for bssi in buscaValoresMedias.valores_RSSI:
    fig = plt.figure()
    fig.patch.set_facecolor("#B2C1E0")
    plt.subplot(111, axisbg='#C8CCDA')
    plt.xlabel('Posicao X Oeste-Este')
    plt.ylabel('Posicao Y Sul-Norte')
    plt.xlim(-11, 11)
    plt.ylim(-11, 11) 
    for pos in buscaValoresMedias.valores_RSSI[bssi][1]:
        powerDbm = buscaValoresMedias.get_media_BSSI_XY(bssi,pos) *(-1.00)
        

        circle(pos, (1- (powerDbm/100.0)) +0.05,color='#000000',facecolor="b",alpha=1.0-powerDbm/100.0 )
        plt.text(pos[0], pos[1],format_float(powerDbm),rotation=0, fontsize='small', color='white', horizontalalignment = 'center',verticalalignment = 'center')
        #ax.annotate(format_float(powerDbm), xy=(pos[0],pos[1]), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
        #print powerDbm/100.0
    plt.scatter(X, Y, 5, facecolors='black', edgecolors='black',color = 'g')
    #plt.title(bssi+' '+buscaValoresMedias.valores_RSSI[bssi][0])
    plt.title(bssi+' '+buscaValoresMedias.valores_RSSI[bssi][0]+' '+ListaNomesAPs.getAP(bssi))
    plt.savefig("resultados_img\\"+ListaNomesAPs.getAPPiso(bssi)+"\\"+bssi.replace(":","-")+"_"+buscaValoresMedias.valores_RSSI[bssi][0]+".png",bbox_inches=0,dpi=250,facecolor=fig.get_facecolor())
    plt.close()
    
    i+=1
    #if i ==3 :
    #    break
    
print "cenas"

#plt.show()