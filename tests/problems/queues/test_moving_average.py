from problems.queues.moving_average import MovingAverage


def test_moving_average_next():
    ma = MovingAverage(size=3)
    vals = [1, 10, 3, 5]
    result = [ma.next(val) for val in vals]
    assert result == [1 / 1, 11 / 2, 14 / 3, 18 / 3]
