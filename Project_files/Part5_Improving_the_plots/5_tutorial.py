import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# User Define Function {Ghasak} to draw points on our selected map
from input_point_function import input_point   # Or you can use (*)

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
# lat, lon = 29.76, -96.36
# x, y = m(lon,lat)
# m.plot(x,y,'r.', markersize = 20)
# lat, lon = 40.12, -104.24
# x,y = m(lon,lat)
# m.plot(x,y, 'go', markersize = 22)
# -----------------------------------------------------------
# lets here use the function down that we created
# point1 = input_point(29.76, -96.36, 20,"r", 1.0)
# point2 = input_point(40.12,-104.24,10,"b",1.0)
# point3 = input_point(45, -104.24, 10, "b", 0.5)
# -----------------------------------------------------------
lat = [30,31,34,33,32]
lon = [-103,-110,-107,-111,-115]

lat2 = [40, 33, 44, 31, 30]
lon2 = [-113, -100, -102, -111, -112]

input_point(lat, lon, 15, "y",0.7)
input_point(lat2,lon2, 25, "r", 0.6)

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




