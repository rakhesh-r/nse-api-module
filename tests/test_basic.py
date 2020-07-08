from .context import nseapi
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @classmethod
    def setUpClass(cls) -> None:
        """setup"""
        cls._nse_api = nseapi.NseApi()

    def test_dummy_method(self):
        input_1: bool = True
        assert input_1 == self._nse_api.dummy_method(input_1)

    def test_get_top_gainers(self):
        output = self._nse_api.get_top_gainers('NIFTY 50', 5)
        assert len(output) == 5


if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
