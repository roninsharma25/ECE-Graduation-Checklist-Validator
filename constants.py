"""
Author: Ronin Sharma
Date: December 14, 2022
"""

# Graduation Checker ---
# Create a requirement mapping with each course
REQUIREMENT_MAP = {
    'MATH': [],
    'CS': [],
    'CHEM': [],
    'PHYS': [],
    'ECE': [],
    'PE': [],
    'FWS': [],
    'LS': [],
    'AAE': [],
    'ENGRD': [],
    'ENGRI': [],
    'CDE': [],
    '4000+': [],
    '3000+': [],
    'OTE': [],
}
FIRST_HALF = ['MATH', 'CS', 'CHEM', 'PHYS', 'ECE', 'PE']

# Excel Mapping ---
# Easy to modify for different excel formats
LEFT_HALF_LETTERS = ['B', 'C', 'D', 'E', 'F']
RIGHT_HALF_TOP_LETTERS = ['I', 'J', 'K', 'L', 'M', 'N']
RIGHT_HALF_BOTTOM_LETTERS = ['I', 'J', 'K', 'L', 'M']

# Top left
FIRST_SECTION_COURSES = ['MATH 1910', 'MATH 1920', 'MATH 2930', 'MATH 2940', 'CS 1110/1112', 'CHEM 2090',
                         'PHYS 1112/16', 'PHYS 1110', 'PHYS 2213/17', 'PHYS 2214/18', 'ECE/ENGRD 2300',
                         'PE0', 'PE1']

# Bottom left
SECOND_SECTION_COURSES = ['ECE 2100', 'ECE 2720', 'ECE 3030', 'ECE 3100', 'ECE 3140', 'ECE 3150', 'ECE 3250']

# Top right
THIRD_SECTION_COURSES = ['FWS0', 'FWS1', 'LS0', 'LS1', 'LS2', 'LS3', 'LS4', 'LS5', 'AAE0', 'AAE1', 'ENGRD', 'ENGRI']

# Bottom right
FOURTH_SECTION_COURSES = ['CDE', '4000+0', '4000+1', '3000+0', '3000+1', '3000+2', 'OTE0', 'OTE1', 'OTE2']

# Excel Data ---
RIGHT_HALF = ['FWS', 'LS', 'AAE', 'ENGRD', 'ENGRI', 'CDE', '4000+', '3000+', 'OTE']
CATEGORY = ['FWS', 'LS', 'AAE', 'ENGRD', 'ENGRI']

DUPLICATE_COUNTS_DICT = {
    'PE': 0,
    'FWS': 0,
    'LS': 0,
    'AAE': 0,
    '4000+': 0,
    '3000+': 0,
    'OTE': 0,
}

# Requirements ---
MULTI_OPTION = {
    'PROBABILITY': ['ENGRD 2700', 'ECE 3100'],
    'ADVANCED COMPUTING': ['CS 2110', 'ECE 2400', 
        'ENGRD 3200', 'AEP 4380', 'ECE 4740',
        'ECE 4750', 'ECE 4760'],
    'CDE': ['ECE 4370', 'ECE 4530', 'ECE 4670', 'ECE 4740', 'ECE 4750', 'ECE 4760'],
    'TECHNICAL WRITING': ['ENGRC 3020', 'ENGRC 3023', 'ENGRC 3025', 'ENGRC 3111', 
                          'ENGRC 3120', 'ENGRC 3152', 'ENGRC 3340', 'ENGRC 3350',
                          'ENGRC 3500', 'ENGRC 3610', 'ENGRC 3640', 'ENGRC 4152',
                          'ENGRC 4590'],
    'ENGRI': ['ENGRI 1100', 'ENGRI 1101', 'ENGRI 1120', 'ENGRI 1130', 'ENGRI 1140', 
              'ENGRI 1150', 'ENGRI 1160', 'ENGRI 1165', 'ENGRI 1170', 'ENGRI 1200', 
              'ENGRI 1210', 'ENGRI 1220', 'ENGRI 1270', 'ENGRI 1310', 'ENGRI 1337',
              'ENGRI 1620']
}

INVALID_UPPER_LEVEL_ECE = ['ECE 3600', 'ECE 4999', 'ECE 5830', 'ECE 5870', 'ECE 5880']
ECE_FOUNDATION = ['ECE 3030', 'ECE 3100', 'ECE 3140', 'ECE 3150', 'ECE 3250']

NUM_LS_CAT = 3
LS_REQUIREMENT_SATISFIER = {
    'CA': ['AAS 1100', 'AEM 4421', 'AIIS 1110', 'AMST 1101', 'ANTHR 1190'],
    'HA': ['AAS 2042', 'AIIS 1110', 'AMST 1540', 'ANTHR 1200', 'ARTH 2200'],
    'KCM': ['AEM 2020', 'AIIS 2100', 'AMST 3121', 'ANTHR 4101', 'ARAB 4867'],
    'LA': ['AAS 2620', 'AIIS 2600', 'AKKAD 1411', 'AMST 1312', 'ANTHR 3110'],
    'SBA': ['AAS 3400', 'AEM 1300', 'AIIS 2240', 'AMST 1104', 'ANTHR 2400'],
    'CE': ['ENGRC 3023', 'ENGRC 3350', 'ENGRC 3500']
}
