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

def get_lyr_coords(path, layer_name = False, out_name = None, out_path = None, out_format = 'json', print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     lyr_coords = gis_analysis.get_pt_coords(lyr[0],print_to_screen) # returns json

     if out_format == 'csv':
          gis_output.export_csv(lyr_coords, out_name, out_path, headers = True)
     elif out_format == 'xlsx':
          gis_output.export_xlsx(lyr_coords, out_name, out_path, headers = True)
     return lyr_coords

def main():

     my_coords = get_lyr_coords(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids',out_name = 'coords_export_gdb', out_path = '/Users/justinhawley/repos/fastgisapi/output', out_format = 'xlsx', print_to_screen = True)
     my_coords = get_lyr_coords(r'/Users/justinhawley/Desktop/counties/centroids.shp', out_name = 'coords_export', out_path = '/Users/justinhawley/repos/fastgisapi/output', out_format = 'xlsx', print_to_screen = True)

if __name__ == '__main__':
    main()