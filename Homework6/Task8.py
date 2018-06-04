"""
Write a class named AddressBook that saves names and email addresses in a file. The following code should work (and create the file if not already exists):

with AddressBook('contacts.txt') as ab:
    ab.add('Eve', 'eve@gmail.com')
    ab.add('Alice', 'alice@walla.co.il')

with AddressBook('contacts.txt') as ab:
   print(ab.email('Eve'))
   ab.add('Bob', bob@walla.co.il')

Modify the class so the following will also work (Hint: read about __getitem__):

with AddressBook('contacts.txt') as ab:
   	print(ab['Eve'])

d = defaultdict(int)
    for k, v in sorted(list(zip(sentence, [sentence.count(word) for word in sentence]))):
        d[k] += 1

    return d.items()
"""
from collections import defaultdict
import os


class AddressBook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_obj = open(file_name, 'r+')
        self.info = defaultdict(int)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def add(self, key, value):
        self.info[key] = value #Why it is  empty
        self.file_obj.write(f'{key}: {value} \n')

    def email(self, name):
        if os.stat(self.file_name).st_size == 0:
            print("AddressBook is empty")
        else:
            for line in self.file_obj.readlines():
                username, email = line.split(':')
                if username == name:
                    return email

    def __getitem__(self, key):
        return self.info[key]


if __name__ == '__main__':
    with AddressBook('contacts.txt') as ab:
        ab.add('Eve', 'eve@gmail.com')
        ab.add('Alice', 'alice@walla.co.il')

    with AddressBook('contacts.txt') as ab:
        print(ab.email('Eve'))
        ab.add('Bob', 'bob@walla.co.il')

    with AddressBook('contacts.txt') as ab:
        print(ab['Eve'])
