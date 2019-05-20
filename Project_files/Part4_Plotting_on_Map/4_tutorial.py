import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#plt.figure(figsize=(8, 8))

m = Basemap(projection='mill',
            llcrnrlat=20,
            urcrnrlat=50,
            llcrnrlon=-130,
            urcrnrlon=-60, resolution='c')
# 'c' is for crucial resolution, you can change to 'l', 'h' ..etc.


'''
Putting your Coordinates here:
 '''
# -----------------------------------------------------------
lat, lon = 29.76, -96.36
x, y = m(lon,lat)
m.plot(x,y,'r.')
lat, lon = 40.12, -104.24
x,y = m(lon,lat)
m.plot(x,y, 'go')
# -----------------------------------------------------------
m.drawcoastlines()
m.drawcounties()
m.drawstates()
#m.drawrivers()
m.fillcontinents()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')
# -----------------------------------------------------------
plt.title('GeoPlotting!')
plt.show()
plt.close()
