"""
Author: Ronin Sharma
Date: December 14, 2022
"""

import json
import requests
import pandas as pd
import numpy as np
import lxml.html as lh

from constants import NUM_LS_CAT, LS_REQUIREMENT_SATISFIER

class LiberalStudiesChecker:

    def __init__(self, ls_classes_taken):
        """
        Attributes:
            ls_classes_taken (list): liberal studies courses taken
            ls_data (DataFrame): scraped liberal studies' data
        """

        self.ls_classes_taken = ls_classes_taken

    def scrape_data(self):
        """
        Retrieves the current liberal studies courses and their categories.
        """
        
        categories = ['CA', 'HA', 'KCM', 'LA', 'SBA', 'CE', 'ALC', 'SCD', 'HST', 'ETM', 'SSC', 'GLC']
        completeData = []

        for category in categories:
            response = requests.get(f'https://apps.engineering.cornell.edu/liberalstudies/{category}.cfm')
            data = lh.fromstring(response.content)
            tableData = data.xpath('//tr')

            for row in tableData[1:]:
                rowElements = list(row.iterchildren())
                distributions = rowElements[3].text_content().split(', ')
                distributionsFormatted = []

                for distribution in distributions:
                    newStr = distribution.replace('(', '').replace(')', '')
                    distributionsFormatted.append(newStr)

                completeData.append([ category, f'{rowElements[0].text_content()} {rowElements[1].text_content()}', distributionsFormatted])

        df = pd.DataFrame(completeData)
        df.columns = ['Category', 'Department + Course Number', 'Distributions']
        df.to_csv('liberal_studies.csv', index = None)
        self.ls_data = df

    def check_ls_data(self):
        """
        Checks if the liberal studies courses taken satisfy the requirements.

        Returns:
            result (string): all categories satisfied and possible recommendations for other liberal studies courses
        """
        
        categories = []

        for class_ in self.ls_classes_taken:
            categories += [category for category in self.ls_data[ self.ls_data['Department + Course Number'] == class_].iloc[:, 0]]
        
        # Remove redundant categories
        categories = np.unique(categories)

        allCategories = LS_REQUIREMENT_SATISFIER.keys()
        possibleLSCourses = []

        for category in allCategories:
            if (category not in categories):
                possibleLSCourses.append( f'These courses: {", ".join(LS_REQUIREMENT_SATISFIER[category])} can be used to satisfy the {category} requirement.' )

        numLSCategories = len(categories)
        if (numLSCategories < NUM_LS_CAT):
            result = f'You have not taken enough LS categories. You have only taken {", ".join(categories)}, but you need {NUM_LS_CAT} categories. ' \
                     f'Here are some liberal studies suggestions -  {" ".join(possibleLSCourses)}'
        else:
            result = f'You have taken enough LS categories: {", ".join(categories)}'

        return result
