# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:13:16 2017

@author: division
"""
import numpy as np
import matplotlib.pyplot as plt

######################################################

### randomly generated tester set

#import random
#zoom = [-10.0,10.0,-10.0,10.0]
#x1 = random.uniform(-10.0,10.0)
#x2 = random.uniform(-10.0,10.0)
#x3 = random.uniform(-10.0,10.0)
#x4 = random.uniform(-10.0,10.0)
#x5 = random.uniform(-10.0,10.0)
#y1 = random.uniform(-10.0,10.0)
#y2 = random.uniform(-10.0,10.0)
#y3 = random.uniform(-10.0,10.0)
#y4 = random.uniform(-10.0,10.0)
#y5 = random.uniform(-10.0,10.0)
#z1 = random.uniform(-10.0,10.0)
#z2 = random.uniform(-10.0,10.0)
#z3 = random.uniform(-10.0,10.0)
#z4 = random.uniform(-10.0,10.0)
#z5 = random.uniform(-10.0,10.0)
#cs=[[x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4],[x5,y5,z5]]
#neutral_flag = 0
#scheme = 'viridis'

######################################################

### fixed tester set:
def test():
    cs=[[0,10,10],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    zoom = [-10.0,10.0,-10.0,10.0]
    neutral_flag = 0
    scheme = 'viridis'
    findPotential(cs, zoom, neutral_flag, scheme)

######################################################

### user submission form:

#charge format: [x,y,z,q]
#zoom format: [xmin,xmax,ymin,ymax]
#neutral-flag: at origin --> 0 = no neutrals, 1 = neutral(s) present

#cs = [[]]
#zoom = []
#neutral_flag = 0 or 1
#scheme = 'schemenamehere'

######################################################

### equipotential graph generator

def findPotential(cs, zoom, neutral_flag, scheme='viridis'):

    #transpose coordinates and generate x,y data grid. resolution is 60.
    coords = list(map(list, zip(*cs)))
    x = np.linspace(zoom[0],zoom[1], 50)
    y = np.linspace(zoom[2],zoom[3], 50)
    X,Y = np.meshgrid(x, y)
    
    #numerically crunch potential field Z=f(x,y,cs)
    Z = (cs[0][2]/((X-cs[0][0])**2+(Y-cs[0][1])**2)**0.5 
           + cs[1][2]/((X-cs[1][0])**2+(Y-cs[1][1])**2)**0.5 
           + cs[2][2]/((X-cs[2][0])**2+(Y-cs[2][1])**2)**0.5 
           + cs[3][2]/((X-cs[3][0])**2+(Y-cs[3][1])**2)**0.5 
           + cs[4][2]/((X-cs[4][0])**2+(Y-cs[4][1])**2)**0.5)
    
    #renormalization parameters and stdZ catch
    avZ = float(np.average(Z))
    stdZ = float(np.std(Z))
    if stdZ==0:
        stdZ=0.01
    
    #list of contour levels to plot
    Zs = [avZ-stdZ,
          avZ-0.75*stdZ,avZ-0.5*stdZ,avZ-0.35*stdZ,avZ-0.25*stdZ,avZ-0.2*stdZ,
          avZ-0.15*stdZ,avZ-0.1*stdZ,avZ,avZ+0.1*stdZ,avZ+0.15*stdZ,
          avZ+0.2*stdZ,avZ+0.25*stdZ,avZ+0.35*stdZ,avZ+0.5*stdZ,avZ+0.75*stdZ,
          avZ+stdZ]
    
    #suppress potential limits
    Z[Z<avZ-stdZ]=avZ-stdZ
    Z[Z>avZ+stdZ]=avZ+stdZ
    
    #catch no neutral charge at origin
    if neutral_flag == 0 :
        csn=[]
        for i in range(len(cs)):
            if not(cs[i][0]==0 and cs[i][1]==0 and cs[i][2]==0):
                csn.append(cs[i])        
        cs = csn        
        coords = list(map(list, zip(*cs)))
    
    #generate contour plot with overlaid scatter plot
    plt.contourf(X, Y, Z, Zs , cmap = scheme)
    plt.scatter(coords[0],coords[1],zorder=1,c='k')
    frame = plt.gca()
    frame.set_xlim([zoom[0],zoom[1]])
    frame.set_ylim([zoom[2],zoom[3]])
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    plt.savefig('v.png', bbox_inches='tight')