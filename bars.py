import json
import os
import sys
from math import sqrt


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        parsed_json = json.load(file_handler)
    return parsed_json


def get_biggest_bar(data):
    bars = parsed_json['features']
    bar_attributes = []
    for bar in bars:
        bar_attributes.append(bar['properties']['Attributes'])
    biggest_bar = max(bar_attributes, key=lambda x: x['SeatsCount'])
    return(biggest_bar['Name'])


def get_smallest_bar(data):
    bars = parsed_json['features']
    bar_attributes = []
    for bar in bars:
        bar_attributes.append(bar['properties']['Attributes'])
    smallest_bar = min(bar_attributes, key=lambda x: x['SeatsCount'])
    return(smallest_bar['Name'])


def get_closest_bar(data, longitude, latitude):
    bars = parsed_json['features']
    closest_bar = min(bars, key=lambda x: sqrt(
        (x['geometry']['coordinates'][0] - longitude)**2 + 
        (x['geometry']['coordinates'][1]-latitude)**2))
    return(closest_bar['properties']['Attributes']['Name'])


if __name__ == '__main__':
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        parsed_json = load_data(file_path)
        longtitude = float(input("Please, input longtitude:"))
        latitude = float(input("Please, input latitude:"))
        print("The biggest bar is:",  get_biggest_bar(parsed_json))
        print("The smallest bar is:", get_smallest_bar(parsed_json))
        print("The closest bar to you is:",
              get_closest_bar(parsed_json, longtitude, latitude))
    else:
        print('File is not found!')
