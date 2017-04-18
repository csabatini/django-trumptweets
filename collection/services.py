import requests

base_url = 'https://trumptweets.slickmobile.us/'


def get_tags():
    r = requests.get(base_url + 'api/v1/tag')
    return {'tags': r.json()}
