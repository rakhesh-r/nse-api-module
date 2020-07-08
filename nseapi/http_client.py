import requests


def get(url, params):
    return requests.get(url, headers=_get_headers(), params=params)


def _get_headers():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Host': 'www.nseindia.com'}
    return headers
