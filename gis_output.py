#-------------------------------------------------------------------------------
# Name:        gis_output.py
# Purpose:     Gets coordinates for point layers
#
# Author:      Justin Hawley (justin@orcagis.com)
#
# Created:     08/04/2022
#
# Interpreter: /fastgisapi/venv/bin/python3
#-------------------------------------------------------------------------------

import csv

def export_csv(json, name, headers = True):
    name = '{}.csv'.format(name)

    # get columns, only grabs whats in first row
    columns = []
    for line in json:
        for key, val in line.items():
            columns.append(key)
        break

    with open(name, 'w',newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader()
            for key in json:
                writer.writerow(key)