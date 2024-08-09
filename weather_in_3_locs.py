import requests

locs = [
    'london',
    'svo',
    'череповец',
]

for loc in locs:
    res = requests.get('https://ru.wttr.in/' + loc + '?n&lang=ru&?M&?q&?T')
    res.raise_for_status()
    print(res.text)
