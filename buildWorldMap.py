"""
Program: buildWorldMap.py

Author: Benjamin Forman

Description: this script utilizes matplotlib and the basemap package it provides to users. The script produces a map of the world and displays different ways of customizing the map and adding value and detail where desired. pyplot, another package of matplotlib, is used to display the map.
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

#create the map object
#'robin' setting displays map laid out, 'ortho' displays world as a globe
map = Basemap(projection='robin', lat_0=0, lon_0=-100,
                resolution='l', area_thresh=1000.0)
#drawcoastlines() and drawcountries() produce sharper lines on the image
map.drawcoastlines()
map.drawcountries()
#map.fillcontinents(color='coral')
map.bluemarble()
map.drawmapboundary()
#drawmeridians and drawparallels places lat and long lines on the map
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
plt.show()

end of file                         
