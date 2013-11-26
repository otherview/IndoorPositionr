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
        
        this.accessPoints = new AccessPoints();
    };
    
    this.showSurveyAccessPoints = function() {
        this.accessPoints.showSurveyAccessPoints();
    }
    
    this.showMeasuredPathAccessPoints = function() {
        this.accessPoints.showMeasuredPathAccessPoints();
    }
    
    this.guessPosition = function(){
        this.accessPoints.
        
        tagusMap.map.markersPossibleLocation = []
        var positionMarker = L.AwesomeMarkers.icon({
               icon: 'home', 
               color: 'blue'
           });
        
                surveyed =  $.getJSON('/_get_guess_position', {},
                        function(data) {
                            if (data.scanned) {
                                console.log("Scanned ok");
                            }
                            }).done(function(data) {
                                console.log( "Recieved full data" );
                                for(var ap in data){
                                    
                                    console.log(ap+"  ->  lat:"+ data[ap][0]+" lng:"+data[ap][1]);
                                
                                    if(ap === "1"){ positionMarker.options.color = 'orange'; console.log("E ESTE PONTO");}else{ positionMarker.options.color = 'red';  }
                                    tmpMarker = L.marker([data[ap][0],data[ap][1]], {icon: positionMarker}).addTo(tagusMap.map);
                                    
                                    tmpMarker.bindPopup("<p> Ponto Path: "+ap+"</p><button type='button' onclick='console.log(tagusMap.map.markersMeasuredPath["+ap+"].getPossibility())'>Measure Point</button>").openPopup();
                                    tagusMapControl.addOperationPossibilityFinder(tmpMarker);
                                    tagusMapControlCompare.addPosition(tmpMarker,data[ap][2]);
                                    tagusMap.map.markersPossibleLocation[ap]= tmpMarker;
                                    
                                    
                                };
                                
                                });
    }
    
    this.init();
    };
