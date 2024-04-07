import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate the expected price
        expected_prices = [(quote['top_ask']['price'] + quote['top_bid']['price']) / 2 for quote in quotes]
        # Call getDataPoint function
        actual_prices = [getDataPoint(quote)[3] for quote in quotes]
        # Assert the calculated prices
        self.assertEqual(actual_prices, expected_prices, "Price calculation is incorrect")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate the expected price
        expected_prices = [(quote['top_ask']['price'] + quote['top_bid']['price']) / 2 for quote in quotes]
        # Call getDataPoint function
        actual_prices = [getDataPoint(quote)[3] for quote in quotes]
        # Assert the calculated prices
        self.assertEqual(actual_prices, expected_prices, "Price calculation is incorrect")

    def test_getRatio_non_zero_denominator(self):
        """
        Test getRatio function with non-zero denominator.
        """
        # Define test data
        price_a = 10
        price_b = 5
        # Call getRatio function
        actual_ratio = getRatio(price_a, price_b)
        # Calculate the expected ratio
        expected_ratio = price_a / price_b
        # Assert the result
        self.assertEqual(actual_ratio, expected_ratio, "getRatio returns incorrect ratio when denominator is non-zero")

    def test_getRatio_zero_denominator(self):
        """
        Test getRatio function with zero denominator.
        """
        # Define test data
        price_a = 10
        price_b = 0
        # Call getRatio function
        actual_ratio = getRatio(price_a, price_b)
        # Assert the result
        self.assertEqual(actual_ratio, 0, "getRatio returns incorrect ratio when denominator is zero")

if __name__ == '__main__':
    unittest.main()
