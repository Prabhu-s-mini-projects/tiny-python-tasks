"""
Class Name: ArticleDialogBox.py
Blue+print of:implements the abstract class of article dialog box
"""
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.button import Button
# Internal Dependencies
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.dialog_box import DialogBox
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.listbox import ListBox
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.textbox import TextBox
from Tasks.Design_Patterns.Mediator_Pattern.core_framework.ui_control import UIControl

# CONSTANTS

class ArticleDialogBox(DialogBox):
    """
    Purpose: Blueprint of implements the abstract class of article dialog box
    Attributes:
         list_box: ListBOX
         text_box: Textbox
    Methods:
        changed : implements the abstract method
    """
    def __init__(self):
        self.list_box = ListBox(owner=self)
        self.title_box= TextBox(owner=self)
        self.save_button = Button(owner=self)

    def changed(self, ui_control :UIControl) -> None:
        """ To perform: """
        if ui_control == self.list_box:
            self.title_box.content = self.list_box.selection
            self.save_button.is_enabled = True
        elif ui_control == self.title_box:
            content = self.title_box.content
            self.save_button.is_enabled = not "" in content

    def simulate(self)-> None:
        """To simulate scenario 1"""
        self.list_box.selection = "selected title"
        print(f"{ self.title_box.content = } ")
        print(f"{ self.save_button.is_enabled = } ")

    def simulate_scenario_2(self)-> None:
        """ To simulate scenario 2"""
        self.title_box.content = ""
        print(f"{ self.title_box.content = } ")
        print(f"{ self.save_button.is_enabled = } ")
