from . import http_client


class NseApi:
    _NSE_STOCK_DATA_INDEX_BASED: str
    _NSE_EQUITY_MASTER: str

    def __init__(self):
        self._NSE_EQUITY_MASTER = "https://www.nseindia.com/api/equity-master"

        self._NSE_STOCK_DATA_INDEX_BASED = "https://www.nseindia.com/api/equity-stockIndices"
        self.NSE_STOCK_DATA_INDEX_BASED_PARAMS = lambda index: {'index': index}

    def get_top_gainers(self, index, top_n):
        r = http_client.get(self._NSE_STOCK_DATA_INDEX_BASED, self.NSE_STOCK_DATA_INDEX_BASED_PARAMS(index))
        if not r.ok:
            raise Exception("Failed to call " + "https://www.nseindia.com/api/equity-stockIndices")
        dict_stocks = r.json()['data']
        # Exclude index from the list
        dict_stocks = [stock for stock in dict_stocks if stock['priority'] == 0]
        dict_stocks.sort(key=lambda stock: (stock['pChange']), reverse=False)
        dict_stocks = dict_stocks[:top_n]
        return dict_stocks

    def dummy_method(self, input_1: object) -> object:
        return input_1
