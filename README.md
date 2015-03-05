# Generating-map-using-BaseMap-querying-the-MSD-via-hdf5_getters
This research module goes into the process of creating a map image using BaseMap, a module from MatPlotLib. It also displays how to abstract data from the million song database (MSD), which is powered by EchoNest, using the script: hdf5_getters.py. hdf5_getters provides several different methods to get artist/song/other attributes data from a track by querying the MSD, such as: artist_i.d., artist_hotnesss, artist_location, get_title, get_similar_artists, and many others. The hdf5_getter module works in cooperation within the getTrackData.py script with the os and glob modules. os and glob are Python standard library modules. This research module includes both the script used to produce the map image via basemap, as well as the getTrackData.py script, and goes into detail about each

#Problem 
Before I was able to start constructing the foundation for the world music map, I had to figure out how to extract desired information from audio files. Particularly I was aiming to deduce how to obtain the: artist name, song title, artist latitude, and artist longitude from the audio file. I wanted this data so that I could then create data pinpoints to place on the world map for the respective artist/song pairs in whichever given country they originated. I needed to figure out how to collect the data necessary for producing these pinpoints because they will serve as a key aspect of the visualization and usability of the map. With pin points (produced via latitude and longitude pairs) that pop up on the map, users will be able to simply click the point and information pertaining to the song, artist, and background will then be provided. I produced this Python script that will go through 10,000 songs, extract the data, and place it into a list as a set of quadruples. I did so in hope that others will be able to use it and modify the script to extract the specific data they wish to obtain. Being able to produce a list that encapsulates such a myriad of data is a practice I thought others would deem very useful in their own projects. Also as part of my brainstorming I wanted to figure out another way to produce a map of the world and deciphered a way using BaseMap, a module provided by MatPlotLib.

#Process
buildWorldMap uses a data set called geos-3.3.3 provided by the basemap-1.0.7 download to provide the information needed to contstruct the map. The script produces the map by calling the BaseMap function and setting some specifiers. Then different attributes of the map are distinguished by calling different customization functions provided by BaseMap.

getTrackData uses the MillionSongSubset as a base directory to access. This directory is organized as a tree of files, starting at the root and descending into several branches. The use of the os and glob modules assists in traversing the tree and acessing all 10,000 songs. The file type passed to os is '.h5' because those are the type of files within the MillionSongSubset. As each song in the subset are visited, getter functions from hdf5_getters are used to retrieve the data we wish to obtain. As it extracts each piece of data for each song, it appends it to the trackList in quadruplets (sets of 4). Once the script completes you will have all the data you need in an organized list.

#Dependencies
For buildWorldMap:
- matplotlib.pyplot
- numpy
- mpl_toolkits.basemap

For getTrackData:
- directory of x amount of songs
- sys
- os
- glob
- hdf5_getters

#Example
Here is an example of how to use os and glob to traverse a directory of files. Notice the root, dirs, files notation. A resource on how that notation works is provided by this quick-read resource
[root, dirs, files]: http://www.tutorialspoint.com/python/os_walk.htm
This code extract from my code provides an example of properly using os and glob as well as the root, dirs, files notation:
The path for the base directory is set within the parameters of the function signature which may be a new notation for people to see.
```
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
```
An example of a chunk of data that would be produced and appended to trackList would be:
```
 ('The Box Tops', 'Soul Deep', -90.048919999999995, 35.149679999999996)
 ```
 Providing: Artist, Song Title, Longitude, and Latitude
 
For an example of how to produce a map using BaseMap take a look at the script I've provided, but the gist of initiliazing the map is shown below:
```
map = Basemap(projection='robin', lat_0=0, lon_0=-100,
                resolution='l', area_thresh=1000.0)
```

#Code Explanation 
The function signature denotes that the extension for all files in the base directory will be .h5 in a sense to let the function know what it's looking for. The for loop essentially uses os to traverse every file within the directory from the root using the built-in walk function. Glob provides a list of pathnames that match the pathname in parenthesis, which in this case is the .h5 extension, and uses it's built-in join function to link the path to all of the .h5 files from the root all the way down the tree. Now all of the files are in one place where they can be accessed by simply following all the way down the tree of files from root to leaf. The file must be declared as a variable so that its attributes can be accessed and stored into trackList. It also has to be declared as a object in order to open the file for data extraction and to close it prior to advancing to another file. Once the file is opened:
h5 = hdf5_getters.open_h5_file_read(file) we can then append data from it to our trackList by calling one of the helper methods from hdf5_getters i.e. hdf5_getters.get_artist_name(h5). Upon appending data to our list we need to be sure and close the file before proceeding to the next file. Once the script has ran through the total amount of songs in the base directory, trackList will be populated with all the data we needed. The script can be modified to obtain many other different attributes from the track. The hdf5_getters github README provides a list of all of the helper methods available and can give a good idea of exactly how much data you can work with when dealing with .h5 files. Here is the link to that page:
[hdf5_getters GitHub]: https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py

