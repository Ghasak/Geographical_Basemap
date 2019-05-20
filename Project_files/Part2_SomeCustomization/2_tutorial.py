import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


plt.figure(figsize=(8, 8))

m = Basemap(projection='mill',
                          llcrnrlat=-60,
                          urcrnrlat=90,
                          llcrnrlon=-180,
                          urcrnrlon=180, resolution='c')
# 'C' is for crucial resolution, you can change to 'l', 'h' ..etc.

m.drawcoastlines()
#m.fillcontinents()
m.fillcontinents(color= '#072b57', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')
plt.title('Quick basemap example!')
plt.show()
