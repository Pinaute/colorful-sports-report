import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import calendar
import csv

activity_colors = {
    "slacking":"#e3e3e3", #grey
    "running":"#ff7c3b", #orange
    "cycling": "#55d781", #green
    "swimming": "#fdd300", #yellow
    "skiing": "#db57b1", #pink
    "fencing": "#6289fe", #bleu
    "sailing": "#a177f2", #violet
}

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

df = pd.read_csv('sports_activities.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month - 1
df['Day'] = df['Date'].dt.day - 1

year = df['Date'].dt.year[0]

fig, ax = plt.subplots(figsize=(12, 12), dpi=80)

for i, month_name in enumerate(calendar.month_name[1:]):
    month_data = df.loc[df['Month'] == i]
    colors = month_data['Activity'].apply(activity_to_color)

    dot_size = month_data['Dot_size']
    ax.scatter(month_data['Month'], month_data['Day'], c=colors, s=dot_size, alpha=1, edgecolors='none')

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

order = [2, 1, 3, 0, 6, 5, 4]
handles = []
labels = []

activity_counts = count_activities('sports_activities.csv')

for activity, values in activity_counts.items():
    count = values['count']
    color = values['color']
    handles.append(Line2D([], [],  color=color, marker='o', markersize=10, linestyle='None'))
    labels.append(f'{activity} ({count})')

plt.legend([handles[i] for i in order], [labels[i] for i in order], loc='upper center', bbox_to_anchor=(0.5, -0.02), fancybox=True, shadow=False, ncol=7)

plt.show()

fig.savefig('calendar_heatmap.png', dpi=300, format="png", bbox_inches="tight")
