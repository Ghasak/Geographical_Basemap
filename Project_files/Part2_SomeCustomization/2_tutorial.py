import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


plt.figure(figsize=(8, 8))

m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()
plt.title('Quick basemap example!')
plt.show()
