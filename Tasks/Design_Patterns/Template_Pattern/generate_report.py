"""
Class Name: GenerateReport.py
Blue+print of:generating a report task
"""

from Tasks.Design_Patterns.Template_Pattern.tasks import Tasks


# Dependencies

# Internal Dependencies

# CONSTANTS

class GenerateReport(Tasks):
    """
    Purpose: Blueprint of generating a report task
    Methods:
        _do_execute : Will execute the steps that need to perform
    """

    def get_report(self) -> None:
        """ To perform: Will execute the steps that need to perform"""
        self._do_execute()

    def _do_execute(self) -> None:
        """ To perform: Will execute the steps that need to perform"""
        print("Generating an Report")
