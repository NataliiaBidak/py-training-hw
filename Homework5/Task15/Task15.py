"""
Write a python program that takes a list of file extensions and prints all the files from the current
directory matching the extension given. The following extensions and meaning should be supported:
c should find and print all .c and .h file names
py should find and print all .py and .pyc file names
pl should find and print all .pl and .pm file names
Bonus: Read extension and meaning from a configuration file.
json.dumps -перетворює в json формат  стрічку
json.loads - перетворює json в Python  стрічку
json.dump -перетворює в json формат  потік
json.load - перетворює json в Python  потік

"""

import os
import json
import sys

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

cars_json = json.dumps(cars)

with open("cars.json", 'w') as cars_file:
    cars_file.write(cars_json)

with open("cars.json", 'r') as cars_file:
    cars = json.load(cars_file)

def get_all_jeeps():
    list_of_cars = cars.get("Jeep")
    return (', '.join(list_of_cars))


def get_first_model_each_manufacturer():
    new_list = []
    for x, y in cars.items():
        new_list.append(y[0])
    return new_list


def get_all_matching_models(grep='Trail'):
    new_list = []
    for x, y in cars.items():
        for name in y:
            if grep.lower() in name.lower():
                new_list.append(name)
    return sorted(new_list)


def sort_dict_alphabetically():
    for x, y in sorted(cars.items()):
        cars.update({x: sorted(y)})
    dump_list = json.dumps(cars, sort_keys=True)
    return json.loads(dump_list)


expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
actual = get_all_jeeps()
assert type(actual) == str
assert actual == expected


actual = get_first_model_each_manufacturer()
expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
assert actual == expected



expected = ['Trailblazer', 'Trailhawk']
assert get_all_matching_models() == expected
expected = ['Accord', 'Commodore', 'Falcon']
assert get_all_matching_models(grep='CO') == expected



actual = sort_dict_alphabetically()
expected = {
    'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
    'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
    'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
    'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
    'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
}
assert actual == expected
