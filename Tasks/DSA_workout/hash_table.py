"""
Class Name: HashTable.py
Blue+print of:hashtable of year
"""
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

    def __hash_method(self,key: str) -> int:
        """ To perform: will use the hash method"""
        if isinstance(key,str):
            # for string
            index = 0
            for c in key:
                # using 23 a prime number to more variance
                # to avoid collusion
                index = (index + ord(c) * 23)% len(self.map_table)
            print(f"{ index = } ")
            return index
        # if not a type string
        raise ValueError("Invalid Key")

    def get_index(self,key:str)-> int:
        """will return the index"""
        return self.__hash_method(key)
