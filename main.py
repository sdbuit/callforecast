# main.py

import csv
import datetime
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt

def parse_datetime(dt_str):
    return datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')

def floor_to_interval(dt, interval_minutes=30):
    seconds = (dt.hour * 3600 + dt.minute * 60 + dt.second)
    interval = interval_minutes * 60
    floored_seconds = (seconds // interval) * interval
    hour = floored_seconds // 3600
    minute = (floored_seconds % 3600) // 60
    return dt.replace(hour=hour, minute=minute, second=0, microsecond=0)

def load_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                parsed = {
                    'contactId': int(row['contactId']),
                    'contactStart': parse_datetime(row['contactStart']),
                    'campaignId': int(row['campaignId']),
                    'abandoned': int(row['abandoned']),
                    'abandonseconds': float(row['abandonseconds']),
                    'inQueueSeconds': float(row['inQueueSeconds']),
                    'agentSeconds': float(row['agentSeconds'])
                }
                data.append(parsed)
            except Exception as e:
                print(f'Error parsing row: {row} -> {e}')
    return data

def group_and_average(data, field='agentSeconds', interval_minutes=30):
    groups = defaultdict(list)
    for row in data:
        dt = row['contactStart']
        floored_dt = floor_to_interval(dt, interval_minutes)
        groups[floored_dt].append(row[field])
    
    averages = {}
    for key, values in groups.items():
        averages[key] = sum(values) / len(values)
    return averages

def plot_averages(averages):
    sorted_times = sorted(averages.keys())
    avg_vals = [averages[time] for time in sorted_times]
    
    plt.figure()
    plt.plot(sorted_times, avg_vals, marker='o')
    plt.xlabel('Time (Floored to 30-min intervals)')
    plt.ylabel('Average Agent Seconds')
    plt.title('Average AgentSeconds by 30-min Interval')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    filename = 'calls.csv'
    data = load_csv(filename)
    # print(f'Loaded {len(data)} rows')
    averages = group_and_average(data, field='agentSeconds', interval_minutes=30)
    for time_key, avg in sorted(averages.items()):
        print(f"{time_key}: {avg:.2f}")
    plot_averages(averages)
