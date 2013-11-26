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

def is_Int(s):
    try: 
        int(s)
        print "erro aqui"
        return ""
    except ValueError:
        return s


def get_BSSI_XY_Powers(bssi,xy):
    if not valores_RSSI[bssi][1].get(xy):
        return []
    return valores_RSSI[bssi][1][xy]

def create_BSSI(bssi,essid):
    if not valores_RSSI.get(bssi):
        if not essid:
            essid = "NO ESSID"
        valores_RSSI[bssi] =[essid,{}]
        return True
    else:
        print "Ja existe "+bssi+" "+essid
        return False

def add_BSSI_XY_Power(bssi,xy,power):
    if not valores_RSSI.get(bssi):
        print "Nao existe "+bssi+" "+essid
        return False
    else:
        if not valores_RSSI[bssi][1].get(xy):
            valores_RSSI[bssi][1][xy] = [power]
        else:
            valores_RSSI[bssi][1][xy].append(power)
        return True

def get_media_BSSI_XY(bssi,xy):
    result = get_BSSI_XY_Powers(str(bssi),xy)
    if not result:
        print "SEM VALORES (BSSID ERRADO ?)"
        return 0
    return (sum(result)/float(len(result)))
 
def init_busca_Valores(fileCSV):   
    with open(fileCSV) as infile:
        for line in infile:
            linha = line.strip().split(",")
            linha.pop()
            is_essid = False
            
            i=0
            xy=(0,0)
            x=0
            y=0
            
            for valor in linha:
                is_power = True
                if is_essid:
                    print "Chama o Create_BSSI"
                    print "Valores = "+bssi+" Nome da REDE :"+valor
                    create_BSSI(bssi,is_Int(str(valor)))
                    is_essid = False
                    is_power = False
                if i == 0:
                    x= int(valor)
                    is_power = False
                if i == 1:
                    y= int(valor)
                    xy =(x,y)
                    is_power = False
                if ":" in valor:
                    bssi = str(valor)
                    is_essid = True
                    is_power = False
                if is_power:
                    print "Power : "+str(valor)
                    add_BSSI_XY_Power(bssi,xy,int(valor))          
                i+=1
            print "Para a posicao "+str(xy)+" "+str(i-2)+" valores"
        
        
if __name__ == '__main__':
    import os
    init_busca_Valores(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\listings_dbm_final-FINAL.csv')
    get_media_BSSI_XY("00:11:F5:86:31:3B",(0,10))
    print minimo