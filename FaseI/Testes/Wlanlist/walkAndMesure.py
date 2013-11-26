__author__ = 'Pedro Gomes'
import winWlanApi
import numpy as np




if __name__ == '__main__':
    print "--- Medidor de wlans --- \n GRELHA 10x10 \n"
    import matplotlib.pyplot as plt
    import sys

    position = [0,-11]
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    if len(sys.argv) == 3:
        position[0] = int(sys.argv[1])
        position[1] = int(sys.argv[2])
    print "Comecar na posicao x = "+str(position[0])+" y="+str(position[1])
    
    
    
    def press(event):
        print('press', event.key)
        BSSI_position = {}
        if event.key=='up':
            visible = xl.get_visible()
            xl.set_visible(not visible)
            position[1] = position[1]+1
            print "Position update to "+str(position)
            ax.plot(position[0], position[1], marker='D',color='r')
            fig.canvas.draw()
            
        if event.key=='down':
            visible = xl.get_visible()
            xl.set_visible(not visible)
            position[1] = position[1]-1
            print "Position update to "+str(position)
            ax.plot(position[0], position[1], marker='D',color='r')
            fig.canvas.draw()
            
        if event.key=='left':
            visible = xl.get_visible()
            xl.set_visible(not visible)
            position[0] = position[0]-1
            print "Position update to "+str(position)
            ax.plot(position[0], position[1], marker='D',color='r')
            fig.canvas.draw()
            
        if event.key=='right':
            visible = xl.get_visible()
            xl.set_visible(not visible)
            position[0] = position[0]+1
            print "Position update to "+str(position)
            ax.plot(position[0], position[1], marker='D',color='r')
            fig.canvas.draw()
            
        BSSI_position[position[0], position[1]] = winWlanApi.get_BSSI_times_and_total_seconds(2,30)
        with open("listings_dbm.csv","a") as file:
            for keyX,keyY in BSSI_position:
                file.write(str(keyX)+","+str(keyY)+",")
                for bssi in BSSI_position[keyX,keyY]:
                    file.write(str(bssi)+","+str(BSSI_position[keyX,keyY][bssi][0][0])+",")
                    for value in BSSI_position[keyX,keyY][bssi]:
                        file.write(str(value[1])+",")
                file.write("\n")
        BSSI_position.clear()
        print "Medicao feita e guardada!"


    x = range(-10,11)
    y = range(-10,11)

    fig = plt.figure()
    ax = fig.gca()
    ax = fig.add_subplot(111)
    ax.set_xticks(np.arange(-10,11,1))
    ax.set_yticks(np.arange(-10,11,1))

    plt.plot(x, [0 for i in range(-10,11)], marker='o', linestyle='--', color='b', label='Square')
    plt.plot([0 for i in range(-10,11)],y, marker='o', linestyle='--', color='b', label='Square')
   # plt.plot(0,0,marker='o',color='g')
    plt.axis([-12, 12, -12, 12])


    fig.canvas.mpl_connect('key_press_event', press)
    xl = ax.set_xlabel('easy come, easy go')
    
    plt.show()