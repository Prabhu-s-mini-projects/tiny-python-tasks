"""
App_Name: Map app
Purpose: Uses Direction class to get ETA and Direction to another point
"""
# Internal modules
from Tasks.Design_Patterns.State_Pattern.Excersice.direction_service import DirectionService
from Tasks.Design_Patterns.State_Pattern.Excersice.driving import DrivingMode


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Map app
    to do Uses Direction class to get ETA and Direction to another point
    """
    # To do
    driving_service = DirectionService()

    driving_service.travel_mode = DrivingMode()
    print(f"{ driving_service.get_eta() = } ")
    print(f"{ driving_service.get_direction() = } ")


if __name__ == '__main__':
    main()
