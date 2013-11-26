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
import AP_Relative_Plot_Lib as APRelPlotLib

class gridPlotUpdate:
  
  def __init__(self, ax, starterPosition=(0,-11)):
    self.position = starterPosition
    self.ax = ax
  
  def step(self,key,ax):
    if key == 'Up':
      self.position = (self.position[0],self.position[1]+1)
    elif key == 'Down':
      self.position = (self.position[0],self.position[1]-1)
    elif key == 'Right':
      self.position = (self.position[0]+1,self.position[1])
    elif key == 'Left':
      self.position = (self.position[0]-1,self.position[1])
    else :
      return "Tecla "+key+" nao faz nada"
    
    self.measureBSSI()
    return "Mexeu 1 casa: "+key
  
  def plotPosition(self ):
    print "Position update to "+str(self.position)
    self.ax.plot(self.position[0],self.position[1], marker='D',color='r')
  
  def measureBSSI(self):
    tmpWriteBSSI = {}
    tmpWriteBSSI[self.position[0],self.position[1]] = wlanAPI.get_BSSI_times_and_total_seconds(1,30)
    self.plotPosition()
    with open("walkAndMesure2-LOG.csv","ab") as f:
      for position in tmpWriteBSSI:
        for bssi in tmpWriteBSSI[position]:
          f.write(str(position[0])+","+str(position[1])+","+str(bssi)+","
                  +str(tmpWriteBSSI[position][bssi].getCSVValues()+"\n"))
    return 


def gridInitialPlot():
  fig = plt.figure()
  ax = fig.gca()
  ax = fig.add_subplot(111)
  ax.set_xticks(np.arange(-10,11,1))
  ax.set_yticks(np.arange(-10,11,1))
  
  x = range(-10,11)
  y = range(-10,11)
  plt.plot(x, [0 for i in range(-10,11)], marker='o', linestyle='--', color='b', label='Square')
  plt.plot([0 for i in range(-10,11)],y, marker='o', linestyle='--', color='b', label='Square')
  plt.axis([-12, 12, -12, 12])
  return fig,ax  



class App():
    def key(self,event):
        print('press', event.keysym)
        self.textInput = "Scanning..."
        self.labelInput.config(text=self.textInput)
        import time
        time.sleep(0.5)
        self.textInput = self.plotUpdate.step(event.keysym,self.ax)
        self.labelInput.config(text=self.textInput)
        
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.wm_title("Embedding in TK")
        self.frame = tk.Frame(self.root, width=100, height=100)

        self.fig,self.ax = gridInitialPlot()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.toolbar = NavigationToolbar2TkAgg( self.canvas, self.root )
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label = tk.Label(text="")
        self.textInput = "-----"
        self.labelInput = tk.Label(text = self.textInput)
        self.plotUpdate = gridPlotUpdate(self.ax)
        
        
        self.frame.bind("<Key>", self.key)
        self.frame.bind("<1>", lambda event: self.frame.focus_set())
        
        self.frame.pack()
        self.labelInput.pack()
        self.label.pack()

        
        self.update_clock()
        self.root.mainloop()

    
    def update_clock(self):

        #self.fig = realTimePlot(self.fig,self.ax)
        self.canvas.show()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(200, self.update_clock)

app=App()