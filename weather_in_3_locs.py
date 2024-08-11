import requests


def main():
    places = [
        'london',
        'svo',
        'череповец',
    ]

    for place in places:
        payload = {
            'lang=ru': '',
            'M': '',
            'n': '',
            'q': '',
            'T': '',
        }
        weather_reqs = requests.get(f'https://wttr.in/{place}', params=payload)
        weather_reqs.raise_for_status()
        print(weather_reqs.text)


if __name__ == '__main__':
    main()
