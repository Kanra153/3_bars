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


def get_biggest_bar(bar_attributes):
    biggest_bar = max(bar_attributes, key=lambda x: x['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bar_attributes):
    smallest_bar = min(bar_attributes, key=lambda x: x['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars, longitude, latitude):
    closest_bar = min(bars, key=lambda x: sqrt(
        (x['geometry']['coordinates'][0] - longitude)**2 +
        (x['geometry']['coordinates'][1]-latitude)**2))
    return closest_bar


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        parsed_json = load_data(file_path)
        bars = parsed_json['features']
        bar_attributes = []
        for bar in bars:
            bar_attributes.append(bar['properties']['Attributes'])
        try:
            longtitude = float(input("Please, input longtitude:"))
            latitude = float(input("Please, input latitude:"))
        except ValueError:
            print("Restart the script using \
            correct format of your coordinates")
            sys.exit()
        print("The biggest bar is:", '\n',
              json.dumps(get_biggest_bar(bar_attributes),
              ensure_ascii=False, indent=3))
        print("The smallest bar is:", '\n',
              json.dumps(get_smallest_bar(bar_attributes),
              ensure_ascii=False, indent=3))
        print("The closest bar to you is:", '\n',
              json.dumps(get_closest_bar(bars, longtitude, latitude),
              ensure_ascii=False, indent=3))
    else:
        print('File is not found!')
