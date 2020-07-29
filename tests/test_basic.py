from .context import nseapi
import unittest
import random


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @classmethod
    def setUpClass(cls) -> None:
        """setup"""
        print(__name__)
        cls._nse_api = nseapi.NseApi()
        cls._utils = nseapi.utils

    def test_get_top_n_gainers(self):
        print("Test test_get_top_n_gainers")
        output = self._nse_api.get_top_n_gainers('NIFTY 50', 5)
        print(output)
        assert len(output) == 5

    def test_get_top_n_losers(self):
        print("Test test_get_top_n_losers")
        output = self._nse_api.get_top_n_losers('NIFTY 50', 10)
        print(output)
        assert len(output) == 10

    def test_get_top_gainers_above_perc(self):
        print("Test test_get_top_gainers_above_perc")
        output = self._nse_api.get_top_gainers_above_perc('NIFTY 50', 2.5)
        print(output)
        if len(output) > 0:
            assert output[random.randint(0, len(output) - 1)]['pChange'] >= 2.5
        else:
            assert True

    def test_get_top_losers_below_perc(self):
        print("Test test_get_top_losers_below_perc")
        output = self._nse_api.get_top_losers_below_perc('NIFTY 50', -4.62)
        print(output)
        if len(output) > 0:
            assert output[random.randint(0, len(output) - 1)]['pChange'] <= -4.62
        else:
            assert True

    def test_get_historical_day_data_dates(self):
        print("Test test_get_historical_day_data_dates")
        output = self._nse_api.get_historical_day_data_dates(symbol='TECHM',
                                                             from_date='01-05-2020', to_date='31-05-2020')
        print(output)
        assert len(output) == 19

    # This test case fails if you run next day of a holiday
    def test_get_historical_day_data_days(self):
        print("Test test_get_historical_day_data_days")
        output = self._nse_api.get_historical_day_data_days(symbol='TECHM', days_from_today=1)
        print(output)
        assert len(output) == 1 or len(output) == 2

    def test_get_difference_dates(self):
        print("Test test_get_difference_dates")
        output = self._utils.get_difference_dates('01-07-2020', '13-07-2020')
        assert output == 12

    def test_get_date_after_n_days(self):
        print("Test test_get_date_after_n_days")
        output = self._utils.get_date_after_n_days(from_date='01-07-2020', n_days=5)
        assert output == '06-07-2020'

    def test_get_date_before_n_days(self):
        print("Test test_get_date_before_n_days")
        output = self._utils.get_date_before_n_days(to_date='06-07-2020', n_days=5)
        assert output == '01-07-2020'

    def test_get_stock_info_by_symbol(self):
        print("Test test_get_stock_info_by_symbol")
        output = self._nse_api.get_stock_info_by_symbol('INFY')
        assert output['info']['symbol'] == 'INFY'


if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
