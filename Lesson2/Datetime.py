from datetime import datetime, timedelta

# Задание
# Напечатайте в консоль даты: вчера, сегодня, месяц назад


dt = datetime.now()
delta = timedelta(days = 1)
one_day_ago = dt - delta
print(one_day_ago)
delta = timedelta(days = 30)
one_month_ego = dt - delta
print(one_month_ego)
#date now
print(datetime.now())


# Превратите строку "01/01/17 12:10:03.234567" в объект datetime
dstr = '01/01/17 12:10:03.234567'
date_strip = datetime.strptime(dstr, '%d/%m/%y %H:%M:%S.%f')
print(date_strip)

