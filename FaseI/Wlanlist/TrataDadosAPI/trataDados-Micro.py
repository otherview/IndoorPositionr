from matplotlib.mlab import normpdf
import matplotlib
import numpy
import pylab as p
import buscaValoresMedias




def desenhaGrafico():
    x = numpy.arange(-4, 4, 0.01)
    y = normpdf(x, 0, 1) # unit normal
    p.plot(x,y, color='red', lw=4)
    p.show()


if __name__ == '__main__':
    buscaValoresMedias.init_busca_Valores("listings_dbm_Micro.csv")
    #for bssi in buscaValoresMedias.valores_RSSI:
    bssi ="00:24:C4:2D:1E:00"
    print "Encontrado o AP"
    for pos in buscaValoresMedias.valores_RSSI[bssi][1]:
        powerDbm = buscaValoresMedias.get_media_BSSI_XY(bssi,pos) *(-1.00)
        print str(pos)+ ' '+bssi+' '+buscaValoresMedias.valores_RSSI[bssi][0]+' '+str(powerDbm)
    desenhaGrafico()