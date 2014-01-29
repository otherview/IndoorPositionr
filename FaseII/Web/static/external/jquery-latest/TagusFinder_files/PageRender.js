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
this.init = function(){

        if( $('#mobile-element').css('display')=='none') {
            tmpClosure.isMobile = true;       
        }
    
        
     },
    
    this.init();
}