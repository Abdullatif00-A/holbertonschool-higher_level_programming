#!/usr/bin/python3
"""Student class module."""


class Student:
    """A class to be jsonified."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary with filter"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {name: value for name, value in self.__dict__.items()
                    if name in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Load attributes from json ."""
        for key, value in json.items():
            setattr(self, key, value)
