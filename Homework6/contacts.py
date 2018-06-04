class Contacts:
    def __init__(self, list_of_contacts={}):
        self.list_of_contacts = list_of_contacts

    def add(self, name, info):
        self.list_of_contacts.update({name: info})

    def contacts_by_lives_in(self, country):
        list_of_names = []
        for name, info in self.list_of_contacts.items():
            if country in info['lives_in']:
                list_of_names.append(name)
        return list_of_names
