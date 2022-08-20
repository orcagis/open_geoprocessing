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

# int -> OFTInteger
# double -> OFTReal
# text -> OFTString
# date -> OFTDate
def add_field(layer, source, field_name, data_type, length, print_to_screen = False):
    file_name, file_extension = os.path.splitext(source.name)
    ogr_data_type = None

    if file_extension == '.shp':
        if data_type == 'int':
            ogr_data_type = ogr.OFTInteger
        elif data_type == 'double':
            ogr_data_type = ogr.OFTReal
        elif data_type == 'text':
            ogr_data_type = ogr.OFTString
        elif data_type == 'date':
            ogr_data_type = ogr.OFTDate

        new_field = ogr.FieldDefn(field_name, ogr_data_type)
        if length and data_type == 'text':
            new_field.SetWidth(length)
        layer.CreateField(new_field)
    else:
        sys.exit('Invalid format')
   
def get_spatial_ref(layer, print_to_screen = False):
    spatial_ref = layer.GetSpatialRef()
    if print_to_screen:
        print('spatial reference: {}'.format(spatial_ref))
    #spatial_ref = {'spatial_ref': spatial_ref}  
    return spatial_ref

def get_geom_type(layer, print_to_screen = False):
    feat = layer.GetFeature(0)
    geom_type = feat.geometry().GetGeometryName()
    if print_to_screen:
        print('geometry type: {}'.format(geom_type))
    geom_type = {'geometry_type': geom_type}  
    return geom_type

def get_lyr_extent(layer, print_to_screen = False):
    lyr_extent = layer.GetExtent()
    if print_to_screen:
        print('layer_extent: {}'.format(lyr_extent))
    lyr_extent = {
        'min_x': lyr_extent[0],
        'max_x': lyr_extent[1],
        'min_y': lyr_extent[2],
        'max_y': lyr_extent[3]
    }
    return lyr_extent

def get_lyr_feat_count(layer, print_to_screen = False):
     feature_count = layer.GetFeatureCount()
     if print_to_screen:
        print('feature count: {}'.format(feature_count))
     return feature_count

def get_lyr_schema(layer, print_to_screen = False):
    schema = []
    for field in layer.schema:
        record = {}
        record['name'] = field.name
        record['type'] = field.GetTypeName()
        schema.append(record)
        if print_to_screen:
                print('{}: {}'.format(record['name'], record['type']))
    return schema

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