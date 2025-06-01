#!/usr/bin/python3
"""
This module defines the CountedIterator class.
It wraps an iterator and counts how many items have been iterated.
"""


class CountedIterator:
    """Custom iterator that counts how many times it was iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)  # Will raise StopIteration automatically
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated."""
        return self.count

    def __iter__(self):
        """Return the iterator itself."""
        return self
