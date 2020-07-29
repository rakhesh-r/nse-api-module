from . import http_client
from . import utils


class NseApi:

    def __init__(self):
        self._NSE_EQUITY_MASTER = "https://www.nseindia.com/api/equity-master"

        self._NSE_STOCK_DATA_INDEX_BASED = "https://www.nseindia.com/api/equity-stockIndices"
        self._NSE_STOCK_DATA_INDEX_BASED_PARAMS = lambda index: {'index': index}

        self._NSE_STOCK_DATA_HISTORICAL_DAY = "https://www.nseindia.com/api/historical/cm/equity"
        self._NSE_PARAM_SERIES_EQ = '["EQ"]'
        self._NSE_STOCK_DATA_HISTORICAL_DAY_PARAMS = lambda symbol, series, from_date, to_date: {'symbol': symbol,
                                                                                                 'series': series,
                                                                                                 'from': from_date,
                                                                                                 'to': to_date
                                                                                                 }
        self._NSE_STOCK_INFO_BY_SYMBOL = "https://www.nseindia.com/api/quote-equity"
        self._NSE_STOCK_INFO_BY_SYMBOL_PARAMS = lambda symbol: {'symbol': symbol}

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
        return dict_stocks

    # Max of 60 days
    def get_historical_day_data_days(self, symbol, days_from_today: int):
        if days_from_today > 60:
            raise Exception("days_from_today max value is 60 days ")
        r = http_client.get(self._NSE_STOCK_DATA_HISTORICAL_DAY,
                            self._NSE_STOCK_DATA_HISTORICAL_DAY_PARAMS(
                                symbol=symbol,
                                from_date=utils.get_date_before_n_days(None, days_from_today),
                                to_date=utils.get_today_date(),
                                series=self._NSE_PARAM_SERIES_EQ))
        if not r.ok:
            raise Exception("Exception", r)

        return r.json()['data']

    # Date format DD-MM-YYYY
    # It can return max 60 days of data
    def get_historical_day_data_dates(self, symbol, from_date, to_date):
        days = utils.get_difference_dates(from_date=from_date, to_date=to_date)
        if days > 60:
            to_date = utils.get_date_after_n_days(from_date=from_date, n_days=60)
        r = http_client.get(self._NSE_STOCK_DATA_HISTORICAL_DAY,
                            self._NSE_STOCK_DATA_HISTORICAL_DAY_PARAMS(symbol=symbol, from_date=from_date,
                                                                       to_date=to_date,
                                                                       series=self._NSE_PARAM_SERIES_EQ))
        if not r.ok:
            raise Exception("Exception", r)

        return r.json()['data']

    def get_stock_info_by_symbol(self, symbol):
        r = http_client.get(self._NSE_STOCK_INFO_BY_SYMBOL, self._NSE_STOCK_INFO_BY_SYMBOL_PARAMS(symbol))
        if not r.ok:
            raise Exception("Failed to call " + self._NSE_STOCK_INFO_BY_SYMBOL)
        dict_stocks = r.json()
        return dict_stocks
