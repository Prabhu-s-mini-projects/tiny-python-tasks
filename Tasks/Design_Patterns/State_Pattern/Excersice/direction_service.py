"""
Class Name: DirectionService.py
Blue+print of:Contains 2 methods get eta and direction btw 2 points
"""
# Internal Dependencies
from Tasks.Design_Patterns.State_Pattern.Excersice.travel_mode import TravelMode


class DirectionService:
    """
    Purpose: Blueprint of Contains 2 methods get eta and direction btw 2 points
    Attributes:
        travel_mode : ENUM
    Methods:
        get_eta : Calculates the estimated time of arrival
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            travel_mode : T
        """
        self.travel_mode: TravelMode = kwargs.get("travel_mode")

    def get_eta(self) -> int:
        """ To perform: Calculates the estimated time of arrival"""
        return self.travel_mode.get_eta()

        # Below code is replaced by state pattern
        # if self.travel_mode == TravelMode.DRIVING :
        #     print("Calculating ETA (driving)")
        #     return 1
        # elif self.travel_mode == TravelMode.BICYCLING:
        #     print("Calculating ETA (bicycling)")
        #     return 2
        # elif self.travel_mode == TravelMode.TRANSIT:
        #     print("Calculating ETA (transit)")
        #     return 3
        # else:
        #     print("Calculating ETA (walking)")
        #     return 4

    def get_direction(self) -> int:
        """Returns a direction to the user based on the current position"""
        return self.travel_mode.get_direction()

        # Replaced by state pattern
        # if self.travel_mode == TravelMode.DRIVING:
        #     print("Calculating ETA (driving)")
        #     return 1
        # elif self.travel_mode == TravelMode.BICYCLING:
        #     print("Calculating ETA (bicycling)")
        #     return 2
        # elif self.travel_mode == TravelMode.TRANSIT:
        #     print("Calculating ETA (transit)")
        #     return 3
        # else:
        #     print("Calculating ETA (walking)")
        #     return 4
