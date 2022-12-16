"""
Author: Ronin Sharma
Date: December 14, 2022
"""

import sys
import pandas as pd
from requirement_checker import RequirementChecker
from grade_checker import GradeChecker
from excel_data import ExcelData
from constants import *

class GraduationChecker:

    def __init__(self, excel_file, grades_file):
        """
        Attributes:
            excel_file (string): populated graduation checklist excel file
            grades_file (string): populated grades data file
            requirement_map (dict): initial empty requirement map
        """
        
        self.excel_file = excel_file
        self.grades_file = grades_file
        self.requirement_map = REQUIREMENT_MAP

    def create_requirement_map(self):
        """
        Loads excel file and creates INITIAL requirement mapping.
        """
        
        df = pd.read_excel(self.excel_file)

        # Extract the relevant data for most courses
        data = df.iloc[8:35, 1:19].fillna(0).to_numpy()

        for row in data[2:]:
            categories = f'{row[0]}, {row[7]}'
                
            for requirement in self.requirement_map.keys():
                if (requirement in categories):
                    if (requirement in FIRST_HALF):
                        self.requirement_map[requirement].append(list(row)[:5])
                    else:
                        self.requirement_map[requirement].append(list(row)[7:13])

        # Extract data from extra courses
        extra_courses = df.iloc[37:45, 1:6].to_numpy()

        # Extract technical writing and advanced programming courses
        technical_writing = df.iloc[51, 1]
        advanced_programming = df.iloc[52, 1]
    
    def analyze_checklist(self):
        """
        Generates excel data and mapping objects, checks all requirements, and verify grades.
        """
        
        ed = ExcelData(self.requirement_map)
        ed.run()

        # Retrieve required data
        excel_mapping = ed.get_excel_map()
        course_mapping = ed.get_course_map()
        
        # Create requirement checker
        rc = RequirementChecker(ed, course_mapping, self.excel_file)
        rc.run()

        # Create grade checker
        gc = GradeChecker(self.grades_file, ed, excel_mapping, course_mapping, rc)
        gc.run()

        # Save the excel file
        rc.save_excel_file()

if __name__ == '__main__':
    excel_file = '2021-checklist-2720.xlsx' if len(sys.argv) < 2 else sys.argv[1]
    grades_file = 'ronin_grades.csv' if len(sys.argv) < 3 else sys.argv[2]
    gc = GraduationChecker(excel_file, grades_file)
    gc.create_requirement_map()
    gc.analyze_checklist()
