import json
import os
import sys
from math import sqrt


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        parsed_json = json.load(file_handler)
    return parsed_json


def get_bars_info(parsed_json):
    bars_info = parsed_json['features']
    return bars_info


def get_biggest_bar(bars_info):
    biggest_bar = max(bars_info,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_info):
    smallest_bar = min(bars_info,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars_info, longitude, latitude):
    closest_bar = min(bars_info, key=lambda x: sqrt(
        (x['geometry']['coordinates'][0] - longitude)**2 +
        (x['geometry']['coordinates'][1]-latitude)**2)
        )
    return closest_bar


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('File is not found!')
    file_path = sys.argv[1]
    parsed_json = load_data(file_path)
    try:
        longitude = float(input("Please, input longitude:"))
        latitude = float(input("Please, input latitude:"))
    except ValueError:
        sys.exit("Restart the script using \
            correct format of your coordinates")
    biggest_bar = get_biggest_bar(get_bars_info(parsed_json))
    print("The biggest bar is:", '\n',
          "Name: {}"
          .format(biggest_bar['properties']['Attributes']['Name']), '\n',
          "Number of seats: {}"
          .format(biggest_bar['properties']['Attributes']['SeatsCount']), '\n',
          "Coordinates: {}, {}"
          .format(biggest_bar['geometry']['coordinates'][0],
          biggest_bar['geometry']['coordinates'][1])
         )
    smallest_bar = get_smallest_bar(get_bars_info(parsed_json))
    print("The smallest bar is:", '\n',
          "Name: {}"
          .format(smallest_bar['properties']['Attributes']['Name']), '\n',
          "Number of seats: {}"
          .format(smallest_bar['properties']['Attributes']['SeatsCount']),
          '\n',
          "Coordinates: {}, {}"
          .format(smallest_bar['geometry']['coordinates'][0],
          smallest_bar['geometry']['coordinates'][1])
         )
    closest_bar = get_closest_bar(get_bars_info(parsed_json),
        longitude, latitude)
    print("The closest bar is:", '\n',
          "Name: {}"
          .format(closest_bar['properties']['Attributes']['Name']), '\n',
          "Number of seats: {}"
          .format(closest_bar['properties']['Attributes']['SeatsCount']),
          '\n',
          "Coordinates: {}, {}"
          .format(closest_bar['geometry']['coordinates'][0],
          closest_bar['geometry']['coordinates'][1])
         )

