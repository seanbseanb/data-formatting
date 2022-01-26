#
# Basic Python3 program to parse Aqua Security json scans into an Excel-friendly format.
# Copyright 2022 Sean Berry, BMC Software
# 
# importing the module
import json

import glob

import sys

list_of_files = glob.glob("./lp*_*")

print("_, repository, container_name, filename, file, name, score, severity, score_version, description")
 
for filename in list_of_files:

    # Opening JSON file
    with open(filename) as json_file:
        data = json.load(json_file)
     
        # Print the type of data variable
        #print("Type:", type(data))
     
        # Print the data of dictionary
        #print("\nCVEs:", data['cves'])
    
        #print("\nPrinting nested dictionary as a key-value pair\n")

        for i in data['cves']:

            # description field tends to have all sorts of characters that break a nice quoted CSV, strip them out
            i['description'] = i['description'].replace(',', '_')
            i['description'] = i['description'].replace('"', '_')
            i['description'] = i['description'].replace('\\"', '_')
#            i['description'] = i['description'].replace('\\', '_')
            i['description'] = i['description'].replace("\\n", " ")

            # my data had a line I needed to split, you likely don't
            repo, container_name, *rest = filename.split('_',1)
            print('"', repo, container_name, filename, i['file'], i['name'], i['score'], i['severity'], i['score_version'], i['description'], '"', sep='","')
