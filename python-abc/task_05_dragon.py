#!/usr/bin/python3
"""
This module defines mixins and a Dragon class that uses them.
SwimMixin and FlyMixin provide modular swimming and flying capabilities.
"""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        """Print a message indicating the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        """Print a message indicating the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A mythical dragon that can swim and fly."""

    def roar(self):
        """Print a roar message specific to dragons."""
        print("The dragon roars!")
