"""
Class Name: Compressor.py
Blue+print of:abstract class for all different types of extension
"""
# Dependencies
from abc import ABC, abstractmethod


class FilterImage(ABC):
    """
    Purpose: Blueprint of abstract class for all different types of extension
    """

    @abstractmethod
    def apply(self) -> None:
        """ To perform: apply filter to the image"""
