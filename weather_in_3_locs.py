import requests


def main():
    places = [
        'london',
        'svo',
        'череповец',
    ]

    for place in places:
        payload = {
            'M': '',
            'n': '',
            'q': '',
            'T': '',
        }
        weather_response = requests.get(f'https://ru.wttr.in/{place}', params=payload)
        weather_response.raise_for_status()
        print(weather_response.text)


if __name__ == '__main__':
    main()
