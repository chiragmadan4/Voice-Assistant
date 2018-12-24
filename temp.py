from datetime import date
import txttosp
import calendar
my_date = date.today()
txttosp.convertToAudio(str(my_date))
print(calendar.day_name[my_date.weekday()])

