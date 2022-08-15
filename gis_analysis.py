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

def list_fields(layer, print_to_screen = False):
    schema = []
    ldefn = layer.GetLayerDefn()
    for n in range(ldefn.GetFieldCount()):
        fdefn = ldefn.GetFieldDefn(n)
        schema.append(fdefn.name)
        if print_to_screen:
            print(fdefn.name)
    return (schema)

def get_lyr_attributes(layer, fields, print_to_screen = False):
    id = 0
    output_data = []
    for feat in layer:
        record = {}
        record['id'] = id
        for field in fields:
            val = feat.GetField(field)
            record[field] = val
            if print_to_screen:
                print (val, end=', ')
        output_data.append(record)
        id += 1
        if print_to_screen:
            print()
    return output_data

# returns coordinates as a json response and optionally prints to screen
def get_pt_coords(pt_lyr, print_to_screen = False):
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
            if print_to_screen:
                print('{}: {}, {}'.format(id,x,y))
            record = {
                "id": id,
                "x": x,
                "y": y
            }
            output_coords.append(record)
            id += 1
    return output_coords

def main():
    pass

if __name__ == '__main__':
    main()