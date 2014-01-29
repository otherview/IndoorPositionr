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
        tempClosure.latLng = [lat,lng]
        var guessed =  $.getJSON('/_get_possible_locations', {"lat":lat,"lng":lng}).done( function(data) {
                        for(ap in data){
                            
                            apPosition = data[ap]
                            tempClosure.guessedAccessPoints[String(apPosition)] = new GuessedSingleAcessPoint(apPosition,data[ap],tempClosure.latLng)
                                
                            }
                    });
    }
    
    this.showScanGuessPosition = function(){
        
        var tempClosure = this
        var scanned = $.getJSON('/_get_scan_position', {}).done( function(data) {
                        for(ap in data){
                            
                            apPosition = data[ap]
                            tempClosure.guessedAccessPoints[String(apPosition)] = new GuessedSingleAcessPoint(apPosition,data[ap])
                                
                            }
                    });
    }
    
    
    this.showContinuousScanGuessPosition = function(){
        
        var tempClosure = this
        var scanned = $.getJSON('/_get_continuous_scan_position', {}).done( function(data) {
                        for(ap in data){
                            
                            apPosition = data[ap]
                            tempClosure.guessedAccessPoints[String(apPosition)] = new GuessedSingleAcessPoint(apPosition,data[ap])
                                
                            }
                    });
    }
    
    
     this.stopContinuousScanGuessPosition = function(){
        var stopContinuousScanGuessPosition = $.getJSON('/_stop_continuous_scan_position', {});
    }
    
    
    this.showWalkandGuessPosition = function(){
        
        var tempClosure = this
        var tmpShowWalkandGuessPosition = $.getJSON('/_get_walk_and_position', {}).done( function(data) {
                        for(ap in data){
                            
                            apPointArrayPossiblePositions = data[ap]
                            console.log("-----------------")
                            console.log(ap)
                            console.log(apPointArrayPossiblePositions)
                            console.log("-----------------")
                            
                            tempClosure.guessedAccessPoints[String(ap)] = new MultipleGuessedSingleAcessPoint(apPointArrayPossiblePositions,ap)
                                
                            }
                    });
    }
    
    
    this.showMobilePositions = function() {
        var tempClosure = this
        var tmpshowMobilePositions = $.getJSON('/_get_mobile_position', {}).done( function(data) {
                        for(ap in data){
                            
                            apPointArrayPossiblePositions = data[ap]
                            console.log("-----------------")
                            console.log(ap)
                            console.log(apPointArrayPossiblePositions)
                            console.log(apPointArrayPossiblePositions)
                            console.log("-----------------")
                            
                            tempClosure.guessedAccessPoints[String(ap)] = new GuessedSingleAcessPoint(apPointArrayPossiblePositions,ap)
                                
                            }
                    });
    }
    this.init();
    
    }
