import pandas as pd
from datetime import datetime

file_path = '/var/log/syslog'

with open(file_path, 'r') as file:
    log_lines = file.readlines()

logs = []

for line in log_lines:
    parts = line.split()
    if len(parts) > 4:
        timestamp = parts[0] 
        user = parts[1]
        service = ' '.join(parts[2:3])
        message = ' '.join(parts[4:])

        logs.append({
            'timestamp': timestamp,
            'user': user,
            'service': service,
            'message': message,
        })

df = pd.DataFrame(logs)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute
df['second'] = df['timestamp'].dt.second
df['microsecond'] = df['timestamp'].dt.microsecond
df['timezone'] = df['timestamp'].dt.tz

print(df.tail())

df.to_csv("syslog.csv")

print(df['user'].count())
