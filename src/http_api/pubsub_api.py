import requests
from config import HTTP_API_KEY, APP_ID
from pprint import pprint

authorization = ("Authorization", f"Bearer {HTTP_API_KEY}")


def get_formats():
    headers = dict([authorization])
    response = requests.get('https://eu1.cloud.thethings.network/api/v3/as/pubsub-formats',
                            headers=headers)
    pprint(response.json())


def list_pubsub():
    headers = dict([authorization])
    response = requests.get(f'https://eu1.cloud.thethings.network/api/v3/as/pubsub/{APP_ID}',
                            headers=headers)
    pprint(response.json())


if __name__ == '__main__':
    # get_formats()
    list_pubsub()
