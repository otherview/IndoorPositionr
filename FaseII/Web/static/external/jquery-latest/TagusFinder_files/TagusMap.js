//#-------------------------------------------------------------------------------
//# Name:        TagusMap
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     11/10/2013
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------



function TagusMap() {
    
    
    
    this.init = function(){
        this.map = L.map('map').setView([0, 0], 3);
        L.tileLayer('/tiles/{z}_{x}_{y}.jpg', {
        //attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 5
        }).addTo(this.map);

        this.map.markersFixed = [];
        this.map.guessedMarkers = {};
        
        this.accessPoints = new AccessPoints();
        
        this.scanGuessStatus = "stop"
        
        this.metersConvertion = 91037
        this.showMobile = false;
    };
    
    this.showSurveyAccessPoints = function() {
        this.accessPoints.showSurveyAccessPoints();
    }
    
    this.showMeasuredPathAccessPoints = function() {
        this.accessPoints.showMeasuredPathAccessPoints();
    }
    
    this.showScanGuessPosition = function(){
        this.accessPoints.showScanGuessPosition();
    }
        
     
    this.showScanGuessAndLogPosition = function(){
        
        var tempClosure = this
        if (this.scanGuessStatus === "stop"){
            $("#scanGuessStatus").css("background-color","lightgreen");
            $("#buttonContinuousScan").text("Stop Scan")
            this.scanGuessStatus = "active"
            this.time = 0
            this.intervalFunction = setInterval(function() {
                        tempClosure.time +=1
                        $('#statusInfoPosicoesTempo').text( "Posicoes: "+tempClosure.time+" Tempo: "+tempClosure.time+"s")
                        tempClosure.accessPoints.showContinuousScanGuessPosition();
                        
                           
                        }, 1000);
        }else{
            
            $("#scanGuessStatus").css("background-color","lightgrey");
            $("#buttonContinuousScan").text("Scan Guess Position and Log")
            this.scanGuessStatus = "stop"
            clearInterval(this.intervalFunction)
            tempClosure.accessPoints.stopContinuousScanGuessPosition();
        }
        
        
        
    }
    
    
    this.showWalkandGuessPosition = function(){
        
        this.accessPoints.showWalkandGuessPosition();
        
    }
    
    this.showMobilePosition = function(){
        tmpClosure = this;
        if (tagusMap.showMobile == false) {
            tagusMap.showMobile = true;
            $('#showMobilePosition').html("STOP Show Mobile Position");
            tmpClosure.mobileTimer=setInterval(function(){
                tmpClosure.accessPoints.showMobilePositions()},1000);
            
        }else{
            tagusMap.showMobile = false;
            clearInterval(tmpClosure.mobileTimer);
            $('#showMobilePosition').html("Start Show Mobile Position");
            
        }
        

        
    }
    
    this.init();
    };
