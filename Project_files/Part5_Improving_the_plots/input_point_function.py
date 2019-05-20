import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



def input_point(objectx,atloc, lonloc, sizex, colorx, alphax):
    '''
    - Our function to draw a specific x and y on a map
        - This function need a m-object from basemap to be define first.
            this is not an efficient way to define a function since it rely heavily on define
            the object (m) which is needed to plot the map itself.
        - [Update] : I was able to fix this problem by allowing the drawing object as one of the inputs.
            for our current case the object name (m).

    '''
    lat, lon = atloc, lonloc
    x, y = objectx(lon, lat)
    return objectx.plot(x, y, 'go', markersize=sizex, color=colorx, alpha=alphax)
