"""
Write a Python program to subtract five days from current date.
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17)

"""
from datetime import datetime, timedelta
new_date = datetime.now().date() - timedelta(5)

print(f'Current Date {datetime.now().date()}')
print(f'5 days before Current Date {new_date}')

print(timedelta.__doc__)