import requests
import json

api_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'


def get_response(url):
    return requests.get(url)


def my_name():
    return input('Enter a name: ')


if __name__ == '__main__':
    print(__name__)
    my_name()
    # response = get_response(api_url)
    # print(response)
