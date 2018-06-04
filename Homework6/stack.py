class Stack:
    def __init__(self):
        self.items_list = []

    def add_item(self, *items):
        for item in items:
            self.items_list.append(item)

    def pop_item(self):
        if len(self.items_list) == 0:
            return 0
        return self.items_list.pop()

    def count_items(self):
        return len(self.items_list)
