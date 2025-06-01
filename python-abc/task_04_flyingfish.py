#!/usr/bin/python3
"""
This module defines classes for Fish, Bird, and FlyingFish.
FlyingFish inherits from both Fish and Bird and overrides their methods.
"""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish that can both swim and fly."""

    def swim(self):
        """Print a custom swimming message for the flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print a custom flying message for the flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
