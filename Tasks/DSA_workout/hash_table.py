"""
Class Name: HashTable.py
Blue+print of:hashtable of year
"""
from pandas.conftest import index


# Dependencies

# Internal Dependencies

# CONSTANTS

class HashTable:
    """
    Purpose: Blueprint of hashtable of year
    Attributes:
        map_table : list
    Methods:
        __hash_method : will use the hash method
    """

    def __init__(self, size: int = 7):
        """
        Attributes:
            map_table : list
        """
        self.map_table: list = [None] * size

    def __hash_method(self,key:any) -> int:
        """ To perform: will use the hash method"""
        if type(key) == "str":
            # for string
            index = 0
            for c in key:
                # using 23 a prime number to more variance
                # to avoid collusion
                index = (index + ord(c) * 23)% len(self.map_table)
            print(f"{ index = } ")
            return index
        elif type(key) == "int":
            pass
        else:
            raise " It has to string or int"

