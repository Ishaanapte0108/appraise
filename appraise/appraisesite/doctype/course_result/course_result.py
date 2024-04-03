import frappe
from frappe.model.document import Document
import appraise.controllers.form_validation as validation
import appraise.controllers.aggregatorController as agg
# import re

Doctype = 'Course Result'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class CourseResult(Document):
    """method to autoname your document"""
    def autoname(self):
        self.name = f'SD2_{self.professor}_{self.academic_year}_{self.semester}'
    
    def before_save(self):
        self.self_appraisal_score = computemarks(self)
        agg.modify(self, Doctype)

    def validate(self):
        validation.standard_validation(self)
            
    def on_trash(self):
        agg.delete(self)
        
def computemarks(self):
    sum = 0
    count = 0
    for item in self.criteria_table:
        if item.c2 < 0 or item.c2 > 100:
            frappe.throw('Course Result percentage entered incorrectly')
        else:
            count +=1
            if item.c2 > 80:
                temp_marks = 700
            elif 70 < item.c2 <= 80:
                temp_marks = 590
            elif 60 < item.c2 <= 70:
                temp_marks = 470
            elif 50 < item.c2 <= 60:
                temp_marks = 350
            elif 40 < item.c2 <= 50:
                temp_marks = 240
            elif item.c2 < 40:
                temp_marks = 0
            else:
                frappe.throw('Something went wrong')
            sum+= temp_marks
            item.d3 = temp_marks
    
    return sum // count
