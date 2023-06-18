import csv
import datetime
import random

current_year = datetime.date.today().year
start_date = datetime.date(current_year, 1, 1)
end_date = datetime.date(current_year, 12, 31)

activities = ['slacking', 'running', 'cycling', 'swimming', 'skiing', 'fencing', 'sailing']
dot_size = 300
achievement = 0

items = [(start_date + datetime.timedelta(days=x), random.choice(activities), dot_size, achievement) for x in range((end_date - start_date).days + 1)]

with open('working_base.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Activity', 'Dot_size', 'Achievement'])
    for item in items:
        writer.writerow([item[0], item[1], item[2], item[3]])
