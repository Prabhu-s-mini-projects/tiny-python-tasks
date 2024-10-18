"""
Class Name: DrivingMode.py
Blue+print of:driving mode: indicates driving in car
"""
# Internal Dependencies
from Tasks.Design_Patterns.State_Pattern.Excersice.travel_mode import TravelMode


class DrivingMode(TravelMode):
    """
    Purpose: Blueprint of driving mode: indicates driving in car
    """

    def get_eta(self) -> int:
        """ returns the eta"""
        print("Calculating ETA (driving)")
        return 1

    def get_direction(self) -> int:
        """ returns the direction"""
        print("Calculating Direction (driving)")
        return 1
