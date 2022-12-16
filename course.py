"""
Author: Ronin Sharma
Date: December 14, 2022
"""

class Course:

    def __init__(self, name, credits, term, grade, category, requirement, id):
        """
        Attributes:
            name (string): course name
            credits (int): course's number of credits
            term (string): semester the course was taken
            grade (string): grade received for the course
            category (string): course category (N/A if no category)
            requirement (string): requirement the course satisfies
            id (int): course id
        """

        self.name = name
        self.credits = credits
        self.term = term
        self.grade = grade
        self.category = category
        self.requirement = requirement
        self.id = id
    
    def check_valid_name(self):
        """
        Returns True if a course has a valid name, False otherwise. 
        Invalid names are extra excel cells.
        """
        
        return self.name not in ['ECE Core/Foundation']

    def get_name(self):
        """
        Returns the name of the course
        """
        
        return self.name
    
    def get_credits(self):
        """
        Returns the number of credits the course is
        """
        
        return self.credits
    
    def get_term(self):
        """
        Returns the semester the course was taken
        """
        
        return self.term
    
    def get_grade(self):
        """
        Returns the grade received in the course
        """
        
        return self.grade

    def get_requirement(self):
        """
        Returns the requirement the course satisfies
        """
        
        return self.requirement
    
    def get_id(self):
        """
        Returns the id of the course
        """
        
        return self.id
    
    def get_missing(self):
        """
        Returns True if the course is missing information, False otherwise.
        """
        
        return 0 in [self.grade, self.term]

    def __str__(self):
        """
        Returns the course attributes in a readable format
        """
        
        return f'Course Name: {self.name}, Credits: {self.credits}, ' \
               f'Term: {self.term}, Grade: {self.grade}, ' \
               f'Category: {self.category}, Requirement: {self.requirement}, ' \
               f'Id: {self.id}'
