"""
Write the class AddressBook so the following code works:
c = AddressBook()

c.add(name='ynon', email='ynon@ynonperek.com', likes='red')
c.add(name='bob', email='bob@gmail.com', likes='blue')
c.add(name='ynon', email='ynon@gmail.com', likes='blue')

c.find_by(name='ynon')
# returns:
# [
#   {'name': 'ynon', 'email': 'ynon@ynonperek.com', 'likes': 'red'},
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]

c.find_by(likes='blue)
# returns:
# [
#   { 'name': 'bob', 'email': 'bob@gmail.com', 'likes': 'blue' },
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]

"""


class AddressBook:
    def __init__(self):
        self.list_of_people = []

    def add(self, name=None, email=None, likes=None):
        info = {}
        info['name'] = name
        info['email'] = email
        info['likes'] = likes
        self.list_of_people.append(info)

    def find_by(self, name=None, likes=None):
        if name:
            print([x for x in self.list_of_people if x['name'] == name])
        elif likes:
            print([x for x in self.list_of_people if x['likes'] == likes])


if __name__ == '__main__':
    c = AddressBook()

    c.add(name='ynon', email='ynon@ynonperek.com', likes='red')
    c.add(name='bob', email='bob@gmail.com', likes='blue')
    c.add(name='ynon', email='ynon@gmail.com', likes='blue')

    c.find_by(name='ynon')
    c.find_by(likes='blue')
