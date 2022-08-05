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

# modify to include input polygons (get centroid coords)
# add additional output format types, json will be default

def pt_coord_shp(path):
    file_name, file_extension = os.path.splitext(path)
    if file_extension == '.shp':
        fn = path
        ds = ogr.Open(fn, 0)

        if ds is None:
            sys.exit('Could not open {0}.'.format(fn))
    
        lyr = ds.GetLayer(0)
        lyr_def = lyr.GetLayerDefn()
        geom_type = ogr.GeometryTypeToName(lyr_def.GetGeomType())

        if geom_type != 'Point':
            sys.exit('Invalid geometry {0}. Must be Point.'.format(geom_type))
        else:
            coords = get_coords(lyr)
            del ds
            return coords
    else:
        sys.exit('Invalid file type, must be shapefile (.shp)')

def pt_coord_gdb(path, layer_name = None):
    file_name, file_extension = os.path.splitext(path)
    if file_extension == '.gdb':
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
                lyr_def = lyr.GetLayerDefn()
                geom_type = ogr.GeometryTypeToName(lyr_def.GetGeomType())

                if geom_type != 'Point':
                    sys.exit('Invalid geometry {0}. Must be Point.'.format(geom_type))
                else:
                    coords = get_coords(lyr)
                    del gdb
                    return coords
    else:
         sys.exit('Invalid file type, must be file geodatabase (.gdb)')

# prints the coordinates (y, x)
def print_coords(lyr):
    for feat in lyr:
        pt = feat.geometry()
        x = pt.GetX()
        y = pt.GetY()
        print('{}, {}'.format(x,y))

# returns coordinates as a json response, id's are arbitrary
def get_coords(lyr):
    id = 0
    output_coords = []
    for feat in lyr:
        pt = feat.geometry()
        x = pt.GetX()
        y = pt.GetY()
        print('{}: {}, {}'.format(id,x,y))
        record = {
            "id": id,
            "x": x,
            "y": y
        }
        output_coords.append(record)
        id += 1
        
        #for test
        if id > 10:
            break
    return output_coords

def main():
    #my_coords = pt_coord_shp(r'/Users/justinhawley/Desktop/counties/centroids.shp')
    my_coords = pt_coord_gdb(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids')
    print(my_coords)

if __name__ == '__main__':
    main()