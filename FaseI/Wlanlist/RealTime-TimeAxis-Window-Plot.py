import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy as np
import sys
import Tkinter as tk
import time
import API.winWlanApi as wlanAPI
import API.PhysicalAccessPoint as PhyAP
import API.AccessPoint as AP


APsFisicos = PhyAP.PhysicalAccessPoint()



def addMark(key,ax,timeSlot,updateStatus):
    position = timeSlot/1000.0
    if key == 'space':
      print "Marked at position :"+str(position)
      ax.axvline(x=position,marker='D',color='r',linewidth=4)
      return "Marked at position :"+str(position),True
    elif key == 'Escape':
      print 'Getting Ready to save info'
      global APsFisicos
      APsFisicos.saveToCSV("RealTime-Scan.csv")
      return "Saved to File at TimeSlot :"+str(position),True
    elif key == 'Return':
      print 'Paused scanning at :'+str(position)
      if updateStatus :
        return 'Paused scanning at :'+str(position),False
      else:
        return 'Resumed scanning at :'+str(position),True
      
    else :
      return "Tecla "+key+" nao faz nada",True

def gridInitialPlot():
  fig = plt.figure()
  #ax = fig.gca()
  ax = fig.add_subplot(111)
  plt.axis([0, 30, -100, 0])
  
  ax.set_xlabel("Time")
  ax.set_ylabel("Power RSSI")
  
  #fig.patch.set_facecolor('blue')
  #fig.patch.set_alpha(0.7)


  ax.patch.set_facecolor('grey')
  ax.patch.set_alpha(0.5)
  
  return fig,ax

def realTimePlotUpdate(fig, ax, timeSlot):
  import time
  
  class APPlot:
    def __init__(self):
      self.plottedAPs = {}
      self.overlayedAPs = {}
      
    def addAP(self,APFisicoBSSI, name,powerRSSI):
      self.plottedAPs[APFisicoBSSI] = ["line",name,"o"]
      self.overlayedAPs[powerRSSI] = APFisicoBSSI
    
    def isOverlayed(self,APFisicoBSSI, powerRSSI):
      if self.overlayedAPs.has_key(powerRSSI):
        
        if self.overlayedAPs[powerRSSI] == APFisicoBSSI:
          return False
        self.plottedAPs[self.overlayedAPs[powerRSSI]][2] = "D"
        self.overlayedAPs[powerRSSI] = APFisicoBSSI
        self.plottedAPs[self.overlayedAPs[powerRSSI]][2] = "D"
        return self.overlayedAPs[powerRSSI]
      else:
        self.overlayedAPs[powerRSSI] == APFisicoBSSI
        return False
      
    def addPlotedAP(self,APFisicoBSSI,line):
      self.plottedAPs[APFisicoBSSI][0] = line
      
    def getMarker(self,APFisicoBSSI):
      return self.plottedAPs[APFisicoBSSI][2]
    def getName(self,APFisicoBSSI):
      return self.plottedAPs[APFisicoBSSI][1]
      
    def getAllLinesAndNames(self):
      lines = [self.plottedAPs[line][0][0] for line in self.plottedAPs]
      names = [self.plottedAPs[name][1] for name in self.plottedAPs]
      return lines,names
    
    def getNumberPlottedAPs(self):
      return len(self.plottedAPs)
    
  
  lastTimeSlot = timeSlot
  lastPosition = (0,timeSlot/1000.0)
  timeSlot +=1000
  position = (0,timeSlot/1000.0)
  plottedAPS = APPlot()
  
  
  if timeSlot/1000 >= 20:
    ax.xaxis.pan(0.2)

  global APsFisicos
  BSSIs = wlanAPI.get_BSSI()
  for bssi in BSSIs:
    tmpAP = AP.AccessPoint(bssi,BSSIs[bssi][0])
    tmpAP.addValues(position,int(BSSIs[bssi][1]))
    APsFisicos.insert(tmpAP)
    
    
  for apFisico in APsFisicos.getKnownAPs(position): #APsFisicos.physicalAPs:
    tmpPowerRSSI = APsFisicos.getAverage(apFisico,position)
    if tmpPowerRSSI == 0:
      continue
    lastTmpPowerRSSI = APsFisicos.getAverage(apFisico,lastPosition)
    tmpAPNames = APsFisicos.getAPMultipleNames(apFisico)
    plottedAPS.addAP(apFisico,tmpAPNames,tmpPowerRSSI)
    
    if plottedAPS.isOverlayed(apFisico,tmpPowerRSSI):
            
      print "OVERLAY -> "+str(apFisico)+"-> "+str(tmpPowerRSSI)
      
      
    if timeSlot <= 1000:
      tmpPlotIndex  = ax.plot(timeSlot/1000.0, tmpPowerRSSI,
                        marker=plottedAPS.getMarker(apFisico), linestyle='--', color=APsFisicos.getColor(apFisico),
                        label=plottedAPS.getName(apFisico), linewidth=1)
      
      plottedAPS.addPlotedAP(apFisico, tmpPlotIndex)
    else:
      
      tmpPlotIndex = ax.plot([lastTimeSlot/1000.0, timeSlot/1000.0],[lastTmpPowerRSSI, tmpPowerRSSI],
        marker=plottedAPS.getMarker(apFisico), linestyle='-',
        color=APsFisicos.getColor(apFisico), linewidth=1)
      
      plottedAPS.addPlotedAP(apFisico, tmpPlotIndex)
      print "AP: "+str(APsFisicos.getAPMultipleNames(apFisico))+" -- "+str(APsFisicos.getAverage(apFisico,position))
  #print BSSIs
      
  print "Total de APs :"+str(plottedAPS.getNumberPlottedAPs())

  lines,names=plottedAPS.getAllLinesAndNames()
  ax.legend(lines,names,loc= 1,prop={'size':8})

  return fig,timeSlot



class App():
    def key(self,event):
        print('press', event.keysym)
        self.textInput = "Processing..."
        self.labelInput.config(text=self.textInput)
        self.textInput,self.update= addMark(event.keysym,self.ax,self.timeSlot,self.update)
        self.labelInput.config(text=self.textInput)
        

        
        
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.wm_title("Embedding in TK")
        self.frame = tk.Frame(self.root, width=100, height=100)

        self.fig,self.ax = gridInitialPlot()
        self.timeSlot = 0 #(ms) -> 60s = 60000 ms = 300 * 200 ms

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.toolbar = NavigationToolbar2TkAgg( self.canvas, self.root )
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.update = True

        self.label = tk.Label(text="")
        self.textInput = "-----"
        self.labelInput = tk.Label(text = self.textInput)
        
        
        self.frame.bind("<Key>", self.key)
        self.frame.bind("<1>", lambda event: self.frame.focus_set())
                        
        self.frame.pack()
        
        self.labelInput.pack()
        self.label.pack()


        
        self.update_clock()
        self.root.mainloop()

    
    def update_clock(self):
        print "UPDATE CLOCK: "+ time.strftime("%H:%M:%S")
  
        if self.update:
          self.fig,self.timeSlot = realTimePlotUpdate(self.fig,self.ax,self.timeSlot)
          self.canvas.show()
          self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        else:
          print "TA OFF"
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(500, self.update_clock)
        #self.update_clock()

app=App()