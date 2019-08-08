# How to plot data on maps in Jupyter using Matplotlib, Plotly, and Bokeh

* Read more here: https://www.bigendiandata.com/2017-06-27-Mapping_in_Jupyter/
* See also: https://bokeh.pydata.org/en/latest/docs/user_guide/geo.html

If you’re trying to plot geographical data on a map then you’ll need to select a plotting library that provides the features you want in your map. And if you haven’t plotted geo data before then you’ll probably find it helpful to see examples that show different ways to do it. So, in this post I’m going to show some examples using three different python mapping libraries. Specifically, I will show how to generate a scatter plot on a map for the same geographical dataset using Matplotlib, Plotly, and Bokeh in Jupyter notebooks.
What is Jupyter?
Jupyter is a web application that allows you to create notebooks that contain live code, visualizations, and explanatory text. It’s often used by data scientists for statistical modeling and data visualization. I frequently use Jupyter as a development environment to explore data sets and develop visualizations prior to implementing them in a standalone web application.
Matplotlib vs Plotly vs Bokeh
The three plotting libraries I’m going to cover are Matplotlib, Plotly, and Bokeh. Bokeh is a great library for creating reactive data visualizations, like d3 but much easier to learn (in my opinion). Any plotting library can be used in Bokeh (including plotly and matplotlib) but Bokeh also provides a module for Google Maps which will feel very familiar to most people. Google Maps does one thing and it does it well. On the other hand, Matplotlib and Plotly can do much more than just plot data on maps. As far as geo mapping goes Matplotlib and Plotly look different (sometimes better) from the canonical Google Maps visual. I’ve given all three of these libraries a pretty fair shake, and of the three I prefer using Bokeh with Google Maps because it’s so familiar and so simple to plot anything with latitude and longitude data.

In these examples, I'm plotting data from the California Housing Prices dataset, which I discovered while reading Hands-On Machine Learning with Scikit-Learn & TensorFlow, by Aurélien Géron. If you're interested in learning about how real world machine learning applications get developed and operationalized, I highly recommend Aurélien's book! For the matplotlib example below, I borrowed heavily from the code Aurélien posted here.

Please provide your feedback to this article by adding a comment to https://github.com/iandow/iandow.github.io/issues/3.


Geo Mapping with Matplotlib
To learn more about working with scatter plots on maps with Matplotlib, read Chapter 2 of Hands-On Machine Learning with Scikit-Learn & TensorFlow, by Aurélien Géron.

Geo Mapping with Plotly
To learn more about working with scatter plots on maps with Plotly, check out https://plot.ly/python/scatter-plots-on-maps/.
