#-------------------------------------------------------------------------------
# Name:        ContinuousScan
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     26/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class ContinuousScan():
    def __init__(self):
        self.counter = 0
        self.continuousScan = {}
        
        
    def updateContinuousScan(self, scan, possiblePositions):
        self.counter += 1
        self.continuousScan[self.counter] = {}
        self.continuousScan[self.counter]['scan'] = scan
        self.continuousScan[self.counter]['possiblePositions'] = possiblePositions
        
        

def main():
    return
    
    
if __name__ == '__main__':
    main()
