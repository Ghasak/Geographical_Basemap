# Geographical Plotting with Python Part 5 -
## - Improving the plots
Continue our progress with map using **basemap**. and we will try to change the size and the size of the marker.

## Step -1-
Changing the dot size is simple as following the steps form previous tutorial. We can get it using:
```
m.plot(x,y,'r.', markersize = 50)
```
I have created a function that can show the a point on the specific map given the object (m) defined already through the **basemap** library.
```
def input_point(atloc, lonloc, sizex):
    lat, lon = atloc, lonloc
    x, y = m(lon, lat)
    return m.plot(x, y, 'go', markersize=sizex)
```
## Step -2-
After adding the function above to draw points on the map, we proceed with inputting many points as an array. Here is an example:

```
lat = [30,31,34,33,32]
lon = [-103,-110,-107,-111,-115]

lat2 = [40, 33, 44, 31, 30]
lon2 = [-113, -100, -102, -111, -112]

input_point(lat, lon, 15, "y",0.7)
input_point(lat2,lon2, 25, "r", 0.6)
```
see the results here:

![](https://github.com/Ghasak/Geographical_Basemap/blob/master/Project_files/Part5_Improving_the_plots/Resources/Screen%20Shot%202019-05-20%20at%2018.10.31.png)
## Authors


## Step -3-
I have created a function externally and called through our main code. The practice here is not so efficient as the function is rely on the object (m) to be define in the main script file **5_tutorial.py**. The function is located withing the  directory of this tutorial part namely **input_point_function**
```
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

```

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
