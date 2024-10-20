"""
App_Name: Strategy pattern
Purpose: Contains implementation of a strategy-pattern
"""
from Tasks.Design_Patterns.Strategy_Pattern.bwfilter import BWFilter
# Internal modules
from Tasks.Design_Patterns.Strategy_Pattern.image_storage import ImageStorage
from Tasks.Design_Patterns.Strategy_Pattern.jpeg_compressor import JPEGCompressor


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Strategy pattern
    to do Contains implementation of a strategy pattern
    """
    # To do
    print(
        """
        Strategy Pattern: 
        It's a behavioral design pattern that lets you define a family of algorithms,
        put each of them into a separate class, and make their objects interchangeable.
        """
    )
    image_storage = ImageStorage()
    image_storage.store("newfile", JPEGCompressor(), BWFilter())
    # image_storage.store("newfile", "PNG", "B&W filter")
    # image_storage.store("newfile", "JPEG", "High contrast")


if __name__ == '__main__':
    main()
