//#-------------------------------------------------------------------------------
//# Name:        SingleAcessPoint
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     23/11/2013
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------


function SingleAcessPoint(position,values) {
    
    this.init = function(){
    
    this.position = position
    this.values = values
    
    this.showAP()
    }
    
    this.showAP = function(){
 
        var positionMarker = L.AwesomeMarkers.icon({
                            icon: 'home', 
                            color: 'blue'
                            });

        this.marker = L.marker(this.position, {icon: positionMarker}).addTo(tagusMap.map);
        this.marker.bindPopup("<p> Ponto: "+ap+"</p>").openPopup();
                              

    }
    
    this.init();
    
    }
    
function MeasuredSingleAccessPoint(position,values){
    
    this.init = function(){
    
    this.position = position
    this.values = values
    
    this.showAP()
    }
    
    this.showAP = function(){
 
        var tmpClosure = this
        var positionMarker = L.AwesomeMarkers.icon({
                            icon: 'home', 
                            color: 'blue'
                            });

        this.marker = L.marker(this.position, {icon: positionMarker}).addTo(tagusMap.map);
        this.marker.bindPopup("<p> Ponto: "+ap+"</p><button type=\"button\" onclick=\"tagusMap.accessPoints.measuredPathAccessPoints[\'"+this.position+"\'].guessPosition()\">Guess Position</button>").openPopup();
                              

    }
    
    
    this.guessPosition = function(){
        lat = this.position[0]
        lng = this.position[1]
        tagusMap.accessPoints.showPossiblePoints(lat,lng)
        

        
    }
    
    this.init();
    
}


function GuessedSingleAcessPoint(position,values){
    
    this.init = function(){
    
    this.position = position
    this.values = values
    
    this.showAP()
    }
    
    this.showAP = function(){
 
        var tmpClosure = this
        if (ap ==1.0){color = 'green'} else{ color = 'red'}
        var positionMarker = L.AwesomeMarkers.icon({
                            icon: 'home', 
                            color: color
                            });

        this.marker = L.marker(this.position, {icon: positionMarker}).addTo(tagusMap.map);
        this.marker.bindPopup("<p> Ponto: "+ap+"</p>").openPopup();
                              

    }
    this.init()
}
