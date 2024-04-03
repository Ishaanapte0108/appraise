import frappe, math as m
from frappe.model.document import Document
import appraise.controllers.form_validation as validation
import appraise.controllers.aggregatorController as agg
import re

Doctype = 'Internal revenue generation'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'


class Internalrevenuegeneration(Document):
    """method to autoname your document"""
    def autoname(self):
        self.name = f'CB1_{self.owner}_{self.academic_year}_{self.semester}'
    
    def before_save(self):
        self.self_appraisal_score = compute_marks(self)
        agg.modify(self, Doctype)

    def validate(self):
          validation.standard_validation(self)

    def on_trash(self):
        agg.delete(self)


def compute_marks(self):

    match = re.search(pattern_for_wtg, self.col1)
    if match:
        val1 = float(match.group(1).strip())
    else:
        frappe.throw('Error Fetching Field Weightages')
    
    match = re.search(pattern_for_wtg, self.col2)
    if match:
        val2 = float(match.group(1).strip())
    else:
        frappe.throw('Error Fetching Field Weightages')            

    marks_obtained = m.floor(val1 * val2 * 375)

    return marks_obtained
