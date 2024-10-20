"""
Class Name: Tasks.py
Blue+print of:An abstract class for all the Tasks
"""
# Dependencies
from abc import ABC, abstractmethod

# Internal Dependencies
from Tasks.Design_Patterns.Template_Pattern.recorder import Recorder


class Tasks(ABC):
    """
    Purpose: Blueprint of An abstract class for all the Tasks
    Attributes:
         task_recorder: Recorder
    Methods:
         execute: "Will be called in main class"
         _do_execute: "An abstract protected method will be defined in the sub-class"
    """

    def __init__(self):
        """
        Attributes: task_recorder: Recorder
        """
        self.task_recorder: Recorder = Recorder()

    def execute(self) -> None:
        """ To perform: the following steps """
        self.task_recorder.start_record()

        self._do_execute()  # will be defined by child class

        self.task_recorder.stop_record()

    def dummy(self) -> None:
        """ To perform: the following steps """
        print("dummy")

    @abstractmethod
    def _do_execute(self) -> None:
        """An abstract-protected method will be defined in the subclass """
