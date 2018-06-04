"""
Write a python program that takes a list of file extensions and prints all the files from the current
directory matching the extension given. The following extensions and meaning should be supported:
c should find and print all .c and .h file names
py should find and print all .py and .pyc file names
pl should find and print all .pl and .pm file names
Bonus: Read extension and meaning from a configuration file.
json.dumps -перетворює в json формат в стрічку
json.loads - перетворює json в Python в стрічку
json.dump -перетворює в json формат в стрічку
json.load - перетворює json в Python в потік

"""

import os
import json
import sys


def files_in_dir(*args):
    if not args:
        for file in os.listdir("C:\\Users\\nataliia.bidak\\PycharmProjects\\Training\\py-training-hw\\Homework5\\Task6"):
           print(file)
        # return print([file for file in os.listdir("C:\\Users\\nataliia.bidak\\PycharmProjects\\Training\\py-training-hw\\Homework5\\Task6")])
    with open("file.json", 'r') as file:
        json_file = json.loads(file.read())
        for key in args:
            for extention in json_file[key]:
               # print (list(filter(lambda x:x.endswith(extention), os.listdir("C:\\Users\\nataliia.bidak\\PycharmProjects\\Training\\py-training-hw\\Homework5\\Task6")))[0])
                 print([x for x in os.listdir("C:\\Users\\nataliia.bidak\\PycharmProjects\\Training\\py-training-hw\\Homework5\\Task6") if x.endswith(extention)][0])




if __name__ == '__main__':
    files_in_dir(*sys.argv[1:])

