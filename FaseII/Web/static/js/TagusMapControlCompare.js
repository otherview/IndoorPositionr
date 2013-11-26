//#-------------------------------------------------------------------------------
//# Name:        TagusMapControlCompare
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     13/11/2013
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------
function TagusMapControlCompare() {

    this.init = function(){
    this.compareMarker = {};
    this.comparePower = {}
    
    }
    
    this.addPosition = function(marker,recv_ap){
        
        console.log("TagusMapControlCompare: marker: "+marker);
        console.log(marker);
        console.log("TagusMapControlCompare: recv_ap: "+recv_ap);
        console.log(recv_ap);
        tagusMapControlCompare.compareMarker[[marker._latlng.lat,marker._latlng.lng]] = recv_ap;
    }
    
    this.makeComparisonTable = function (){
        var addTableValue = "";
        var addTableHeader = "<tr>";
        for (var ap in tagusMapControlCompare.compareMarker) {
            addTableHeader += "<th> "+ap+" </th>";
            
            for (var power in tagusMapControlCompare.compareMarker[ap]) {
                addTableValue += "<td> "+power +"</td><td>"+tagusMapControlCompare.compareMarker[ap][power]+"</td>";
            }
            
        }
        addTableHeader +="</tr>"+addTableValue+"</tr>";
        
        
        
        
        $("#table-compare").append(addTableHeader);
     
    }
    this.init();
}