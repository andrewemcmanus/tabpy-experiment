import ast
# import numpy as np
from openpyxl import load_workbook
import pandas as pd

workbook = load_workbook(filename="cta-ridership-avg.-weekday-bus-stop-boardings-in-october-2012.xlsx")
sheet = workbook.active
values = sheet.values

# print(df)
cols = next(values)
values = list(values)

# LOCATION = 8
# idx = [row[0] for row in values]
# print(coordinates)
df = pd.DataFrame(values)
# location column:
location_list = list(df[8])
# stop Id column:
# print(df[0])
# ast.literal_eval(df[8])
locations = []
for i in location_list:
    if i == location_list[0]:
        print(i)
    else:
        dict = ast.literal_eval(i)
        locations.append(dict)
# print(locations)
coordinates = []
for i in locations:
    lat = float(i['latitude'])
    long = float(i['longitude'])
    coordinates.append([lat, long])
    # long = float(i['latitude'])
print(coordinates)
# lat = float(loc['latitude'])
# long = float(loc['longitude'])
# print(location_list)
# define location as
# location = sheet["I"] ?
# location = {'latitude': '41.87632184', 'longitude': '-87.77410482'}
# latitude = float(location["latitude"])
# longitude = float(location["longitude"])
# add value in LATITUDE or LONGITUDE cell in that row
# or just extract and route to GeoJSON for D3
# print(longitude)
# return proper format for map object to render
