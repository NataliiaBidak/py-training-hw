"""
Write a Python program to convert a string to datetime.
Sample String : Jan 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00

"""
from datetime import datetime

print(datetime.strptime('Jan 1 2014 2:43PM', '%b %d %Y %I:%M%p'))

