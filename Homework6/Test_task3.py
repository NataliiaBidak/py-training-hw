import unittest
from stack import Stack

class TestStack(unittest.TestCase):
   def test_flow(self):
       self.test_stack = Stack()

       self.test_stack.add_item(10)
       self.test_stack.add_item(20)
       self.test_stack.add_item(22, 33)
       assert self.test_stack.pop_item() == 33
       assert self.test_stack.pop_item() == 22

       assert self.test_stack.count_items() == 2

       while self.test_stack.pop_item(): pass

       assert self.test_stack.count_items() == 0