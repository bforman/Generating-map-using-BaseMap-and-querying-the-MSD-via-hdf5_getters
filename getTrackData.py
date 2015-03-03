"""
getTrackData.py

Author: Benjamin Forman

Purpose: This script accesses a 10,000 song subset of the MSD and extracts data pertaining to
artist name, song title, latitude, and longitude of the artist using hdf5_getters. os and glob
are used to essentially navigate the tree of files that is the MillonSongSubset. As the for loop
runs through each song in the subset, it extracts the four data attributes and pairs them to a key in
a list as a quadruple. Although others may want to abstract other attributes besides these four, this
practice of obtaining the data will be found useful by anybody who is trying to collect and group
data together in some particular order. At the very least this script will assist in showing ONE way
to scrape desired data from the echonest database.

"""
import sys
import math
import pyechonest
import echonest.remix.audio as audio
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import hdf5_getters


def getTrackData(basedir,ext='.h5'):
        trackList = []
        count = 0
        for root, dirs, files in os.walk(basedir):
                files = glob.glob(os.path.join(root,'*'+ext))
                for file in files:
                        h5 = hdf5_getters.open_h5_file_read(file)
                        if math.isnan(hdf5_getters.get_artist_longitude(h5)):
                                count += 1
                        trackList.append((hdf5_getters.get_artist_name(h5),hdf5_getters.get_title(h5),hdf5_getters.get_artist_longitude(h5),hdf5_getters.get_artist_latitude(h5)))
                        h5.close()
        print 10000 - count
        print trackList[:10]
        return trackList

getTrackData('MillionSongSubset')
