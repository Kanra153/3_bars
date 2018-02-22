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


def get_biggest_bar(bars_info):
    biggest_bar = max(
        bars_info,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bars_info):
    smallest_bar = min(
        bars_info,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def get_closest_bar(bars_info, longitude, latitude):
    closest_bar = min(
        bars_info,
        key=lambda x:
        sqrt(
                (x['geometry']['coordinates'][0] - longitude)**2 +
                (x['geometry']['coordinates'][1]-latitude)**2
        )
     )
    return closest_bar


def output_bars_to_console(bar):
    print('Name: {}'
          .format(bar['properties']['Attributes']['Name']), '\n',
          'Number of seats: {}'
          .format(bar['properties']['Attributes']['SeatsCount']), '\n',
          'Coordinates: {}, {}'
          .format(bar['geometry']['coordinates'][0],
          bar['geometry']['coordinates'][1]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('File is not found!')
    file_path = sys.argv[1]
    parsed_json = load_data(file_path)
    bars_info = parsed_json['features']
    try:
        longitude = float(input('Please, input longitude:'))
        latitude = float(input('Please, input latitude:'))
    except ValueError:
        sys.exit('Restart the script using'
                 'correct format of your coordinates')
    biggest_bar = get_biggest_bar(bars_info)
    smallest_bar = get_smallest_bar(bars_info)
    closest_bar = get_closest_bar(bars_info, longitude, latitude)
    print('The biggest bar is:')
    output_bars_to_console(biggest_bar)
    print('The smallest bar is:')
    output_bars_to_console(smallest_bar)
    print('The closest bar is:')
    output_bars_to_console(closest_bar)
