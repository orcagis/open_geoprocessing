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

# modify to include input polygons (get centroid coords)
# add additional output format types, json will be default
def pt_shp_coord(shp_path):
    #shp_path = r'/Users/justinhawley/Desktop/counties/centroids.shp'
    fn = shp_path
    ds = ogr.Open(fn, 0)

    if ds is None:
        sys.exit('Could not open {0}.'.format(fn))
    
    lyr = ds.GetLayer(0)
    lyr_def = lyr.GetLayerDefn()
    geom_type = ogr.GeometryTypeToName(lyr_def.GetGeomType())

    if geom_type != 'Point':
        sys.exit('Invalid geometry {0}. Must be Point.'.format(geom_type))

    for feat in lyr:
        pt = feat.geometry()
        x = pt.GetX()
        y = pt.GetY()
        print('{}, {}'.format(x,y))

    del ds


def read_gdb(gdb_path, layer_name):
    ogr.UseExceptions()
    driver = ogr.GetDriverByName("OpenFileGDB")
    try:
        gdb = driver.Open(gdb_path, 0)
    except Exception as e:
        print (e)
        sys.exit()

    for featsClass_idx in range(gdb.GetLayerCount()):
        lyr = gdb.GetLayerByIndex(featsClass_idx)
        if lyr.GetName() == layer_name:
            for feat in lyr:
                pt = feat.geometry()
                x = pt.GetX()
                y = pt.GetY()
                print('{}, {}'.format(x,y))
    del gdb

def main():
    pt_shp_coord(r'/Users/justinhawley/Desktop/counties/centroids.shp')
    #read_file_gdb(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids')

if __name__ == '__main__':
    main()
