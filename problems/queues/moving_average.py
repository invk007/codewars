"""Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.
"""

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.queue.popleft()

        return sum(self.queue) / len(self.queue)
