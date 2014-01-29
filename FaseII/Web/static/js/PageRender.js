//#-------------------------------------------------------------------------------
//# Name:        PageRender
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     20/01/2014
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------



function PageRender() {

this.isMobile = false
tmpClosure = this;
this.debugToggle = false;
this.init = function(){

       $("#DEBUG_DIV").css("display","none")
    
        
     },
    
    this.init();
}

function toggleDebug() {
    if (pageRender.debugToggle){
        $("#DEBUG_DIV").css("display","none")
        pageRender.debugToggle = false;
    }else{
        $("#DEBUG_DIV").css("display","block")
        pageRender.debugToggle = true;
    }
}