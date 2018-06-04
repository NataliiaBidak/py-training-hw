 # Given a dictionary. For each value return its key.
class dict(dict):
    def get_key(self, value):
        for a in dict.keys(self):
            if dict.get(self, a) == value:
                return a


a = dict({'Name': 'Zara', 'Age': 7, 'Class': 'First'})
c= dict.copy(a)
print(c['Name'])
b = a.get_key('First')
print(b)




# Create list in next format: db = [{‘id’: int, name: ‘John Doe’, ‘age’: int, ‘sex’: sex, ‘adress’: adress, ‘fav_books’: [‘book1’, ‘book2’, ... ], pets: [], ...}, {id: int, ...}]
db = [{'id': 1, 'name': 'John Doe', 'age': 27, 'sex':'Male', 'adress': 'Lviv', 'fav_books': ['book1', 'python', 'book3'], 'pets': ['frog', 'rat', 'chicken']},
      {'id': 2, 'name': 'Alina Brown', 'age': 217, 'sex':'Female', 'adress': 'Kyiv', 'fav_books': ['c++', 'c', 'cars'], 'pets': ['dinosaur', 'bunny', 'bird']}]
print(len(db))
print ('first name is', db[0]['name'].split(' ', 1)[0],'last name is',db[0]['name'].split(' ', 1)[1])
print('i am',db[0]['name'],'my favorite books are',', '.join(db[0]['fav_books']))
for item in db:
    print(item['name'])
print(db[1]['fav_books'])

# Prepare at least 3 ways to create a dictionary.
dict1 = {}
t = ((1, 'a'),(2, 'b'))
dict2 = dict((y, x) for x, y in t)


names = ["Nick", "Alice", "Kitty"]
professions = ["Programmer", "Engineer", "Art Therapist"]

dict3 = {}
for i in range(len(names)):
   dict3[names[i]] = professions[i]
# 1
name = "Nataliia"
print('Hello, %s' % name)
# 2
print('Hello, {}'.format(name))
# 3
print(f'Hello, {name}')
# 4
from string import Template
print(Template('Hello, $name!').substitute(name=name))
