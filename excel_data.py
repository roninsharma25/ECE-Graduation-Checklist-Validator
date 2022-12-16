"""
Author: Ronin Sharma
Date: December 14, 2022
"""

from course import Course
from excel_map import ExcelMap
from constants import *

class ExcelData:

    def __init__(self, requirement_map):
        """
        Attributes:
            requirement_map (dict): stores the INITIAL mapping between requirements and courses
            course_mapping (dict): stores the NEW mapping between requirements and courses
            excel_map (dict): stores the mapping between course names and excel cells
            course_id (int): stores the id for the next course
            courses (list): all the courses in the excel file
        """

        self.requirement_map = requirement_map
        self.course_map = {}
        excel_map_obj = ExcelMap()
        excel_map_obj.create_excel_map()
        self.excel_map = excel_map_obj.get_excel_map()
        self.course_id = 0
        self.courses = []
    
    def create_courses(self):
        """
        Creates all courses in the excel file. Renames one of the column names.
        """
        
        for row in self.requirement_map:
            for course_ in self.requirement_map[row]:
                self.create_course(course_)

        self.course_map['OTHER'] = self.course_map.pop('N/A')
        

    def create_course(self, course_data):
        """
        Creates one course based on the data in part of one row in the excel file.
        """
        
        try:
            # Extract all information from the 4-5 excel cells
            course_requirement = 'N/A'
            if (course_data[0] in RIGHT_HALF):
                course_requirement = course_data[0]
                course_name = course_data[1]
            else:
                course_name = course_data[0]
            
            course_credits = course_data[2]
            course_category = 'N/A'

            if (course_requirement in CATEGORY):
                course_term = course_data[-2]
                course_grade = course_data[-1]
                if (course_requirement == 'LS'):
                    course_category = course_data[3]
            else:
                course_term = course_data[3]
                course_grade = course_data[4]

            course = Course(course_name, course_credits, course_term, course_grade, course_category, course_requirement, self.course_id)
            self.courses.append(course)
            self.update_course_map(course)
            self.update_excel_map(course, self.course_id)
            self.course_id += 1
            
        except: # not a course (easier excel processing)
            print("EXCEPTION:", course_data)

    def update_course_map(self, course):
        """
        Updates the course mapping based on the new course. The course mapping 
        maps between requirements and courses.
        """
        
        requirement = course.get_requirement()
        if (requirement in self.course_map):
            self.course_map[requirement].append(course)
        else:
            self.course_map[requirement] = [ course ]

    def update_excel_map(self, course, course_id):
        """
        Updates the excel mapping based on the new course and course id. The excel 
        mapping maps from course name to excel cell data and course id.
        """
        
        course_name = course.get_name()
        course_requirement = course.get_requirement()

        if (course_name == 'PE'):
            course_requirement = 'PE'

        if (course_name in self.excel_map):
            self.excel_map[course_name]['id'] = course_id
        elif (course_requirement in self.excel_map):
            self.excel_map[course_requirement]['id'] = course_id
        elif (f'{course_requirement}0' in self.excel_map): # PE, FWS, LS, AAE, 4000+, 3000+, OTE
            self.excel_map[f'{course_requirement}{DUPLICATE_COUNTS_DICT[course_requirement]}']['id'] = course_id
            DUPLICATE_COUNTS_DICT[course_requirement] += 1
            
    def get_course_map(self):
        """
        Returns the course mapping
        """
        
        return self.course_map

    def get_course_by_name(self, name):
        """
        Returns the course with the provided name
        """
        
        for course in self.courses:
            if (course.get_name() == name):
                return course

        return -1
    
    def get_course_by_id(self, id):
        """
        Returns the course with the provided id
        """
        
        for course in self.courses:
            if (course.get_id() == id):
                return course

        return -1
    
    def get_excel_data_by_course_id(self, id):
        """
        Returns the excel data for the course with the provided id
        """
        
        for course in self.excel_map.values():
            if (course['id'] == id):
                return course
        
        return -1
            
    def get_excel_map(self):
        """
        Returns the excel mapping
        """
        
        return self.excel_map
    
    def run(self):
        """
        Creates all courses in the requirement map
        """
        
        self.create_courses()
