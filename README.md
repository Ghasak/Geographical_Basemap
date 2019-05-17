# Geographical Plotting with Python Using -Basemap Package
The Basemap package allow us to run python scipt similar to the QGIS with many features.
It is a part of the Toyota Project that I am working one and here is simply just some
tricks and tips on how to use the package (**basemap**)
* I have used a virtualenv on MacPro Located:
```
~/Desktop/My_DATA_MP/Learning/geographicalplot
```
* On MacPro: ~/Desktop/My_DATA_MP/Leaning


##Expected Results:
Showing the Globe see here:
![]()
And locate a specific location see here:
![]()
##Sub title:
Here we add the following ideas
1. Install the following packages and following the website:
```
I was able to install Basemap fine on Sierra (also using Homebrew for its dependencies), following the instructions here: http://matplotlib.org/basemap/users/installing.html
A couple notes, just to make sure nothing is being overlooked:
    • In your notes, you listed brew install gets, though I assume it was a typo and you actually meant & used brew install geos when installing.
    • Are you certain the correct version of geos was used when modifying your .bash_profile? Some of the examples I've seen around the web use a specific version, so there's always a chance for a copy/paste error. As of yesterday, the version I wound up using was 3.5.0, so my path looked like this: export GEOS_DIR=/usr/local/Cellar/geos/3.5.0/. The version can be verified by looking in your /usr/local/Cellar/geos/ directory to see which one is installed.
    • I'm not 100% certain this matters, but did you reload your .bash_profile after modifying it? source ~/.bash_profile.


This is a full list of what I did:
#   Command Note
1   brew install matplotlib
2   brew install numpy
3   brew install proj

brew install matplotlib
brew install numpy
brew install geos
brew install proj
Downloaded Basemap 1.0.7 source tar file (https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/), untarred it.
Added export GEOS_DIR=/usr/local/Cellar/geos/3.5.0/ to a new line in my .bash_profile, and then reloaded it via:
source ~/.bash_profile
From within untarred Basemap directory:
python setup.py install
Imported Basemap in a python script (via a tutorial elsewhere) with import mpl_toolkits.basemap as bm, and was able to confirm it worked with a produced map.
```

## Better Configuration
This setup up was not working because I have a problem with the installing the pacakge itself. (base-1.0.7.tar.gz) and it wasn’t working until I git the solution
See below:

1.1 What I used Working
On 10.15 Mojave today I did:
#   Command Note
```
1. brew install geos   // I have already installed the brew
2. Pip3 install https://github.com/matplotlib/basemap/archive/master.zip   // I have used pip3 of the virtualenv in python]
3. brew info geos  // This one is to check which version of geos you have already installed on your machine.

brew install geos
pip3 install https://github.com/matplotlib/basemap/archive/master.zip
and it seems to work (mine is Python 3.6 from https://python.org with matplotlib installed by pip).
```
2. Installation Steps
2.1 Preparing the Virtualenv to our Python Gh1
What we can do here is to prepare our virutalenv namely Gh1, and then use it to install all the packages following
```
 ~/Desktop/My_DATA_MP/Learning/geographicalplot
```
We will use at first the Anaconda python to install the virutalenv (make sure you have already installed the package called virtualenv (pip install virtualenv)
Now you need to prepare your virtualenv as following:

python3 -m virtualenv Gh1

This will create a virtualenv called (Gh1) lets proceed:
To check which version we have we simply can write:
```
pip list
Package    Version
---------- -------
pip        19.1.1 
setuptools 41.0.1 
wheel      0.33.4 
```
Now we will install the requirements for this project which are:
pip install matplotlib numpy geos proj

Here is the list of all packages before the basemap
```
Package         Version
--------------- -------
arrow           0.13.1 
Click           7.0    
cycler          0.10.0 
Flask           1.0.2  
geos            0.2.1  
itsdangerous    1.1.0  
Jinja2          2.10.1 
kiwisolver      1.1.0  
lxml            4.3.3  
MarkupSafe      1.1.1  
matplotlib      3.0.3  
numpy           1.16.3 
pip             19.1.1 
proj            0.1.0  
pyparsing       2.4.0  
python-dateutil 2.8.0  
setuptools      41.0.1 
six             1.12.0 
Werkzeug        0.15.4 
wheel           0.33.4 
```
Now what we need is to get the geos in the brew directory and set the virtualenv PATH variable which I have already done following the steps above.
Now we can simply run the magic command to get the Basemap from the GitHub;
```
pip3 install https://github.com/matplotlib/basemap/archive/master.zip
Collecting https://github.com/matplotlib/basemap/archive/master.zip
  Downloading https://github.com/matplotlib/basemap/archive/master.zip
     | 78.2MB 1.4MB/s
```
This will take a bit some time to install but it should be fine,

Done forget this is the directory that I set in the .bash_profile in MacPro
#============================================================================
# Setting PATH form Basemap Package for Python
#============================================================================
```
export GEOS_DIR=/usr/local/Cellar/geos/3.7.2/  # Of course Check through the version: brew info geos
```
Now running
```
-> pip list
Package         Version
--------------- -------
arrow           0.13.1 
basemap         1.2.0  
Click           7.0    
cycler          0.10.0 
Flask           1.0.2  
geos            0.2.1  
itsdangerous    1.1.0  
Jinja2          2.10.1 
kiwisolver      1.1.0  
lxml            4.3.3  
MarkupSafe      1.1.1  
matplotlib      3.0.3  
numpy           1.16.3 
pip             19.1.1 
proj            0.1.0  
pyparsing       2.4.0  
pyproj          2.1.3  
pyshp           2.1.0  
python-dateutil 2.8.0  
setuptools      41.0.1 
six             1.12.0 
Werkzeug        0.15.4 
wheel           0.33.4 
```
Which show us that we already have installed basemap and everything now should work fine.
Final step is to install pillow which is for showing picture in python. And here is the installation:
```
pip install pillow

```

The expected results, from running
python test.py 

## Prerequisites
What things you need to install the software and how to install them:

```
Python 3.7.1 (default, Dec 14 2018, 13:28:58)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
also all requirments are available in

```
pip install -r requirments.txt
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
R 0.x <br />
Packages: see **requirements.txt** <br />
## Instructions
1. Install all required packages
2. Modify parameters if desired
3. Run **folder/script.R**
