"""
Author: Ronin Sharma
Date: December 14, 2022
"""

import pandas as pd
import numpy as np

class GradeChecker:

    def __init__(self, grade_file, excel_data, excel_mapping, course_mapping, requirement_checker):
        """
        Attributes:
            grade_file (string): file with the grade data
            excel_data (ExcelData): object with the data from the excel file
            excel_mapping (dict): stores the mapping between course names and excel cells
            course_mapping (dict): stores the mapping between requirements and couurses
            requirement_checker (RequirementChecker): object with the requirement checker functions
        """
        
        self.grade_file = grade_file
        self.excel_data = excel_data
        self.excel_mapping = excel_mapping
        self.course_mapping = course_mapping
        self.requirement_checker = requirement_checker
        self.grade_map = {}

    def load_grades(self):
        """
        Loads the grade data from the grade file
        """
        
        grade_data = pd.read_csv(self.grade_file).to_numpy()
        for class_ in grade_data:
            grade = class_[5]
            if (not pd.isnull(grade)):
                self.grade_map[f'{class_[3]} {class_[4]}'] = grade

    def compare_grades(self):
        """
        Checks if the grade's file has the same grades as the excel spreadsheet. 
        Prints out mismatches with the course name, specified grade, and actual grade.
        """
        
        for key in self.course_mapping:
            for course in self.course_mapping[key]:
                course_name = course.get_name()
                if (course_name not in ['PE', 'ECE Core/Foundation']):
                    course_id = self.excel_data.get_course_by_name(course_name).get_id()
                    course_grade = course.get_grade()
                    excel_data = self.excel_data.get_excel_data_by_course_id(course_id)
                    if (course_name not in self.grade_map):
                        if ('/' in course_name):
                            course_names = self.generate_course_names(course_name)
                            for name in course_names:
                                if name in self.grade_map and course_grade != self.grade_map[name]:
                                    print('MISMATCH', name, course_grade, self.grade_map[name])
                                    self.requirement_checker.update_cell_color(excel_data)
                        else:
                            self.requirement_checker.update_cell_color(excel_data)
                    elif (course_grade != self.grade_map[course_name]):
                        print('MISMATCH', course_name, course_grade, self.grade_map[course_name])
                        self.requirement_checker.update_cell_color(excel_data)
    
    def generate_course_names(self, name):
        """
        Creates several possible course names from the given name

        Arguments:
            name (string): the original course name
        
        Returns:
            A list of alternative course names
        """

        possible_names = []
        slash_index = name.index('/')
        space_index = name.index(' ')
        
        # DEPT ####/####
        dept = name[:space_index]
        first_num = name[space_index+1:slash_index]
        second_num = name[slash_index+1:]
        possible_names += [f'{dept} {first_num}', f'{dept} {second_num}']

        # DEPT ####/##
        first_two_digits = first_num[:2]
        possible_names += [f'{dept} {first_num}', f'{dept} {first_two_digits}{second_num}']

        # DEPT/DEPT ####
        first_dept = name[:slash_index]
        second_dept = name[slash_index+1:space_index]
        num = name[-4:]
        possible_names += [f'{first_dept} {num}', f'{second_dept} {num}']

        return np.unique(possible_names)

    def run(self):
        """
        Loads the grades and checks if they are valid
        """
        
        self.load_grades()
        self.compare_grades()
