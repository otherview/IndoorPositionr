//#-------------------------------------------------------------------------------
//# Name:        AccessPoints
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     23/11/2013
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------


function AccessPoints() {
    
    this.init = function(){
    
    this.surveyedAccessPoints = {}
    this.measuredPathAccessPoints = {}
    this.guessedAccessPoints = {}
    }
    

    this.showSurveyAccessPoints = function() {
        
        var tempClosure = this
        surveyed =  $.getJSON('/_get_surveyed_access_points', {}).done( function(data) {
                        for(ap in data){
                            
                            apPosition = ap.replace("(", "").replace(")", "").split(", ")
                            tempClosure.surveyedAccessPoints[String(apPosition)]= new SingleAcessPoint(apPosition,data[ap])
                                
                            }
                    });
    }
    
    
    this.showMeasuredPathAccessPoints = function() {
    
    
    
        var tempClosure = this
        measured = $.getJSON('/_get_measured_path', {}).done( function(data) {
                            for(ap in data){
                                
                                apPosition = ap.replace("(", "").replace(")", "").split(", ")
                                tempClosure.measuredPathAccessPoints[String(apPosition)] = new MeasuredSingleAccessPoint(apPosition,data[ap])
                            }
        })
    }
    
    
    this.showPossiblePoints = function(lat,lng){
        
        var tempClosure = this
        var guessed =  $.getJSON('/_get_possible_locations', {"lat":lat,"lng":lng}).done( function(data) {
                        for(ap in data){
                            
                            apPosition = data[ap]
                            tempClosure.guessedAccessPoints[String(apPosition)] = new GuessedSingleAcessPoint(apPosition,data[ap])
                                
                            }
                    });
    }
    
    this.init();
    
    }
