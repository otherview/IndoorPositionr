import matplotlib

class PlotWifiHelper:
    'Class with some standart functions to help plotting'
    
    
    def __init__(self ):
        self.table_data = []
        self.col_labels = []
        self.tableInfo = {}
        self.cell_colors = []
        
    
    
    def createTable(self, sub_plot):
    
        
            sub_plot.axes.get_xaxis().set_visible(False)
            sub_plot.axes.get_yaxis().set_visible(False)
            sub_plot.axis('off')
            
            table_data = self.getTableData()
            
            
            
            the_table = sub_plot.table(cellText=self.table_data,
                          colLabels=self.col_labels,
                          loc='center',
                          cellColours=self.cell_colors
                          )
            the_table.auto_set_font_size(False)
            the_table.set_fontsize(9)
            #the_table.scale(2, 2)
        
        #    col_labels=['col1','col2','col3']
        #    row_labels=['row1','row2','row3']
        #    table_vals=[[11,12,13],[21,22,23],[31,32,33],[11,12,13],[21,22,23],[31,32,33]]
            
            return sub_plot
        

        
    def addColumnValue(self, bssi, position, value):
        if self.tableInfo.has_key(bssi):
            self.tableInfo[bssi][position]= value
        else:
            self.tableInfo[bssi]={}
            self.tableInfo[bssi][position] = value
        
        
    def getTableData(self ):
        
        for bssi in self.tableInfo:
            for position in self.tableInfo[bssi]:
                print str(bssi)+" - "+str(position[1])+" : "+str(self.tableInfo[bssi][position])
            top5Variance =sorted(self.tableInfo[bssi], key= self.tableInfo[bssi].__getitem__,
                                 reverse=True)[:3]
            
            if len(top5Variance)<3:
                for count in range(0,3-len(top5Variance)):
                    top5Variance.append('nil')
            colorRow =[]
            for newCount in range(0,3):
                colorRow.append("red")   
            self.table_data.append(top5Variance)
            self.col_labels.append(bssi)
            self.cell_colors.append(colorRow)

        
    
    
    
    
