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
        this.marker.bindPopup("<p> Ponto: "+ap+"</p><button type=\"button\" onclick=\"tagusMap.accessPoints.surveyedAccessPoints[\'"+this.position+"\'].drawCircle()\">DrawCircle</button>").openPopup();
                              

    },
    this.drawCircle = function(){
        
        cenas2 = L.circle(this.position,5*tagusMap.metersConvertion).addTo(tagusMap.map)
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


function GuessedSingleAcessPoint(position,values,originalLatLng){
    
    this.init = function(){
    
    this.position = position
    this.values = values
    
    this.showAP()
    }
    
    this.showAP = function(){
 
        var tmpClosure = this
        if (ap == 1.0){color = 'green';
        L.circle(this.position,5*tagusMap.metersConvertion).addTo(tagusMap.map)
        origLatLng = [parseFloat(originalLatLng[0]),parseFloat(originalLatLng[1])];
        tmpPolyLine = L.polyline([origLatLng,this.position], {color: 'red'}).addTo(tagusMap.map);
        dist = L.latLng(origLatLng).distanceTo(L.latLng(this.position))/tagusMap.metersConvertion;
        tmpPolyLine.bindPopup("Distance: "+dist).openPopup();
        console.log(originalLatLng);
        } else{ color = 'orange'}
        var positionMarker = L.AwesomeMarkers.icon({
                            icon: 'home', 
                            color: color
                            });

        this.marker = L.marker(this.position, {icon: positionMarker}).addTo(tagusMap.map);
        this.marker.bindPopup("<p> Ponto: "+ap+"</p>");
                              

    }
    this.init()
}

function MGuessedSingleAcessPoint(position,values,apNumber){
    
    this.init = function(){
    
    this.position = position
    this.values = values
    this.apNumber = apNumber
    console.log(position)
    console.log(apNumber)
    console.log(values)
    
    this.showAP()
    }
    
    this.showAP = function(){
 
        var tmpClosure = this
        if (tmpClosure.values == 1.0){color = 'green'; L.circle(this.position,5*tagusMap.metersConvertion).addTo(tagusMap.map) } else{ color = 'orange'}
        var positionMarker = L.AwesomeMarkers.icon({
                            icon: 'home', 
                            color: color
                            });


        this.marker = L.marker(this.position, {icon: positionMarker}).addTo(tagusMap.map);
        
        if (typeof tagusMap.map.guessedMarkers[String(this.position)] === 'object'){
            var tmpPopup = tagusMap.map.guessedMarkers[String(this.position)]._popup._content
            this.marker.bindPopup(tmpPopup+"<p> Ponto: "+tmpClosure.apNumber+" Semelhanca: "+tmpClosure.values+"</p> ").openPopup();
            
        }else{
            this.marker.bindPopup("<p> Ponto: "+tmpClosure.apNumber+" Semelhanca: "+tmpClosure.values+"</p> <button type=\"button\" onclick=\"tagusMap.map.guessedMarkers[\'"+String(this.position)+"\'].drawCircle()\">Draw Area</button>").openPopup();
        }
        
        tagusMap.map.guessedMarkers[String(tmpClosure.position)] = this.marker
                              

    }
    this.init()
}



function MultipleGuessedSingleAcessPoint(apPointArrayPossiblePositions,ap){
    
    this.init = function(){
    
    this.apList = {}
    for(var point in apPointArrayPossiblePositions){
        tmpAP = new MGuessedSingleAcessPoint(apPointArrayPossiblePositions[point],point,ap)

        this.apList[ap] = tmpAP
        }
    }

    this.init()
}
