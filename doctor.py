from datetime import timedelta

free = []
d = timedelta(minutes=30)
start = [timedelta(hours=21)]
stop = [timedelta(hours=9)]

busy = [{'start': '10:30',
         'stop': '10:50'
         },
        {'start': '18:40',
         'stop': '18:50'
         },
        {'start': '14:40',
         'stop': '15:50'
         },
        {'start': '16:40',
         'stop': '17:20'
         },
        {'start': '20:05',
        'stop': '20:20'
         }]

for i in busy:
    start += [timedelta(hours=int(i['start'][0:2]), minutes=int(i['start'][3:5]))]
    stop += [timedelta(hours=int(i['stop'][0:2]), minutes=int(i['stop'][3:5]))]

start.sort(), stop.sort()

for i in range(0, len(busy)+1):
    while start[i]-stop[i] >= d:
        free += [stop[i]]
        stop[i] += d

print('Свободные полу-часовые окна врача:', *free, sep='\n')
