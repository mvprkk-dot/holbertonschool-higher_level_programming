#!/usr/bin/python3

class CountedIterator:
    """An iterator that keeps track of the number of items iterated."""

    def __init__(self, data):
        """Initialize the iterator and the counter."""
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        """Override the next method to increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            # Əgər element bitibsə, StopIteration xətasını olduğu kimi ötürürük
            raise StopIteration
