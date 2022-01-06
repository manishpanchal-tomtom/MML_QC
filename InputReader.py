# Import libraries & dependencies
import geopandas as gpd
import os


def InputReader(path, layer=None):
    """This function can read files that is both in
    #Geojson
    #.gdb
    #shp
    #geopackage
    #csv (default ,)
    #excel"""

    name, extension = os.path.splitext(path)

    if ".shp" in str(path) or ".geojson" in str(path):
        so_file = gpd.read_file(path)
        file_headers = so_file.columns

        return so_file, file_headers

    elif ".gdb" in str(path) or ".gpkg" in str(path):
        so_file = gpd.read_file(path, layer=layer)
        file_headers = so_file.columns

        return so_file, file_headers