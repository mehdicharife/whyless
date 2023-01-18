import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


fig, ax = plt.subplots()
        
    
def drawRight(x,y,r,n):
    x1 = x
    y1 = y
    for i in range(0,n):
        hexagon = mpatches.RegularPolygon(
            (x1, y1), 
            6, 
            radius=r, 
            orientation=np.pi/6, 
            facecolor='#b0497e',
            edgecolor='black',
            linewidth=1
        )

        ax.add_patch(hexagon)
        
        x1 = x1 + 3*r/2
        y1 = y1 + np.sqrt(3)*r/2


def drawLeft(x,y,r,n):
    x1 = x
    y1 = y
    for i in range(0,n):
        hexagon = mpatches.RegularPolygon(
            (x1, y1), 
            6, 
            radius=r, 
            orientation=np.pi/6, 
            facecolor='#b0497e',
            edgecolor='black',
            linewidth=1
        )

        ax.add_patch(hexagon)
        
        x1 = x1 - 3*r/2
        y1 = y1 + np.sqrt(3)*r/2
        
            
               
def drawTopRight(x,y,r,n):
    while n > 0:
        drawRight(x,y,r,n)
        y = y + np.sqrt(3)*r
        n = n -1

        
        
def drawTopLeft(x,y,r,n):
    y1 = y
    while n > 0:
        drawLeft(x,y1,r,n)
        y1 = y1 + np.sqrt(3)*r
        n = n -1
        
        
        
def drawTop(x,y,r,n):
    k = n
    drawTopLeft(x,y,r,k)
    drawTopRight(x,y,r,n)


    
def drawBottomRight(x,y,r,n):
    k = n - 1
    y1 = y - np.sqrt(3)*r
    while k > 0:
        drawRight(x,y1,r,n)
        y1 = y1 - np.sqrt(3)*r
        k = k - 1


def drawBottomLeft(x,y,r,n):
    x1 = x - 3*r/2
    y1 = y - np.sqrt(3)*r/2
    k = n - 1
    while k > 0:
        drawLeft(x1,y1,r,n-1)
        y1 = y1 - np.sqrt(3)*r
        k = k - 1


def drawBottom(x,y,r,n):
    drawBottomRight(x,y,radius,n)
    drawBottomLeft(x,y,radius,n)
    

def draw(x,y,radius,n):
    drawTop(x,y,radius,n)
    drawBottom(x,y,radius,n)
    
    

def color(x,y,radius,i,j,n):
    x0 = x
    y0 = y

    hexagon = mpatches.RegularPolygon(
                (x0, y0), 
                6, 
                radius=radius, 
                orientation=np.pi/6, 
                facecolor='#ffaadf', 
                linewidth=1
    )
    ax.add_patch(hexagon)
    
    x1 = (3+(i-2)*3/2)*radius + x0
    y1 = (j + i/2)*np.sqrt(3)*radius + y0   

    for k in range(0,3):
        for p in range(0,2):
            hexagon = mpatches.RegularPolygon(
                        (2*p*x0 + ((-1)**p)*x1, 2*p*y0 + ((-1)**p)*y1), 
                        6, 
                        radius=radius, 
                        orientation=np.pi/6, 
                        facecolor='#3c001b', 
                        linewidth=1
            )
            
            ax.add_patch(hexagon)
        
        factor = np.sqrt(3*(i**2 + i*j + j**2))*radius

        a=x1
        x1 = x1 - 2*factor*np.sin(np.pi/6)*np.cos(-np.pi/6 + np.arcsin((x1-x0)/factor))
        y1 = y1 + 2*factor*np.sin(np.pi/6)*np.sin(-np.pi/6 + np.arcsin((a-x0)/factor))

        
    
    ax.set_xlim(-10.5*radius, 10.5*radius)
    ax.set_ylim(-10.5*radius, 10.5*radius)
    plt.show()


        
def api(x,y,radius,i,j,n):
    draw(x,y,radius,n)
    color(x,y,radius,i,j,n)

    
    


n = 6   
radius = 4
i = 2
j = 3    

api(0,0,radius,i,j,n)

    




