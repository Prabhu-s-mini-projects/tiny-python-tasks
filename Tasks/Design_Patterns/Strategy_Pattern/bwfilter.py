"""
Class Name: BWFilter.py
Blue+print of:apply black and white filter to an image
"""
# Internal Dependencies
from Tasks.Design_Patterns.Strategy_Pattern.filter_image import FilterImage


class BWFilter(FilterImage):
    """
    Purpose: Blueprint of apply black and white filter to an image
    Methods:
        apply : apply the black and white filter
    """

    def apply(self) -> None:
        """ To perform: apply the black and white filter"""
        print("Applying B&W filter")
