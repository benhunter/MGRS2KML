# MGRS2KML - convert list of MGRS coordinates to a KML file
# usage:
#       python mgrs2kml.py <MGRS.csv> <output.kml>

import csv
import sys

import mgrs
from fastkml import kml
from shapely.geometry import Point

input_csv = sys.argv[1]
data = []
output_kml = sys.argv[2]

# open file
with open(input_csv, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        data.append(row)

print(data)

# convert to coordinates for KML
# TODO test MGRS formats. Spaces, caps
for point in data[1:]:
    m = mgrs.MGRStoLL(''.join(point[1].split()))
    print(point, m)
    point.append(m)
print(data)

# build KML
# initialize the KML document
k = kml.KML()
ns = '{http://www.opengis.net/kml/2.2}'
d = kml.Document(ns, "NULL", "NULL", "NULL")  # TODO update fields
k.append(d)

for point in data[1:]:
    p = kml.Placemark(ns, point[0], point[0], point[0])
    # KML uses long, lat, alt for ordering coordinates (x, y, z)
    elevation = 0
    p.geometry = Point(point[2]['lon'], point[2]['lat'], elevation)
    d.append(p)


print(d)
print(k)

with open(output_kml, 'w') as f:
    f.write(k.to_string())
    print('Finished. Wrote output to:', output_kml)
