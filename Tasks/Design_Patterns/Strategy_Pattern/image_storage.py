"""
Class Name: ImageStorage.py
Blue+print of:storage that will compress and apply filter to the image
"""
# Internal Dependencies
from Tasks.Design_Patterns.Strategy_Pattern.compressor import Compressor
from Tasks.Design_Patterns.Strategy_Pattern.filter_image import FilterImage


class ImageStorage:
    """
    Purpose: Blueprint of storage that will compress and apply filter to the image
    """

    def print_doc_str(self) -> None:
        """print doc string for pylint fix """
        print("ignore this method")

    def store(self, filename: str,
              compressor: Compressor,
              filter_image: FilterImage) -> None:
        """ To perform: Compressing the image and apply the filter"""

        # Compressing the image
        compressor.compress()

        # applying the filter
        filter_image.apply()

        # without strategy pattern
        #
        # # Compressing the images based on the type
        # if compressor == "JPEG":
        #     print("compressing using JPEG compressor")
        # elif compressor == "PNG":
        #     print("compressing using PNG compressor")
        # else:
        #     print("Compressing a without extension compressor")
        #
        # # Applying the filter
        # if filter_image == "B&W filter":
        #     print("Applying B&W filter")
        # elif filter_image == "High contrast":
        #     print("Applying High contrast filter")
        # else:
        #     print("No filter applied")

        print(f"{filename} is stored")
