import json
import os
import sys
from math import sqrt
from math import pow


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        parsed_json = json.load(file_handler)
    return parsed_json


def get_biggest_bar(data):
    bars = parsed_json['features']
    seats = []
    for bar in bars:
        seats.append(bar['properties']['Attributes']['SeatsCount'])
    biggest_seats = max(seats)
    for bar in bars:
        if bar['properties']['Attributes']['SeatsCount'] == biggest_seats: #TODO: Сделать с помощью min()/max()
            biggest_bar = bar
    return(biggest_bar['properties']['Attributes']['Name'])



def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        parsed_json = load_data(file_path)
        get_biggest_bar(parsed_json)
