import math
import frappe
from frappe.model.document import Document
import appraise.controllers.form_validation as validation
import appraise.controllers.aggregatorController as agg
import re

Doctype = 'Administrative Co-Curricular Activities'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'


class AdministrativeCoCurricularActivities(Document):
    """method to autoname your document"""
    def autoname(self):
        self.name = f'AB2_{self.owner}_{self.academic_year}_{self.semester}'
    
    def before_save(self):
        self.self_appraisal_score = round(compute_marks(self))
        agg.modify(self, Doctype)

    def validate(self):
        validation.standard_validation(self)
    
    def on_trash(self):
        agg.delete(self)


def compute_marks(self):
    counter = 0
    pas = []

    for item in self.criteria_table:
        if counter > 1:
            frappe.throw('Can only have two entries in the table')
        else:
            counter += 1

            match = re.search(pattern_for_wtg, item.no_of_registered_students)
            if match:
                val1 = float(match.group(1).strip())
            else:
                frappe.throw('Error Fetching Field Weightages')

            match = re.search(pattern_for_wtg, item.activity_duration_in_hrs)
            if match:
                val2 = float(match.group(1).strip())
            else:
                frappe.throw('Error Fetching Field Weightages')

            match = re.search(pattern_for_wtg, item.student_feedback)
            if match:
                val3 = float(match.group(1).strip())
            else:
                frappe.throw('Error Fetching Field Weightages')
            
            pow = val1 * val2 * val3 * 100
            pas.append(round(pow))

    return math.floor(sum(pas))
