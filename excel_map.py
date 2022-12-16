"""
Author: Ronin Sharma
Date: December 14, 2022
"""

from constants import *

class ExcelMap:
    """
    Represents the cell information for a checklist's excel file.
    """

    def __init__(self):
        """
        Attributes:
            excel_map (dict): Stores class names and the corresponding excel cells
        """
        self.excel_map = {}
    
    def create_excel_map(self):
        """
        Creates the mapping between class names and excel cells. The 'num' attribute 
        represents the excel file's row number, and the 'letters' attribute represents 
        the excel file's cell letters. Each course has 4-5 cells that are in the 
        same row but have 4-5 letters.
        """
        
        for (index, course) in enumerate(FIRST_SECTION_COURSES):
            self.excel_map[course] = {'num': index + 12, 'letters': LEFT_HALF_LETTERS, 'id': -1}

        for (index, course) in enumerate(SECOND_SECTION_COURSES):
            self.excel_map[course] = {'num': index + 28, 'letters': LEFT_HALF_LETTERS, 'id': -1}

        for (index, course) in enumerate(THIRD_SECTION_COURSES):
            self.excel_map[course] = {'num': index + 12, 'letters': RIGHT_HALF_TOP_LETTERS, 'id': -1}

        for (index, course) in enumerate(FOURTH_SECTION_COURSES):
            self.excel_map[course] = {'num': index + 28, 'letters': RIGHT_HALF_BOTTOM_LETTERS, 'id': -1}

    def get_excel_map(self):
        """
        Returns the excel map
        """

        return self.excel_map
