"""
Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
Лінк на формат коди  для  дати
https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
"""
from datetime import *
import calendar
print(f'Current date and time {datetime.now()}')
print(f'Current year {datetime.now().year}')
print(f'Month of year {datetime.now().month}')
print(f'Week number of the year {datetime.now().isocalendar()[1]}')
print(f'Weekday of the week {datetime.now().isoweekday()}')
print(f'Day of year {datetime.now().now().timetuple().tm_yday}')
print(f'Day of the month {datetime.now().timetuple().tm_mday}')
print(f'Day of week {calendar.day_name[datetime.now().weekday()]}')
t = datetime.now()
print(t.strftime("%Y-%B-%d").format())
