# ECE-Graduation-Checklist-Validator

### Goal
This application allows ECE students and faculty to automatically verify graduation requirements. Students upload their course history/grades and are informed of missing requirements. For some requirements, students receive recommendations of courses that can be used to satisfy that requirement.

### Setup
1. Update `2021-checklist-2720_original.xlsx` with your course history
2. Obtain your grade data (similar format to `ronin_grades.csv`)
3. Run `python graduation_checker.py <course-history-file.xlsx> <grade-file.csv>`
    * Install module dependencies as needed
4. Open the excel file and view the new sheet created
5. Profit!
