#-------------------------------------------------------------------------------
# Name:        get_coordinates
# Purpose:     Gets coordinates for point layers
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     08/04/2022
#
# Interpreter: /fastgisapi/venv/bin/python3
#-------------------------------------------------------------------------------


import sys
from osgeo import ogr
import os

def get_layer(path, layer_name = None):
    file_name, file_extension = os.path.splitext(path)
    if file_extension == '.shp':
        fn = path
        ds = ogr.Open(fn, 0)
        if ds is None:
            sys.exit('Could not open {0}.'.format(fn))
        else:
            lyr = ds.GetLayer(0)
            return [lyr, ds]

    elif file_extension == '.gdb':
        ogr.UseExceptions()
        driver = ogr.GetDriverByName("OpenFileGDB")
        try:
            gdb = driver.Open(path, 0)
        except Exception as e:
            print (e)
            sys.exit()
        for featsClass_idx in range(gdb.GetLayerCount()):
            lyr = gdb.GetLayerByIndex(featsClass_idx)
            if lyr.GetName() == layer_name:
                return [lyr, gdb]
    else:
        sys.exit('Invalid file type...')


def main():
      #my_layer = get_layer(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids')
      #print(my_layer)
      pass

if __name__ == '__main__':
    main()