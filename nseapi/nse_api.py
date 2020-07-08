from . import http_client


class NseApi:
    _NSE_STOCK_DATA_INDEX_BASED: str
    _NSE_EQUITY_MASTER: str

    def __init__(self):
        self._NSE_EQUITY_MASTER = "https://www.nseindia.com/api/equity-master"

        self._NSE_STOCK_DATA_INDEX_BASED = "https://www.nseindia.com/api/equity-stockIndices"
        self._NSE_STOCK_DATA_INDEX_BASED_PARAMS = lambda index: {'index': index}

    def get_top_n_gainers(self, index, top_n):
        dict_stocks = self._get_stocks_by_index(index)
        dict_stocks.sort(key=lambda stock: (stock['pChange']), reverse=True)
        dict_stocks = dict_stocks[:top_n]
        return dict_stocks

    def get_top_n_losers(self, index, top_n):
        dict_stocks = self._get_stocks_by_index(index)
        dict_stocks.sort(key=lambda stock: (stock['pChange']), reverse=False)
        dict_stocks = dict_stocks[:top_n]
        return dict_stocks

    def get_top_gainers_above_perc(self, index, perc):
        dict_stocks = self._get_stocks_by_index(index)
        dict_stocks = [stock for stock in dict_stocks if stock['pChange'] >= perc]
        return dict_stocks

    def get_top_losers_below_perc(self, index, perc):
        dict_stocks = self._get_stocks_by_index(index)
        dict_stocks = [stock for stock in dict_stocks if stock['pChange'] <= perc]
        return dict_stocks

    def _get_stocks_by_index(self, index):
        r = http_client.get(self._NSE_STOCK_DATA_INDEX_BASED, self._NSE_STOCK_DATA_INDEX_BASED_PARAMS(index))
        if not r.ok:
            raise Exception("Failed to call " + "https://www.nseindia.com/api/equity-stockIndices")
        dict_stocks = r.json()['data']
        # Exclude index from the list
        dict_stocks = [stock for stock in dict_stocks if stock['priority'] == 0]
        return  dict_stocks
