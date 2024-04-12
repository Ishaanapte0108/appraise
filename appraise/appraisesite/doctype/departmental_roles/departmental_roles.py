import frappe
from frappe.model.document import Document
import appraise.controllers.form_validation as validation
import appraise.controllers.aggregatorController as agg
import re

Doctype = 'Departmental Roles'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class DepartmentalRoles(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AB5_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def on_trash(self):
        # Create on_trash method if not exists and call the delete method from aggregatorController
		agg.delete(self)
		
	def validate(self):
		
		validation.standard_validation(self)  


def compute_marks(self):
	
	match = re.search(pattern_for_wtg, self.roles)
	if match:
		val = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	return 50*val