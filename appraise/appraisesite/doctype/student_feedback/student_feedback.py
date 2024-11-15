import frappe
from frappe.model.document import Document
import appraise.controllers.form_validation as validation
import appraise.controllers.aggregatorController as agg

Doctype = 'Student Feedback'

class StudentFeedback(Document):
    """method to autoname your document"""
    def autoname(self):
        self.name = f'SD4_{self.owner}_{self.academic_year}_{self.semester}'
    
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
    all_values = []

    for item in self.feedback_attendance:
        count += 1
        temp_feedback = 0
        if item.feedback > 3.5:
            temp_feedback = 300
        elif 3.0 <= item.feedback <= 3.5:
            temp_feedback = 210
        elif 2.5 <= item.feedback < 3.0:
            temp_feedback = 150
        elif 0 <= item.feedback < 2.5:
            temp_feedback = 0
        else:
            temp_feedback = None
            frappe.throw(f'Feedback score entered incorrectly in row {count}')
    
        if not item.attendance:
            frappe.throw(f'Attendance not entered in row {count}')
        else:
            item.marks_obtained = temp_feedback*item.attendance // 100
        
        all_values.append(item.marks_obtained)

    for i in all_values:
        sum += i

    sap = sum // count
    if sap > 300:
        sap = 300
    
    return sap
