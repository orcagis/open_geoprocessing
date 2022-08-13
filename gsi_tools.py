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
import gis_input
import gis_analysis
import gis_output

def main():
     #my_layer = gis_input.get_layer(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids')
     my_layer = gis_input.get_layer(r'/Users/justinhawley/Desktop/counties/centroids.shp')
     my_coords = gis_analysis.get_pt_coords(my_layer[0], False)
     gis_output.export_csv(my_coords, 'zest2')

if __name__ == '__main__':
    main()