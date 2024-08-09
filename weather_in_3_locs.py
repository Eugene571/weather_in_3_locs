import requests


def main():
    places = [
        'london',
        'svo',
        'череповец',
    ]

    for place in places:
        wtr_in_console = requests.get('https://ru.wttr.in/' + place + '?n&lang=ru&?M&?q&?T')
        wtr_in_console.raise_for_status()
        print(wtr_in_console.text)


if __name__ == '__main__':
    main()
