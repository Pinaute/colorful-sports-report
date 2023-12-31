import datetime
import random
import csv

current_year = datetime.date.today().year
start_date = datetime.date(current_year, 1, 1)
end_date = datetime.date(current_year, 12, 31)

activities = ['notraining', 'run', 'cycle', 'swim', 'ski', 'sail', 'judo', 'runandbike', 'tenis', 'surf', 'sandyacht', 'hike', 'canoe']
dot_size = 100
achievement = 0

items = [{'Date': start_date + datetime.timedelta(days=x),
          'Activity': random.choice(activities),
          'Dot_size': dot_size,
          'Achievement': achievement} for x in range((end_date - start_date).days + 1)]

for item in items:
    if item['Activity'] == 'notraining':
        item['Dot_size'] = 50  # You can use an integer here

with open('sports_activities.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Activity', 'Dot_size', 'Achievement'])
    for item in items:
        writer.writerow([item['Date'], item['Activity'], item['Dot_size'], item['Achievement']])
