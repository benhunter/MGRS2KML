# MGRS2KML
 MGRS coordinates to KML

MGRSPy
FastKML https://fastkml.readthedocs.io/en/latest/usage_guide.html
Shapely https://pypi.org/project/Shapely/
Shapely wheel: https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely



# Old Notes
* Originally tried to use mgrspy on Windows, but had issues with GDAL Python Bindings with osr function calls (from osgeo import osr)
* mgrspy https://pypi.org/project/mgrspy/
* mgrspy requires GDAL: https://pypi.org/project/GDAL/
* GDAL requires NumPy

Windows setup
* GDAL core: http://download.gisinternals.com/sdk/downloads/release-1911-x64-gdal-3-0-0-mapserver-7-4-0/gdal-300-1911-x64-core.msi
* GDAL core must be in PATH environment variable.
* GDAL wheel (for your version of python and architecture): https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal 
