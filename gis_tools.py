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

def get_lyr_feat_count(path, layer_name = False, print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     lyr_feat_count = gis_analysis.get_lyr_feat_count(lyr[0], print_to_screen)
     return lyr_feat_count

def get_lyr_extent(path, layer_name = False, print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     lyr_extent = gis_analysis.get_lyr_extent(lyr[0], print_to_screen)
     return lyr_extent

def get_lyr_geom_type(path, layer_name = False, print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     geom_type = gis_analysis.get_geom_type(lyr[0], print_to_screen)
     return geom_type

def get_lyr_coords(path, layer_name = False, out_name = None, out_path = None, out_format = 'json', print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     lyr_coords = gis_analysis.get_pt_coords(lyr[0],print_to_screen) # returns json

     if out_format == 'csv':
          gis_output.export_csv(lyr_coords, out_name, out_path, headers = True)
     elif out_format == 'xlsx':
          gis_output.export_xlsx(lyr_coords, out_name, out_path, headers = True)
     return lyr_coords

def list_lyr_fields(path, layer_name = False, print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     lyr_fields = gis_analysis.list_fields(lyr[0], print_to_screen)
     return lyr_fields

def export_lyr_attributes(path, layer_name = False, fields = [], out_name = None, out_path = None, out_format = 'json', print_to_screen = False):
     lyr = gis_input.get_layer(path,layer_name)
     if not fields:
          fields = gis_analysis.list_fields(lyr[0])
     lyr_attributes = gis_analysis.get_lyr_attributes(lyr[0],fields, print_to_screen)

     if out_format == 'csv':
          gis_output.export_csv(lyr_attributes, out_name, out_path, headers = True)
     elif out_format == 'xlsx':
          gis_output.export_xlsx(lyr_attributes, out_name, out_path, headers = True)
     return lyr_attributes

def main():
     #my_fields = list_lyr_fields(r'/Users/justinhawley/Desktop/counties/centroids.shp', print_to_screen = True)

     #my_attributes = export_lyr_attributes(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids', fields = None, out_name = 'centroids_data', out_path = '/Users/justinhawley/repos/fastgisapi/output', out_format = 'csv', print_to_screen = False)

     #my_geom = get_lyr_geom_type(r'/Users/justinhawley/Desktop/counties/centroids.shp', layer_name = 'centroids', print_to_screen = True)

     #my_extent = get_lyr_extent(r'/Users/justinhawley/Desktop/counties/centroids.shp', layer_name = 'centroids', print_to_screen = False)

     #my_count = get_lyr_feat_count(r'/Users/justinhawley/Desktop/counties/centroids.shp', layer_name = 'centroids', print_to_screen = False)
     my_count = get_lyr_feat_count(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids', print_to_screen = False)
     
     print(my_count)

     #export_lyr_attributes(r'/Users/justinhawley/Desktop/counties/centroids.shp', fields = None, out_name = 'centroids_data', out_path = '/Users/justinhawley/repos/fastgisapi/output', out_format = 'json', print_to_screen = True)

     #my_coords = get_lyr_coords(r'/Users/justinhawley/Desktop/my_gdb.gdb','centroids',out_name = 'coords_export_gdb', out_path = '/Users/justinhawley/repos/fastgisapi/output', out_format = 'xlsx', print_to_screen = True)
     #my_coords = get_lyr_coords(r'/Users/justinhawley/Desktop/counties/centroids.shp', out_name = 'coords_export', out_path = '/Users/justinhawley/repos/fastgisapi/output', out_format = 'csv', print_to_screen = True)

if __name__ == '__main__':
    main()