import frappe
from frappe.model.document import Document
import appraise.controllers.form_validation as validation
import appraise.controllers.aggregatorController as agg
import re

Doctype = 'Institutional Governance Responsibilities'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class InstitutionalGovernanceResponsibilities(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI6_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = round(compute_marks(self))

	def on_trash(self):
        # Create on_trash method if not exists and call the delete method from aggregatorController
		agg.delete(self)
		
	def validate(self):
		
		validation.standard_validation(self)


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

			match = re.search(pattern_for_wtg, self.col3)
			if match:
				val3 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')
			
			match = re.search(pattern_for_wtg, self.col4)
			if match:
				val4 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')			

			pow = (val1+val2+val3+val4)*100

			if pow > 370:
				return 370

			return pow