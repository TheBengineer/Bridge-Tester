

def Draw_Chart(surface,x,y,hsize,vsize,dataset,(DataStart,DataEnd,DataMin,DataMax),color,bordercolor,border):
    import pygame
    DataLen = DataEnd-DataStart
    DataHeight = DataMax-DataMin
    xscale = (hsize+1)/DataLen
    yscale = (vsize+1)/DataHeight
    if border >= 1:
        pygame.draw.lines(surface,bordercolor,0,((x,y),(x,y+vsize),(x+hsize,y+vsize),(x+hsize,y),(x,y)),border)
    lines = []
    if DataLen > hsize: #throw fit
        print "Not enough Graph Space. Impement a thingy."
        return
    for j in range(DataEnd-DataStart):
        i = dataset[j+DataStart]
        if (type(i)== type(float())) or (type(i) == type(int())):
            lines.append((x+(j*xscale),(y+vsize)-(i*yscale)))
        elif len(i) == 2:
            lines.append(((i[0]*xscale)+x,(y+vsize)-(i[1]*yscale)))
    pygame.draw.lines(surface,color,0,lines,1)
        
def updateThrottle(rpm,throttle,factor):
    if factor > 1:
        factor = 1
    if factor < 0:
        factor = 0
    if throttle > 1:
        throttle = 1
    if throttle < 0:
        throttle = 0
    rpm += ((throttle*10000)-rpm)*factor
    return rpm,throttle,factor

