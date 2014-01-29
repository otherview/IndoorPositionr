#-------------------------------------------------------------------------------
# Name:        Wlanr
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     20/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def getScan():
    import winWlanApi 
    
    scan = winWlanApi.get_BSSI()
    tmpScan = {}
    
    for bssi in scan:
        tmpScan[bssi] = int(scan[bssi][1])
        
    
    return tmpScan

def main():

    import time
    test = getScan()
    for i in range(0,10):
        time.sleep(1)
        oldTest = test
        test = getScan()
        print "Teste: "+str(i)
        if oldTest == test:
            print "IGUAL"
        else:
            print "DIFERENTE"
        print test
    print "End"
    
if __name__ == '__main__':
    main()
