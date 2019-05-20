# Geographical Plotting with Python Part 2 -
## Some Customization
In this series, you are taught how to plot on a map and do geographical plotting with the matplotlib extension called basemap.


## Step -1-

We will add some customization to our current working environment. latitude  runs as y variable -up and down, while longitude runs x variable. Coordinates are given in NESW-order.
To start Japan has Log. and lat. as:
```
Japan   -> 36.2048° N, 138.2529° E
USA     ->
```
The code is showed as:
```
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
```

## Authors

* **Ghasak Ibrahim** - *Initial work* -

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
## Acknowledgments
* Hat tip to anyone whose code was used

## Inspiration
following this project from:
My Original thoughts.


## To add some keyboard keys use:
<kbd>Ctrl</kbd>
## Adding more features:
## Requirements
python 0.x <br />
Packages: see **requirements.txt** <br />
## Instructions
1. Install all required packages
2. Modify parameters if desired
3. Run **folder/script.R**
