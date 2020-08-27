from typing import List
import math
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_profit = 0
        lowest_stock_price = -math.inf

        for price in prices:
            if lowest_stock_price + price > running_profit:
                running_profit = lowest_stock_price + price

            if -price > lowest_stock_price:
                lowest_stock_price = -price

        return running_profit

    def max_profit_no_transaction_limit(self, prices: List[int]):
        profit = 0
        yesterday_sp = -math.inf

        for price in prices:
            if yesterday_sp + price > 0:
                profit += yesterday_sp+price

            yesterday_sp = -price

        return profit


class Test(unittest.TestCase):

    def test_no_transaction_limit(self):
        s = Solution()
        actual = s.max_profit_no_transaction_limit([0, 100, 0, 100, 0, 100])
        self.assertEqual(actual, 300)
        actual = s.max_profit_no_transaction_limit([100, 100, 80, 20])
        self.assertEqual(actual, 0)
        actual = s.max_profit_no_transaction_limit([0, 50, 10, 100, 30])
        self.assertEqual(actual, 140)
        actual = s.max_profit_no_transaction_limit([100, 40, 20, 10])
        self.assertEqual(actual, 0)

    def test_price_goes_up_then_down(self):
        actual = Solution().maxProfit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = Solution().maxProfit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = Solution().maxProfit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = Solution().maxProfit([9, 7, 4, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = Solution().maxProfit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
