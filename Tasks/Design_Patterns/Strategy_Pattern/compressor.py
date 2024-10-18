"""
Class Name: Compressor.py
Blue+print of:abstract class for all different types of extension
"""
# Dependencies
from abc import ABC, abstractmethod


class Compressor(ABC):
    """
    Purpose: Blueprint of abstract class for all different types of extension
    """

    @abstractmethod
    def compress(self) -> None:
        """ To perform: compress the image"""
