import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



def input_point(atloc, lonloc, sizex, colorx, alphax):
    '''
    - Our function to draw a specific x and y on a map
        - This function need a m-object from basemap to be define first.
            this is not an efficient way to define a function since it rely heavily on define
            the object (m) which is needed to plot the map itself.
    '''
    m = Basemap(projection='mill',
                llcrnrlat=20,
                urcrnrlat=50,
                llcrnrlon=-130,
                urcrnrlon=-60, resolution='c')
    lat, lon = atloc, lonloc
    x, y = m(lon, lat)
    return m.plot(x, y, 'go', markersize=sizex, color=colorx, alpha=alphax)
