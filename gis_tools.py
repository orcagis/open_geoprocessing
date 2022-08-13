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
import csv
# modify to include input polygons (get centroid coords)
# add additional output format types, json will be default

#returns a layer from an input shp or gdb
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

# returns coordinates as a json response and optionally prints to screen
def get_pt_coords(pt_lyr, print_coords = False):
    lyr_def = pt_lyr.GetLayerDefn()
    geom_type = ogr.GeometryTypeToName(lyr_def.GetGeomType())

    if geom_type != 'Point':
        sys.exit('Invalid geometry {0}. Must be Point.'.format(geom_type))
    else:
        id = 0
        output_coords = []
        for feat in pt_lyr:
            pt = feat.geometry()
            x = pt.GetX()
            y = pt.GetY()
            if print_coords:
                print('{}: {}, {}'.format(id,x,y))
            record = {
                "id": id,
                "x": x,
                "y": y
            }
            output_coords.append(record)
            id += 1
    return output_coords

def export_csv(json, headers):
    pass

def main():
    #my_layer = get_layer(r'/Users/justinhawley/Desktop/counties/centroids.shp')
    my_layer = get_layer(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids')
    my_coords = get_pt_coords(my_layer[0])
    print(my_coords)

if __name__ == '__main__':
    main()