#!/usr/bin/env python3
"""Abstract Animal Class and Subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class implementing sound method."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class implementing sound method."""

    def sound(self):
        return "Meow"
