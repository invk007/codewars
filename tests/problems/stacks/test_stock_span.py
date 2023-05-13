from problems.stacks.stock_span import StockSpanner


def test_stock_spanner_next():
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    assert [spanner.next(price) for price in prices] == expected
