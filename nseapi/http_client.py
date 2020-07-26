import requests


def get(url, params):
    return requests.get(url, headers=__get_headers(), params=params)


def __get_headers():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Host': 'www.nseindia.com',
               'Accept-Encoding': 'gzip, deflate, br'}
    return headers

# print(get(
#    'https://www.nseindia.com/api/historical/cm/equity?symbol=TECHM&series=[%22EQ%22]&from=01-07-2020&to=01-07-2020', None))
