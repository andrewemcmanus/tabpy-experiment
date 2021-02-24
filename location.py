import numpy as np
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
locations = df[8]

print(locations)
# define location as
# location = sheet["I"] ?
# location = {'latitude': '41.87632184', 'longitude': '-87.77410482'}
# latitude = float(location["latitude"])
# longitude = float(location["longitude"])
# add value in LATITUDE or LONGITUDE cell in that row
# or just extract and route to GeoJSON for D3
# print(longitude)
# return proper format for map object to render
