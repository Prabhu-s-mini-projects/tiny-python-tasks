"""
App_Name: Observer Pattern
Purpose: Implementation of observer pattern
"""# Internal modules
from Tasks.Design_Patterns.Observer_Pattern.chart import Chart
from Tasks.Design_Patterns.Observer_Pattern.datasource import DataSources
from Tasks.Design_Patterns.Observer_Pattern.spreadsheet import SpreadSheet


# Methods-------------------------------------------------------------------

def main() -> None:
    """
    Here is the Starting point of an App : Observer Pattern
    to do Implementation of observer pattern
    """
    # To do
    print("""
    When the state of an object changes,
    it will notify all other objects with the changes
    """)
    datasource = DataSources(value=5)
    chart = Chart()
    spreadsheet = SpreadSheet()
    datasource.add_observer(chart)
    datasource.add_observer(spreadsheet)
    datasource.value = 10
    datasource.value = 15



if __name__ == '__main__':
    main()
