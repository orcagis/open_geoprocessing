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

def list_fields():
    pass
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
            if id > 10:
                break

    return output_coords

def main():
    pass

if __name__ == '__main__':
    main()