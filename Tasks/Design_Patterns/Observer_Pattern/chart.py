"""
Class Name: Chart.py
Blue+print of:visual_representation of data
"""
# Internal Dependencies
from Tasks.Design_Patterns.Observer_Pattern.observer import Observer

class Chart(Observer):
    """
    Purpose: Blueprint of visual_representation of data
    Methods:
        plot : plot the chart
    """

    def plot(self) -> None:
        """ To perform: plot the chart"""
        print("plot the chart")

    def update(self)-> None:
        """update the values of  a chart """
        print("chart value is updated")
