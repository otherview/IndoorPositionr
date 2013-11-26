#-------------------------------------------------------------------------------
# Name:        Jsonr
# Purpose:
#
# Author:      Pedro Gomes
#
# Created:     20/11/2013
# Copyright:   (c) Pedro Gomes 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def prepareSendJsonSurveyedPositions(surveyedPositions):
    import json
    jsonConvert = json.dumps({str(k): v for k, v in surveyedPositions.iteritems()})
    
    return jsonConvert
    
def prepareSendJsonPossibility(possibilityPoints):
    import json
    
    jsonConvert = possibilityPoints
    
    return jsonConvert


def main():
    pass
    
    
if __name__ == '__main__':
    main()
