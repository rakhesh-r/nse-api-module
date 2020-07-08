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
            assert output[random.randint(0, len(output))]['pChange'] >= 2.5
        else:
            assert True

    def test_get_top_losers_below_perc(self):
        print("Test test_get_top_losers_below_perc")
        output = self._nse_api.get_top_losers_below_perc('NIFTY 50', -4.62)
        print(output)
        if len(output) > 0:
            assert output[random.randint(0, len(output))]['pChange'] <= -4.62
        else:
            assert True


if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
