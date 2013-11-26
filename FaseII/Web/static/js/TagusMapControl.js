//#-------------------------------------------------------------------------------
//# Name:        TagusMapControl
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     11/10/2013
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------


function TagusMapControl() {
    
    this.init = function(){
        // Initialize the FeatureGroup to store editable layers
        var drawnItems = new L.FeatureGroup();
        tagusMap.map.addLayer(drawnItems);

        // Initialize the draw control and pass it the FeatureGroup of editable layers
        var drawControl = new L.Control.Draw({
            edit: {
                featureGroup: drawnItems
            }
        });
        tagusMap.map.addControl(drawControl);
        
        //init markersClicked
        tagusMap.map.markersClicked = [];
        
        this.nClickedMarkers = 0;
        
        tagusMap.map.grid = []
        
        tagusMap.map.on('draw:created', function (e) {
        var type = e.layerType,
            layer = e.layer;
            if (type === 'polygon') {
                console.log("cenas");
                console.log(layer);
                polygon = new L.Polygon( layer._latlngs )
                tagusMap.map.grid.push(polygon);
                tagusMap.map.addLayer(polygon);
            }
        });
        
        tagusMap.map.on('click', function(e) {
             var redMarker = L.AwesomeMarkers.icon({
                icon: 'coffee', 
                color: 'red'
            });
            console.log("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng);
            console.log(L.marker([e.latlng.lat,e.latlng.lng]));
            tmpMarker = L.marker([e.latlng.lat,e.latlng.lng], {icon: redMarker, draggable: true}).addTo(tagusMap.map);
            
            tmpMarker.side = 0;
            tmpMarker.order = tagusMapControl.nClickedMarkers;
            tmpMarker.bindPopup("<p> Ponto: "+tmpMarker.order+"</p><button type='button' onclick='console.log(tagusMap.map.markersClicked["+tmpMarker.order+"].scan())'>Measure Point</button>").openPopup();
            
            tagusMapControl.addScanOperationMarker(tmpMarker);
            
            tagusMapControl.nClickedMarkers = tagusMapControl.nClickedMarkers+1;
            
            
            tagusMap.map.markersClicked.push(tmpMarker);
            
            
            
            });
        
        tagusMap.map.markersPossibleLocation = [];
        console.log("acabou o load do control");
    }
    
    
    this.addAPMarker = function(webAP) {
       for(var key in cenas.responseJSON){
            
            tmpMarker = L.marker(cenas.responseJSON[key]['mapaWeb']).addTo(tagusMap.map);
            console.log("created AP: "+cenas.responseJSON[key]['local']+"at : "+cenas.responseJSON[key]['mapaWeb'])
            tagusMap.map.markersFixed.push(tmpMarker);
       }
        
        
    }
    
    this.movePosition = function(latlng){
        var positionMarker = L.AwesomeMarkers.icon({
               icon: 'coffee', 
               color: 'yellow'
           });
        tmpMarker = L.marker(latlng, {icon: positionMarker}).addTo(tagusMap.map);
        
        if (tagusMap.map.markersPosition) {
            tagusMap.map.removeLayer(tagusMap.map.markersPosition[0]);            
        }
        tagusMap.map.markersPosition = [];
        tagusMap.map.markersPosition.push(tmpMarker);
        
    }
    
    this.simpleMovePosition = function(gridPosition){
        
        var polyline = L.polygon([[-3.864254615721396, -34.27734375],[-1.318243056862001, -21.09375],[13.496472765758964, -23.818359375 ],[10.401377554543553, -38.3203125 ],[6.140554782450308, -52.3828125 ],[-1.0546279422758742, -49.39453125 ],[-7.536764322084078, -46.05468749999999 ]], {color: 'red'}).addTo(tagusMap.map);
    
        if (gridPosition === 0) {
            var polyline = L.polygon([[6.664607562172585, -22.8515625 ],[13.496472765758964, -23.818359375 ],[10.401377554543553, -38.3203125 ],[3.8642546157214213, -36.2109375  ]], {color: 'blue'}).addTo(tagusMap.map);
        }else if (gridPosition === 1) {
            var polyline = L.polygon([[10.401377554543553, -38.3203125 ],[6.140554782450308, -52.3828125 ],[-1.0546279422758742, -49.39453125 ],[3.8642546157214213, -36.2109375  ]], {color: 'blue'}).addTo(tagusMap.map);
        }else if (gridPosition === 2) {
            var polyline = L.polygon([[-3.864254615721396, -34.27734375],[3.6888551431470478, -36.73828124999999 ],[-1.0546279422758742, -49.39453125 ],[-7.536764322084078, -46.05468749999999 ]], {color: 'blue'}).addTo(tagusMap.map);
        }else if (gridPosition === 3) {
            var polyline = L.polygon([[-3.864254615721396, -34.27734375],[-1.318243056862001, -21.796875 ],[6.664607562172585, -23.203125],[4.039617826768437, -36.73828124999999 ]], {color: 'blue'}).addTo(tagusMap.map);
        }
    
    }
    
    this.addScanOperationMarker = function(marker){

        marker.scan = function(){
            marker.setIcon(L.AwesomeMarkers.icon({
                icon: 'coffee', 
                color: 'orange'
            }));
            scanned =  $.getJSON('/_get_scan_area', {'lat':marker._latlng.lat,'lng':marker._latlng.lng},
                        function(data) {
                            console.log(data);
                            if (data.scanned) {
                                console.log("ceeeenas");
                            }
                            }).done(function() {
                                console.log( "second success" );
                                marker.setIcon(L.AwesomeMarkers.icon({
                                icon: 'coffee', 
                                color: 'green'
                                }));
                                });
            
        }
    }
    
    
     this.addSurveyedMarkers = function(){
        
        i=0;
        tagusMap.map.markersSurvey = [];
        var positionMarker = L.AwesomeMarkers.icon({
               icon: 'coffee', 
               color: 'orange'
           });
        
        surveyed =  $.getJSON('/_get_survey_scan', {},
                        function(data) {
                            console.log(data);
                            if (data.scanned) {
                                console.log("ceeeenas");
                            }
                            }).done(function(data) {
                                console.log( "second success" );
                                for(var ap in data){
                                    
                                    console.log(data[ap].lat+"  ->  "+ data[ap].lng);
                                   
                                    
                                    tmpMarker = L.marker([data[ap].lat,data[ap].lng], {icon: positionMarker}).addTo(tagusMap.map);
                                    tmpMarker.bindPopup("<b>Marker: "+i +"</b>").openPopup();
                                    tagusMap.map.markersSurvey.push(tmpMarker);
                                    i++
                                };
                                
                                });
        
     }
     
     
     this.addOperationPossibilityFinder  = function(marker){
     
     marker.getPossibility = function(){
        
        var positionMarker = L.AwesomeMarkers.icon({
                  icon: 'coffee', 
                  color: 'red'
              });
        
        
           surveyed =  $.getJSON('/_get_possible_locations', {'lat':marker._latlng.lat,'lng':marker._latlng.lng},
                           function(data) {
                               console.log(data);
                               if (data.scanned) {
                                   console.log("ceeeenas");
                               }
                               }).done(function(data) {
            for(var mark in tagusMap.map.markersPossibleLocation){
            tagusMap.map.removeLayer(tagusMap.map.markersPossibleLocation[mark]);}
                                   console.log( "second success" );
                                   for(var ap in data){
                                       
                                       console.log(ap+"  ->  lat:"+ data[ap][0]+" lng:"+data[ap][1]);
                                   
                                       if(ap === "1"){ positionMarker.options.color = 'orange'; console.log("E ESTE PONTO");}else{ positionMarker.options.color = 'red';  }
                                       tmpMarker = L.marker([data[ap][0],data[ap][1]], {icon: positionMarker}).addTo(tagusMap.map);
                                       tmpMarker.bindPopup("<b>Markers Similarity: "+ap +"</b>").openPopup();
                                       tmpMarker.order = data[ap][2];
                                       tagusMap.map.markersPossibleLocation.push(tmpMarker);
                                       tagusMap.map.addLayer(tmpMarker);
                                       
                                       
                                       };
                                       tmpPolygonPoints = []
                                    //for(var i=0; i<= tagusMap.map.markersPossibleLocation.length; i++){
                                    //    for(point in tagusMap.map.markersPossibleLocation){
                                    //        if(i === tagusMap.map.markersPossibleLocation[point].order){
                                    //            tmpPolygonPoints.push([tagusMap.map.markersPossibleLocation[point]._latlng.lat,tagusMap.map.markersPossibleLocation[point]._latlng.lng]) }}}
                                    //    tmpPolygon = L.polygon(tmpPolygonPoints).addTo(tagusMap.map);
                                        
                                   });
     
        }
     }
     
    this.getPossibleLocation  = function(){
     
     tagusMap.map.markersPossibleLocation = [];
     var positionMarker = L.AwesomeMarkers.icon({
               icon: 'coffee', 
               color: 'red'
           });
        
        surveyed =  $.getJSON('/_get_possible_locations', {'lat':marker._latlng.lat,'lng':marker._latlng.lng},
                        function(data) {
                            console.log(data);
                            if (data.scanned) {
                                console.log("ceeeenas");
                            }
                            }).done(function(data) {
                                console.log( "second success" );
                                for(var ap in data){
                                    
                                    console.log(ap+"  ->  lat:"+ data[ap][0]+" lng:"+data[ap][1]);
                                
                                    tmpMarker = L.marker([data[ap][0],data[ap][1]], {icon: positionMarker}).addTo(tagusMap.map);
                                    tmpMarker.bindPopup("<b>Point Similarity: "+ap +"</b>").openPopup();
                                    
                                    tagusMap.map.markersPossibleLocation.push(tmpMarker);
                                    
                                    };
                                });
     
    }
    
    this.getMeasuredPath  = function(){
     
     tmpMarker = null;
     tagusMap.map.markersMeasuredPath = [];
     var positionMarker = L.AwesomeMarkers.icon({
               icon: 'home', 
               color: 'blue'
           });
        
        surveyed =  $.getJSON('/_get_measured_path', {},
                        function(data) {
                            console.log(data);
                            if (data.scanned) {
                                console.log("ceeeenas");
                            }
                            }).done(function(data) {
                                console.log( "second success" );
                                for(var ap in data){
                                    
                                    console.log(ap+"  ->  lat:"+ data[ap][0]+" lng:"+data[ap][1]);
                                
                                    tmpMarker = L.marker([data[ap][0],data[ap][1]], {icon: positionMarker}).addTo(tagusMap.map);
                                   
                                    console.log(data[ap][2]);
                                    tmpMarker.bindPopup("<p> Ponto Path: "+ap+"</p><button type='button' onclick='console.log(tagusMap.map.markersMeasuredPath["+ap+"].getPossibility())'>Guess Points</button>").openPopup();
                                    tagusMapControl.addOperationPossibilityFinder(tmpMarker);
                                    tagusMap.map.markersMeasuredPath[ap]= tmpMarker;
                                    
                                };
                                
                                });
     
    }
    
    
    this.guessPosition = function(){
        
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
     
    this.initGrid  = function(){
        
        tagusMapControlGrid = new TagusMapControlGrid();
        grid = tagusMapControlGrid.getGrid()
        for (square in grid) {
            var tmpSquare = new L.polygon(grid[square]);
        
            tagusMap.map.addLayer(tmpSquare);
        }
        
    
    }
    
    this.init();
    
    
}