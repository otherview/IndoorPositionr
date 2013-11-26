#-------------------------------------------------------------------------------
# Name:        Position
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     23/10/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Position:
   
    def __init__(self):
        self.possibilities = {}
        self.load_Survey()
        
    
    def load_Survey(self):
        import sys, os
        sys.path.append('../../FaseI/Wlanlist')
        import TrataDadosAPI.buscaValoresMedias_TESTE_ALPHA as buscaValoresMedias
        import Possibility as possiblity
        buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\..\\Resultados\\TESTE_BETA\\RAW\\scan-19-10_35_posicoes-Tratado.csv',gridSplitter=False,webApp=True)
        self.positionsSurveyed = buscaValoresMedias.valores_RSSI
        self.powersSurveyed = buscaValoresMedias.valores_GridSplitter_RSSI
        buscaValoresMedias.valores_RSSI ={}
        buscaValoresMedias.init_busca_Valores(os.path.dirname(__file__) + '\\..\\Resultados\\TESTE_BETA\\PontosMedidos\\1ponto.csv',gridSplitter=False,webApp=True)
        self.pontosTesteMedidos = buscaValoresMedias.valores_RSSI
        
        for position in self.positionsSurveyed:
            tmpPossibility = possiblity.Possibility(position)
            tmpPossibility.add_AP_survey(self.positionsSurveyed[position])
            self.possibilities[position] = tmpPossibility
        
        for measure in self.pontosTesteMedidos:
            for position in self.possibilities:
                self.possibilities[position].get_locating_vector(self.pontosTesteMedidos[measure])
        
        print "cenas"
        


        
        
def main():
    position = Position()
    
if __name__ == '__main__':
    main()