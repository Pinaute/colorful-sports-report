import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import calendar
import csv

activity_colors = {
    "notraining":"#A9B1B2", #Silver
    "run": "#ff8c00", #Dark_orange
    "cycle": "#55d781", #Emerald
    "swim": "#6289fe", #Cornflower_blue
    "ski": "#ff69b4", #Hot_Pink
    "sail": "#00ced1", #Dark_turquoise
    "judo": "#1C110A", #Licorice
    "runandbike": "#ff6347", #Tomato
    "tenis": "#008080", #Teal
    "surf": "#8a2be2", #Blue_violet
    "sandyacht": "#ffd700", #Gold
    "hike": "#C4621C", #Alloy_orange
    "canoe": "#BF211E", #Cornell_red
}

csv_input = 'sports_activities.csv'

def activity_to_color(activity):
    return activity_colors.get(activity)

def count_activities(csv_file):
    activity_counts = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            activity = row['Activity']
            if activity in activity_counts:
                activity_counts[activity] += 1
            else:
                activity_counts[activity] = 1

    activity_colors_counts = {}
    for activity, count in activity_counts.items():
        color = activity_colors.get(activity, '#e3e3e3')
        activity_colors_counts[activity] = {'count': count, 'color': color}

    return activity_colors_counts

df = pd.read_csv(csv_input)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month - 1
df['Day'] = df['Date'].dt.day - 1

year = df['Date'].dt.year[0]

fig, ax = plt.subplots(figsize=(10, 15))

for i, month_name in enumerate(calendar.month_name[1:]):
    month_data = df.loc[df['Month'] == i]
    colors = month_data['Activity'].apply(activity_to_color)
    size = month_data['Dot_size']
    ax.scatter(month_data['Month'], month_data['Day'], c=colors, s=size, alpha=1, edgecolors='none')

month_abbr = calendar.month_abbr[1:]

ax.set_title('Review of the year', loc='left', weight='bold', fontsize = 16, y=1.05)
ax.set_title(str(year), loc='right', weight='bold', fontsize = 16, y=1.05)
ax.set_xticks(np.arange(len(month_abbr)))
ax.set_xticklabels(month_abbr)
ax.set_yticks(np.arange(0, 31, 1))
ax.set_yticklabels(range(1, 32, 1))
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.set(frame_on=True)

order = [0, 11, 2, 1, 5, 3, 12, 10, 8, 9, 4, 7, 6]
handles = []
labels = []

activity_counts = count_activities(csv_input)

for activity, values in activity_counts.items():
    count = values['count']
    color = values['color']
    handles.append(Line2D([], [],  color=color, marker='o', markersize=8, linestyle='None'))
    labels.append(f'{activity} ({count})')

plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper center', bbox_to_anchor=(0.5, -0.02), fancybox=True, shadow=False, ncol=7, handletextpad=.1)

# plt.show() #Uncomment to get a preview

fig.savefig('calendar_heatmap.png', dpi=150, format="png")
