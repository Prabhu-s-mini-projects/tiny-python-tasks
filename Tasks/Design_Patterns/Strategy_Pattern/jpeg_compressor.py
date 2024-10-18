"""
Class Name: JPEGCompressor.py
Blue+print of:compress the all jpeg images
"""
# Internal Dependencies
from Tasks.Design_Patterns.Strategy_Pattern.compressor import Compressor


class JPEGCompressor(Compressor):
    """
    Purpose: Blueprint of compress the all jpeg images
    Methods:
        compress : will compress the image
    """

    def print_doc_s(self) -> None:
        """print doc string for pylint fix """
        print("ignore this method")

    def compress(self) -> None:
        """ To perform: will compress the image"""
        print("compressing using JPEG compressor")
